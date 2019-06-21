#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class OptionalLiteConan(ConanFile):
    name = "optional-lite"
    version = "2.3.0"
    url = "https://github.com/bincrafters/conan-optional-lite"
    homepage = "https://github.com/martinmoene/optional-lite"
    description = "A single-file header-only version of a C++17-like optional, a nullable object for C++98, C++11 and later"
    author = "Bincrafters <bincrafters@gmail.com>"

    license = "MIT"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"build_tests": [True, False]}
    default_options = {'build_tests': 'True'}
    topics = ("conan", "optional")

    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def source(self):
        tools.get("{0}/archive/v{1}.tar.gz".format(self.homepage, self.version),
                  sha256="8fe46216147234b172c6a5b182726834afc44dfdca1e976a264d6f96eb183916")
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)


    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_TESTS"] = self.options.build_tests
        cmake.configure(build_folder=self._build_subfolder)
        cmake.build()
        if self.options.build_tests:
            path_to_test_exe = os.path.join(self._build_subfolder, 'bin', 'optional-lite.t')
            self.run(path_to_test_exe)

    def package(self):
        include_folder = os.path.join(self._source_subfolder, "include")
        self.copy(pattern="LICENSE", dst="license", src=self._source_subfolder)
        self.copy(pattern="*", dst="include", src=include_folder)


    def package_id(self):
        self.info.header_only()

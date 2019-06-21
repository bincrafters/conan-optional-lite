#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class OptionalLiteConan(ConanFile):
    name = "optional-lite"
    version = "3.2.0"
    url = "https://github.com/bincrafters/conan-optional-lite"
    homepage = "https://github.com/martinmoene/optional-lite"
    description = "A single-file header-only version of a C++17-like optional, a nullable object for C++98, C++11 and later"
    author = "Bincrafters <bincrafters@gmail.com>"

    license = "MIT"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"build_tests": [True, False], "build_examples": [True, False]}
    default_options = {'build_tests': False, 'build_examples': False}
    topics = ("conan", "optional")

    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def source(self):
        tools.get("{0}/archive/v{1}.tar.gz".format(self.homepage, self.version),
                  sha256="069c92f6404878588be761d609b917a111b0231633a91f7f908288fc77eb24c8")
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)


    def build(self):
        cmake = CMake(self)
        cmake.definitions["OPTIONAL_LITE_OPT_BUILD_TESTS"] = self.options.build_tests
        cmake.definitions["OPTIONAL_LITE_OPT_BUILD_EXAMPLES"] = self.options.build_tests
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

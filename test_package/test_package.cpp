#include <cstdlib>
#include <iostream>
#include "nonstd/optional.hpp"

using nonstd::optional;
using nonstd::nullopt;

optional<int> to_int( char const * const text )
{
    char * pos = NULL;
    const int value = strtol( text, &pos, 0 );

    return pos == text ? nullopt : optional<int>( value );
}

int main(int argc, char * argv[])
{
    std::cout << "Bincrafters\n";
    
    const char * text = argc > 1 ? argv[1] : "42";

    optional<int> oi = to_int( text );

    if ( oi ) std::cout << "'" << text << "' is " << *oi;
    else      std::cout << "'" << text << "' isn't a number";
    
    return EXIT_SUCCESS;
}

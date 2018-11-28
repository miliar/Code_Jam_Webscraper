
#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

int pancake_flipper( std::vector<bool>& s, int k )
{
    size_t first_non_happy = 0;
    int flips = 0;

    while ( first_non_happy < s.size( ) && s[first_non_happy] )
    {
        first_non_happy++;
    }

    while ( first_non_happy + k <= s.size( ) )
    {
        for ( size_t idx = first_non_happy; idx < first_non_happy + k; ++idx )
        {
            s[idx] = !s[idx];
        }
        ++flips;

        while ( first_non_happy < s.size( ) && s[first_non_happy] )
        {
            first_non_happy++;
        }
    }

    if ( first_non_happy == s.size( ) )
    {
        return flips;
    }
    else
    {
        return std::numeric_limits<int>::max( );
    }
}

int main()
{
    int numTestCases = 0;
    std::cin >> numTestCases;

    for(int testCase = 0; testCase < numTestCases; testCase++)
    {
        std::vector<bool> s;

        char c;
        std::cin.get(c);
        while (std::cin.get(c))
        {
            if( c == '+' )
            {
                s.push_back( true );
            }
            else if( c == '-' )
            {
                s.push_back( false );
            }
            else
            {
                break;
            }
        }

        int k;
        std::cin >> k;

        int result = pancake_flipper(s, k);
        std::cout << "Case #" << (testCase + 1) << ": ";
        if (result == std::numeric_limits<int>::max( ) )
        {
            std::cout << "IMPOSSIBLE";
        }
        else
        {
            std::cout << result;
        }
        std::cout << std::endl;
    }
}

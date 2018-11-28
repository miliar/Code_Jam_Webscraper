
#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

long long tidy( long long input )
{
    std::vector< int > v;
    while( input )
    {
        v.push_back( input % 10 );
        input /= 10;
    }

    std::reverse( v.begin( ), v.end( ) );

    long long out = 0;
    bool switched = false;
    int prev = 0;
    for (int d: v)
    {
        out *= 10;
        if (switched)
        {
            out += 9;
        }
        else
        {
            if (prev <= d)
            {
                out += d;
                prev = d;
            }
            else
            {
                --out;
                switched = true;
            }
        }
    }

    return switched ? tidy(out) : out;
}

int main()
{
    int numTestCases = 0;
    std::cin >> numTestCases;

    for(int testCase = 0; testCase < numTestCases; testCase++)
    {
        long long value;

        std::cin >> value;

        std::cout << "Case #" << (testCase + 1) << ": " << tidy( value ) << std::endl;
    }
}

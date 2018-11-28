#include <iostream>
#include <math.h>
#include <string>
#include <fstream>
#include <sstream>

namespace patch
{
    template < typename T > std::string to_string( const T& n )
    {
        std::ostringstream stm ;
        stm << n ;
        return stm.str() ;
    }
}

int main() {
    std::ofstream file ("output",std::ofstream::trunc);
    int T;
    long long int N;
    std::cin >> T;
    for ( int i = 0; i < T; i++ )
    {
        std::cin >> N;
        long long int L = 0;
        long long int C;
        int E;
        int len;
        len = N > 0 ? floor(log10(N)) + 1 : 1;
        int split[len];
        bool maxOut = false;
        C = N;
        for ( int j = len - 1; j >= 0; j-- )
        {
            E = C % 10;
            split[j] = E;
            C = ( C - E ) / 10;
        }
        if ( len == 1 )
        {
            L += N;
        }
        else
        {
            for ( int j = len -1 ; j > 0; j-- )
            {
                if ( split[j] < split[j-1] )
                {
                    split[j] = 9;
                    split[j-1] = split[j-1] - 1;
                }
            }
            for ( int j = 0; j < len; j++ )
            {
                L = L * 10;
                if ( maxOut || ( j >= 1 && split[j] < split[j-1] ) )
                {
                    L += 9;
                    maxOut = true;
                }
                else
                {
                    L += split[j];
                }
            }
        }
        std::string output = "Case #" + patch::to_string(i+1) + ": " + patch::to_string(L);
        file << output << std::endl;
        std::cout << output << std::endl;
    }
    std::cout << "output file written" << std::endl;
    return 0;
}
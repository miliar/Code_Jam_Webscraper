#include <iostream>
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

int main()
{
    std::ofstream output ("output",std::ofstream::trunc);
    int T;
    std::string S;
    int K;
    std::cin >> T;
    for (int i = 0; i < T; i++) {
        int F = 0;
        bool R = true;
        std::cin >> S >> K;
        for(int j = 0; j < S.length(); j++)
        {
            if (j + K <= S.length())
            {
                if (S[j] == '-')
                {
                    F++;
                    for (int k = j; k < j + K; k++)
                    {
                        if (S[k] == '+')
                        {
                            S[k] = '-';
                        }
                        else
                        {
                            S[k] = '+';
                        }
                    }
                }
            }
            else
            {
                if (S[j] == '-')
                {
                    R = false;
                }
            }
        }
        std::string outSting = "Case #" + patch::to_string(i + 1) + ": " + ( R ? ( F > 0 ? patch::to_string(F) : "0" ) : "IMPOSSIBLE" );
        output << outSting << std::endl;
    }
    std::cout << "output file written" << std::endl;
    return 0;
}
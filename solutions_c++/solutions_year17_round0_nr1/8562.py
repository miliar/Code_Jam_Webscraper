#include <algorithm>
#include <iostream>
#include <string>

int calcFlips(std::string S, int K)
{
    int pluses = std::count(S.begin(), S.end(), '+');

    int size = S.size();
    if(pluses == size)
        return 0;

    int i = 0;
    int flips = 0;
    while(i < size)
    {
        for(i = 0; i < size; ++i)
        {
            if(S[i] == '-')
            {
                if(i >= size - K + 1)
                    return -1;

                for(int j = i; j < i + K; ++j)
                {
                    if(S[j] == '+')
                        S[j] = '-';
                    else
                        S[j] = '+';
                }
                ++flips;
            }
        }
    }

    return flips;
}

int main(int argc, char* argv[])
{
    int T = 0;
    std::cin >> T;

    for(int i = 0; i < T; ++i)
    {
        std::string S;
        int K = 0;
        std::cin >> S >> K;
        int flips = calcFlips(S, K);

        std::cout << "Case #" << i+1 << ": " << (flips == -1 ? "IMPOSSIBLE" : std::to_string(flips).c_str()) << std::endl;
    }

    return 0;
}


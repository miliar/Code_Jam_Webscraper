#include <iostream>
#include <string>

int calculate(std::string &&S, const int K)
{
    if (S.find_first_not_of('+') == std::string::npos)
    {
        return 0;
    }
    unsigned long length = S.length();
    int ret = 0;
    do
    {
        size_t first = S.find_first_of('-');
        if (first + K > length)
        {
            return -1;
        }
        for (size_t i = first; i < first + K; i++)
        {
            if (S[i] == '-')
            {
                S[i] = '+';
            } else
            {
                S[i] = '-';
            }
        }
        ret++;
    } while (S.find_first_of('-') != std::string::npos);

    return ret;
}

int codeJam()
{
    int T;
    std::cin >> T;
    if (T < 1 || T > 100)
    {
        return 1;
    }
    std::string S;
    int K;
    for (int t = 0; t < T; t++)
    {
        std::cin >> S >> K;
        if (K < 2 || K > S.length())
        {
            return 2;
        }
        if (S.find_first_not_of("-+") != std::string::npos)
        {
            return 3;
        }
        int y = calculate(std::move(S), K);
        if (y >= 0)
        {
            printf("Case #%i: %i\n", t + 1, y);
        } else
        {
            printf("Case #%i: IMPOSSIBLE\n", t + 1);
        }
    }

    return 0;
}

int main()
{
    return codeJam();
}
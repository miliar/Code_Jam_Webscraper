#include <iostream>
#include <utility>

#define UINT64 unsigned long long int


std::pair<UINT64, UINT64>* solve(UINT64 n, UINT64 k)
{
    std::pair<UINT64, UINT64>* result = new std::pair<UINT64, UINT64>();

    while (k > 0) {
        if (n % 2 != 0)
        {
            result->first = n / 2;
            result->second = n / 2;
        }
        else
        {
            result->first = n / 2;
            result->second = n / 2 - 1;
        }

        if (n % 2 == 0 && k % 2 != 0)
        {
            n = n / 2 - 1;
        }
        else
        {
            n = n / 2;
        }

        k /= 2;
    }

    return result;
}

int main(int argc, char** argv)
{
    int t;
    std::cin >> t;

    for (int i = 0; i < t; ++i)
    {
        UINT64 n, k;
        std::cin >> n >> k;
        std::pair<UINT64, UINT64>* solution = solve(n, k);

        std::cout << "Case #" << i + 1 << ": " << solution->first << " "
                  << solution->second << std::endl;

        delete solution;
    }

    return 0;
}

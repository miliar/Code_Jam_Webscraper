#include <vector>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <string>

int main()
{
    freopen("d:\\dropbox\\code\\bin\\input.txt", "r", stdin);
    freopen("d:\\dropbox\\code\\bin\\output.txt", "w", stdout);

    int T;
    std::cin >> T;

    for (int t = 1; t <= T; t++)
    {
        long long n;
        std::cin >> n;

        long long power = 1;
        int last = 9;
        while (power <= n)
        {
            int digit = (n / power) % 10;
            if (digit > last)
            {
                n -= n % power + 1;
                digit--;
            }

            power *= 10;
            last = digit;
        }

        std::cout << "Case #" << t << ": " << n << std::endl;
    }

    return 0;
}
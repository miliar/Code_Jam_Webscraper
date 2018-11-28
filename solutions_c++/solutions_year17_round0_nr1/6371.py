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
        int k = 0;
        std::string pan;

        std::cin >> pan >> k;

        int flipCount = 0;
        bool impossible = false;

        while (!impossible && std::count(pan.begin(), pan.end(), '+') != pan.size())
        {
            for (int i = 0; i < pan.size() && !impossible; i++)
            {
                if (pan[i] == '-')
                {
                    if (pan.size() - i >= k)
                    {
                        std::transform(pan.begin() + i, pan.begin() + i + k, pan.begin() + i, [](const char& c) { return c == '+' ? '-' : '+'; });
                        flipCount++;
                    }
                    else
                    {
                        impossible = true;
                    }
                }
            }
        }

        std::cout << "Case #" << t << ": ";
        if (impossible)
        {
            std::cout << "IMPOSSIBLE" << std::endl;
        }
        else
        {
            std::cout << flipCount << std::endl;
        }
    }

    return 0;
}
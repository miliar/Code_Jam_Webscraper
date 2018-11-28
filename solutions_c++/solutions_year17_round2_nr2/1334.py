#include <vector>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <string>
#include <array>

int main()
{
    freopen("/Users/screamer/Dropbox/Code/bin/input.txt", "r", stdin);
    freopen("/Users/screamer/Dropbox/Code/bin/output.txt", "w", stdout);

    const std::array<char, 6> colors = { 'R', 'O', 'Y', 'G', 'B', 'V' };

    int T;
    std::cin >> T;
    for (int t = 1; t <= T; t++)
    {
        int n;
        std::cin >> n;

        std::array<int, 6> unicorns;
        std::copy_n(std::istream_iterator<int>(std::cin), 6, unicorns.begin());
        
        int left = n;
        std::string result;
        while (left)
        {
            int minAmount = std::numeric_limits<int>::max();
            for (int i = 0; i < unicorns.size(); i++)
            {
                if (unicorns[i] != 0)
                    minAmount = std::min(minAmount, unicorns[i]);
            }

            std::string cycle;
            for (int i = 0; i < unicorns.size(); i++)
            {
                if (unicorns[i] != 0)
                {
                    cycle += colors[i];
                    unicorns[i] -= minAmount;
                }
            }

            if (cycle.size() > 1)
            {
                for (int i = 0; i < minAmount; i++)
                    result += cycle;
            }
            else
            {
                for (int i = 0, toInsert = minAmount; toInsert && i < result.size(); i++)
                {
                    if (result[i] != cycle[0] && result[(result.size() + i - 1) % result.size()] != cycle[0])
                    {
                        result.insert(std::next(result.begin(), i), cycle[0]);
                        toInsert--;
                    }
                }
            }

            left -= cycle.size() * minAmount;
        }

        if (result.size() == n)
        {
            std::cout << "Case #" << t << ": " << result << std::endl;
        }
        else
        {
            std::cout << "Case #" << t << ": " << "IMPOSSIBLE" << std::endl;
        }
    }

    return 0;
}
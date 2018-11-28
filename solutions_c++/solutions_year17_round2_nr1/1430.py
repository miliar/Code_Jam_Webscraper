#include <vector>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <string>
#include <set>

int main()
{
    freopen("/Users/screamer/Dropbox/Code/bin/input.txt", "r", stdin);
    freopen("/Users/screamer/Dropbox/Code/bin/output.txt", "w", stdout);
    
    std::cout.setf(std::ios_base::fixed, std::ios_base::floatfield);
    std::cout.precision(6);

    int T;
    std::cin >> T;
    for (int t = 1; t <= T; t++)
    {
        int d, n;
        std::cin >> d >> n;

        double maxTime = 0;
        while (n--)
        {
            int k, s;
            std::cin >> k >> s;

            maxTime = std::max(maxTime, (d - k) / (double)s);
        }

        std::cout << "Case #" << t << ": " << d / maxTime << std::endl;
    }

    return 0;
}
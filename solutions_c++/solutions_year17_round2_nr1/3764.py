#include <stdio.h>
#include <tchar.h>
#include <iostream>
#include <vector>

#include <string>

#define uint64 unsigned long long


void cruise_control()
{
    int t;

    uint64 d, n, k;

    std::cin >> t;

    for (unsigned tt = 0; tt < t; ++tt)
    {
        std::cin >> d >> n;

        std::vector<std::pair<uint64, double>> horses;
        for (unsigned nn = 0; nn < n; ++nn)
        {
            uint64 horseDist;
            double horseSpeed;
            std::cin >> horseDist >> horseSpeed;

            horses.push_back(std::make_pair( horseDist, horseSpeed));

        }

        double maxTime = 0;
        for (int h = horses.size() - 1; h >= 0; h--)
        {
            double time = ( d - horses[h].first ) / horses[h].second;
            if (time > maxTime)
            {
                maxTime = time;
            }
        }

        double speed = d / maxTime;

        std::cout << std::fixed << "Case #" << tt + 1 << ": " << speed << std::endl;

    }
}


int main()
{
    cruise_control();

    char inputEnd = getchar();
    inputEnd = getchar();

    return 0;
}
// CodeJame2017.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <inttypes.h>
#include <stdint.h>
#include <fstream>
#include <sstream>
#include <string>
#include <bitset>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

#define DB false

void cake(int R, int C, std::ifstream& input)
{
    printf("\n");
    char theCake[25][25] = {};

    for (int r = 0; r < R; r++)
    {
        for (int c = 0; c < C; c++)
        {
            char foo;
            input >> foo;
            if (foo != '?')
                theCake[r][c] = foo;
        }
        std::string line;
        std::getline(input, line);
    }

    auto canFill = [&](char init, int mr, int mc, int lr, int lc)
    {
        for (int r = mr; r <= lr && r < R; r++)
        {
            for (int c = mc; c <= lc && c < C; c++)
            {
                if (theCake[r][c] != 0 && theCake[r][c] != init)
                {
                    return false;
                }
            }
        }
        return true;
    };

    auto fill = [&](char init, int mr, int mc, int lr, int lc)
    {
        for (int r = mr; r <= lr && r < R; r++)
        {
            for (int c = mc; c <= lc && c < C; c++)
            {
                theCake[r][c] = init;
            }
        }
    };

    std::set<char> filled;

    for (int r = 0; r < R; r++)
    {
        for (int c = 0; c < C; c++)
        {
            if (theCake[r][c] != 0 && filled.find(theCake[r][c]) == filled.end())
            {
                int mr = r, mc = c, lr = r, lc = c;
                // up
                while(mr - 1 >= 0 && canFill(theCake[r][c], mr - 1, mc, lr, lc))
                {
                    mr -= 1;
                }
                // down
                while (lr + 1 < R && canFill(theCake[r][c], mr, mc, lr + 1, lc))
                {
                    lr += 1;
                }
                // left
                while (mc - 1 >= 0 && canFill(theCake[r][c], mr, mc - 1, lr, lc))
                {
                    mc -= 1;
                }
                // right
                while (lc + 1 < C && canFill(theCake[r][c], mr, mc, lr, lc + 1))
                {
                    lc += 1;
                }

                fill(theCake[r][c], mr, mc, lr, lc);

                filled.insert(theCake[r][c]);
            }
        }
    }

    for (int r = 0; r < R; r++)
    {
        for (int c = 0; c < C; c++)
        {
            printf("%c", theCake[r][c]);
        }
        printf("\n");
    }
}


int main()
{
    std::ifstream input("1.in");

    int cases = 0;
    input >> cases;

    std::string line;
    std::getline(input, line);

    for (int caseNumber = 0; caseNumber < cases; caseNumber++)
    {
        printf("Case #%d:", caseNumber + 1);

        int R, C;
        input >> R >> C;

        cake(R, C, input);

        //printf("\n");
    }

    DB && getchar();


    return 0;
}


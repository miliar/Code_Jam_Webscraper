// CodeJame2017.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdint.h>
#include <fstream>
#include <sstream>
#include <string>
#include <bitset>
#include <vector>
#include <algorithm>

#define DB false

void pancake(std::string cakeLine, int k)
{
    /*
    auto checkStart = [&]()
    {
        char start = cakeLine[0];
        for (int i = 1; i < k; i++)
        {
            if (cakeLine[i] != start)
            {
                return false;
            }
        }
        return true;
    };

    if (!checkStart())
    {
        std::reverse(cakeLine.begin(), cakeLine.end());
        if (!checkStart())
        {
            printf("IMPOSSIBLE");
            return;
        }
    }
    */

    DB && printf("%s\n", cakeLine.c_str());

    std::string original = cakeLine;

    auto check = [&]()
    {
        DB && printf("%s\n", cakeLine.c_str());
        for (int i = 1; i < cakeLine.length(); i++)
        {
            if (cakeLine[i] != '+')
            {
                return false;
            }
        }
        return true;
    };

    auto flip = [&](int pos)
    {
        for (int i = 0; i < k; i++)
        {
            cakeLine[pos + i] = cakeLine[pos + i] == '+' ? '-' : '+';
        }
    };

    int flips = 0;
    for (int i = 0; i <= cakeLine.length() - k; i++)
    {
        if (cakeLine[i] != '+')
        {
            flip(i);
            flips++;
        }
    }

    if (check())
    {
        printf("%d", flips);
        return;
    }

    cakeLine = original;
    
    std::reverse(cakeLine.begin(), cakeLine.end());

    DB && printf("%s\n", cakeLine.c_str());

    flips = 0;
    for (int i = 0; i <= cakeLine.length() - k; i++)
    {
        if (cakeLine[i] != '+')
        {
            flip(i);
            flips++;
        }
    }

    if (check())
    {
        printf("%d", flips);
    }
    else
    {
        printf("IMPOSSIBLE");
    }
}


int main()
{
    std::ifstream input("1.in");

    int cases = 0;
    input >> cases;

    //std::string line;
    //std::getline(input, line);

    for (int caseNumber = 0; caseNumber < cases; caseNumber++)
    {
        printf("Case #%d: ", caseNumber + 1);

        std::string cakeLine;
        int k;
        input >> cakeLine >> k;

        pancake(cakeLine, k);

        printf("\n");
    }

    //DB && getchar();


    return 0;
}


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

void tidy(std::string input)
{
    //int arr[20];
    //for (int i = input.length() - 1; i >= 0; i--)
    //{
    //
    //}

    if (input.length() == 1)
    {
        printf("%s", input.c_str());
        return;
    }

    //auto isTidy = [&](std::string input)
    //{
    //    char first = input[0];
    //    for (int i = 0; i < input.length() - 1; i++)
    //    {
    //        if (input[i] > input[i + 1])
    //        {
    //            return false;
    //        }
    //    }
    //    return true;
    //};

    //int tidyPos = input.length();
    for (int i = 0; i < input.length() - 1; i++)
    {
        if (input[i] > input[i + 1])
        {
            //tidyPos = i - 1;
            for (int j = i + 1; j < input.length(); j++)
            {
                input[j] = '9';
            }
            input[i] -= 1;
            i = -1;
        }
    }
    if (input[0] == '0')
    {
        input = input.substr(1);
    }

    printf("%s", input.c_str());

    /*
    for (int i = 0; i < input.length(); i++)
    {
        if (i <= tidyPos)
        {
            printf("%c", input[i]);
        }
        else if (i == tidyPos + 1)
        {
            if (input[i] != '1')
            {
                printf("%c", input[i] - 1);
            }
        }
        else
        {
            printf("9");
        }
    }
    */
}


int main()
{
    std::ifstream input("2.in");

    int cases = 0;
    input >> cases;

    std::string line;
    std::getline(input, line);

    for (int caseNumber = 0; caseNumber < cases; caseNumber++)
    {
        printf("Case #%d: ", caseNumber + 1);

        //int64_t N;
        //input >> N;

        std::getline(input, line);

        tidy(line);

        printf("\n");
    }

    DB && getchar();


    return 0;
}


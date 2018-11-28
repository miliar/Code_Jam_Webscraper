// ConsoleApplication1.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <string>
#include <iostream>
#include <sstream>
#include <set>


using namespace std;

int N;
std::set<int> myset = {};


void Do(int X)
{
    auto search = myset.find(X);
    if (search == myset.end()) {
        myset.insert(X);
    }
    else {
        myset.erase(X);
    }

}

void Print(int TID)
{
    printf("Case #%d: ", TID);
    for (auto it = myset.begin(); it != myset.end(); it++)
    {
        printf("%d ", *it);
    }
    printf("\n");

}

int main()
{
    string input_line;
    unsigned long long int  T;
    scanf_s("%lld", &T);
    std::getline(std::cin, input_line);

    //Each Test Case
    for (int i = 1; i <= T; i++)
    {
        myset = {};
        scanf_s("%d", &N); std::getline(std::cin, input_line);
        for (int j = 1; j <= (2 * N - 1); j++)
        {
            for (int k = 0; k < N; k++)
            {
                int X;
                scanf_s("%d", &X);
                Do(X);
            }
            std::getline(std::cin, input_line);

        }
        Print(i);
    }
    return 0;
}



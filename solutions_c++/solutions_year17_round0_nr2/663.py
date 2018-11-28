// ConsoleApplication1.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <string>
#include <iostream>
#include <sstream>
#include <set>


using namespace std;
unsigned long long int T;
int K;
int len;
int flips;
bool ok;

string input_line;

void Do()
{
    int index = 0;
    while ((index < len - 1) && (input_line[index] <= input_line[index + 1]))
    {
        index++;
    }

    if (!( index == len-1 || len==1 ))
    {
        char ch = input_line[index];

        while ((index >= 0) && (input_line[index] == ch))
        {
            input_line[index]--;
            index--;
        }
        index++;

        for (int i = index + 1; i < len; i++)
        {
            input_line[i] = '9';
        }

        int zc = 0;
        while ((zc < len) && (input_line[zc] == '0'))
        {
            zc++;
        }
        input_line.erase(0, zc);
    }
}


void Print(int TID)
{
    cout << "Case #" << TID << ": " << input_line << "\n";
}

int main()
{

    scanf_s("%lld", &T);
    std::getline(std::cin, input_line);

    //Each Test Case
    for (int i = 1; i <= T; i++)
    {

      std::getline(std::cin, input_line);
      len = input_line.length();

        Do();

        Print(i);
    }
    return 0;
}



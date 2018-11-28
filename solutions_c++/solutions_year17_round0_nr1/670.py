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
bool P[1001];
bool ok;

void Do()
{
    ok = true;
    flips = 0;
    int i = 0;
    while (i <= len - K)
    {
        if (!P[i])
        {
            flips++;
            for (int j = i; j < i + K; j++)
            {
                P[j] = !P[j];
            }
        }
        i++;
    }

    while ((i < len) && ok)
    {     
        ok = ok && P[i];
        i++;
    }
}

void Print(int TID, int R)
{
    printf("Case #%d: ", TID);
    if (ok)
    {
        printf("%d", R);
    }
    else {
        printf("IMPOSSIBLE");
    }

    printf("\n");

}

int main()
{
    string input_line;
    
    scanf_s("%lld", &T);
    std::getline(std::cin, input_line);

    //Each Test Case
    for (int i = 1; i <= T; i++)
    {
        char ch = 'X';
        len = -1;
        while (ch != ' ')
        {   
            len++;
            scanf_s("%c", &ch); 
            P[len] = (ch == '+');
        }

        scanf_s("%d", &K); std::getline(std::cin, input_line);
        
        Do();

        Print(i, flips);
    }
    return 0;
}



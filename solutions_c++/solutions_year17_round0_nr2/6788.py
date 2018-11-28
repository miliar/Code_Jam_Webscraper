/**************************************************
    WhatTheFua
    Anan Schuett
    arnan_s@msn.com
**************************************************/

#define BK back()
#define BL for(int K = 1; K <= T; K++)
#define F first
#define INF 2147483647LL
#define LNF 8000000000000000000LL
#define P107 1000000007LL
#define P109 1000000009LL
#define PB push_back
#define PF push_front
#define I insert
#define E erase
#define S second
#define SZ size()
#define IT iterator
#define db double
#define ll long long int
#define mp make_pair

#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;

char str[30];

bool checkFirstDigit()
{
    for(int i = 1; str[i] != 0; i++)
    {
        if(str[i] < str[0])
        {
            return 1;
        } else if(str[i] > str[0]) {
            return 0;
        }
    }

    return 0;
}

void calFirstDigit(int loop)
{
    printf("Case #%d: ", loop);

    if(str[0] != '1')
    {
        printf("%c", str[0] - 1);
    }

    for(int i = 1; str[i] != 0; i++)
    {
        printf("9");
    }

    printf("\n");
}

int main()
{
    int T, i, j;

    scanf("%d", &T);

    BL
    {
        scanf("%s", str);

        if(checkFirstDigit())
        {
            calFirstDigit(K);
            continue;
        } else if(str[1] == 0) {
            printf("Case #%d: %c\n", K, str[0]);
        } else {
            for(i = 0; str[i] != 0; i++)
            {
                for(j = i + 1; str[j] != 0; j++)
                {
                    if(str[i] > str[j])
                    {
                        str[i]--;

                        for(j = i + 1; str[j] != 0; j++)
                        {
                            str[j] = '9';
                        }

                        j = -1;
                    } else if(str[i] < str[j]) {
                        break;
                    }

                    if(j == -1)
                    {
                        break;
                    }
                }

                if(j == -1)
                {
                    break;
                }
            }

            printf("Case #%d: %s\n", K, str);
        }
    }
}

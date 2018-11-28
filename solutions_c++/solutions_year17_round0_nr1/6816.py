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

char str[1010];

bool valid()
{
    for(int i = 0; str[i] != 0; i++)
    {
        if(str[i] == '-')
        {
            return 0;
        }
    }
    return 1;
}

int main()
{
    int T, i, j, k, res, n;

    scanf("%d", &T);

    BL
    {
        scanf("%s%d", str, &k);

        res = 0;
        n = strlen(str);

        for(i = 0; i < n - k + 1; i++)
        {
            if(str[i] == '-')
            {
                res++;

                for(j = i; j < i + k; j++)
                {
                    str[j] = (str[j] == '+')? '-': '+';
                }
            }
        }

        (valid())? printf("Case #%d: %d\n", K, res): printf("Case #%d: IMPOSSIBLE\n", K);
    }
}

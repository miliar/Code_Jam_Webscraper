//#pragma warning (disable: 4786)
//#pragma comment (linker, "/STACK:16777216")
//HEAD
//include <bits/stdc++.h>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <string>
#include <set>
#include <stack>
#include <map>
#include <cmath>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
const int maxn = 10010;

char str[25];
int set_all(int st)
{
    for (int i = st; i < strlen(str); i++) {
        str[i] = '9';
    }
}
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    int ncase = 1;
    scanf("%d", &T);
    while (T--) {
        scanf("%s", str);
        int n = strlen(str);
        while (1) {
            int update_flag = 0;
            for (int i = 0; i < n-1; i++) {
                if (str[i] > str[i+1]) {
                    update_flag = 1;
                    str[i]--;
                    set_all(i+1);
                }
            }
            if (!update_flag) break;
        }
        printf("Case #%d: ", ncase++);
        int flag = 0;
        for (int i = 0; i < n; i++) {
            if (str[i] != '0' || flag) {
                flag = 1;
                putchar(str[i]);
            }
        }
        puts("");
    }

    return 0;
}



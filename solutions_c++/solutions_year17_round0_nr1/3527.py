#include <iostream>
#include <vector>
#include <set>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cstring>
#include <algorithm>
#include <string>
#include <cmath>
#include <fstream>
#include <map>
using namespace std;
const int N = 2120;

char s[N];
int t, k;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("ans.txt", "w", stdout);
    scanf("%d", &t);
    for(int i=1; i<=t; i++)
    {
        scanf("%s%d", s, &k);
        int len = strlen(s);
        int ans = 0;
        bool flag = true;
        int idx = 0;
        while(idx<=len-k)
        {
            if(s[idx] == '+')
            {
                idx += 1;
                continue;
            }
            ans += 1;
            for(int j=idx; j<idx+k; j++)
            {
                if(s[j] == '+') s[j] = '-';
                else if(s[j] == '-') s[j] = '+';
            }
            idx += 1;
        }
        for(int j=idx; j<len; j++)
        {
            if(s[j] == '-')
            {
                flag = false;
                break;
            }
        }
        if(flag)
        {
            printf("Case #%d: %d\n", i, ans);
        }
        else
        {
            printf("Case #%d: IMPOSSIBLE\n", i);
        }
    }
    return 0;
}


#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
#include <vector>
#include <queue>

#define eps 1e-8
#define MOD 10009
#define MAXN 25
#define INF 99999999
using namespace std;
int equ,var;
int a[MAXN][MAXN];
int x[MAXN];

char str[MAXN];
int main()
{
//    freopen("A-small-attempt0.in","r",stdin);
//    freopen("A-small-attempt0.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++)
    {
        int n;
        scanf("%s",str);
        n=strlen(str);
        int cur=n-1;
        while(cur>0)
        {
            if(str[cur]<str[cur-1])
            {
                str[cur-1]--;
                for(;cur<n&&str[cur]!='9';cur++)
                    str[cur]='9';
            }
            cur--;
        }
        printf("Case #%d: ",kase);
            printf("%s\n",str+(str[0]=='0'));
    }
    return 0;
}

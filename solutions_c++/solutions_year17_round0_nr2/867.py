//#include <bits/stdc++.h>
#include <stdio.h>
#include <iostream>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <limits.h>
#include <algorithm>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <bitset>
#include <string>
#include <time.h>
using namespace std;
long double esp=1e-11;
//#pragma comment(linker, "/STACK:1024000000,1024000000")
#define fi first
#define se second
#define all(a) (a).begin(),(a).end()
#define cle(a) while(!a.empty())a.pop()
#define mem(p,c) memset(p,c,sizeof(p))
#define mp(A, B) make_pair(A, B)
#define pb push_back
#define lson l , m , rt << 1
#define rson m + 1 , r , rt << 1 | 1
typedef long long int LL;
const long double PI = acos((long double)-1);
const LL INF=0x3f3f3f3fll;
const int MOD =1000000007ll;
const int maxn=500100;
char s[100];
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    //::iterator iter;                  %I64d
    //for(int x=1;x<=n;x++)
    //for(int y=1;y<=n;y++)
    //scanf("%d",&a);
    //printf("%d\n",ans);
    int T;
    scanf("%d",&T);
    for(int gg=1;gg<=T;gg++)
    {
        s[0]='0';
        scanf("%s",s+1);
        LL n;
        sscanf(s,"%lld",&n);
        int la=s[0];
        int len=strlen(s);
        for(int x=1;x<len;x++)
        {
            if(la>s[x])
            {
                for(int y=x-1;y>=1;y--)
                    if(s[y]>s[y-1])
                {
                    s[y]--;
                    for(int z=y+1;z<len;z++)
                        s[z]='9';
                    break;
                }
                break;
            }
            la=s[x];
        }
        LL ans=0;
        sscanf(s,"%lld",&ans);
        printf("Case #%d: %lld\n",gg,ans);
    }
    return 0;
}

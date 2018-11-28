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
bitset<1001>q,zero,xo;
char s[1001];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    //::iterator iter;                  %I64d
    //for(int x=1;x<=n;x++)
    //for(int y=1;y<=n;y++)
    //scanf("%d",&a);
    //printf("%d\n",ans);
    int T;
    scanf("%d",&T);
    for(int gg=1;gg<=T;gg++)
    {
        int k;
        scanf("%s%d",s,&k);
        q=zero=xo=0;
        for(int x=0;x<k;x++)
            xo[x]=1;
        int n=strlen(s);
        for(int x=0;x<n;x++)
        {
            if(s[x]=='-')
                q[x]=1;
        }
        int ans=0;
        for(int x=0;x<=n-k;x++)
        if(q[x]==1)
        {
            q^=xo<<x;
            ans++;
        }
        if(q==zero)
            printf("Case #%d: %d\n",gg,ans);
        else
            printf("Case #%d: IMPOSSIBLE\n",gg);
    }
    return 0;
}

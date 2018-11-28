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
const LL INF=0x3f3f3f3f3f3f3f3fll;
const int MOD =1000000007ll;
const int maxn=1010;
int d[10],f[10]={1,3,2,6,4,5};
char ff[10]=" RYOBVG";
int ans[maxn];
int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    //::iterator iter;                  %I64d
    //for(int x=1;x<=n;x++)
    //for(int y=1;y<=n;y++)
    //scanf("%d",&a);
    //printf("%d\n",ans);
    int T;
    scanf("%d",&T);
    for(int gg=1;gg<=T;gg++)
    {
        int n;
        scanf("%d",&n);
        for(int x=0;x<=5;x++)
            scanf("%d",&d[f[x]]);           //for(int x=1;x<=6;x++)printf("%d ",d[x]);
        vector<pair<int,int> >q;
        q.clear();
        q.pb(mp(d[1],1));
        q.pb(mp(d[2],2));
        q.pb(mp(d[4],4));
        sort(q.rbegin(),q.rend());
        vector<int>t;
        t.clear();
        for(int x=0;x<=2;x++)
        {
            while(q[x].fi>0)
            {
                q[x].fi--;
                t.pb(q[x].se);
            }
        }
        int pos=0;
        for(int x=1;x<=n;x+=2)
            ans[x]=t[pos++];
        for(int x=2;x<=n;x+=2)
            ans[x]=t[pos++];
        int f=1;
        ans[0]=ans[n];
        for(int x=1;x<n;x++)
            if(ans[x-1]==ans[x]||ans[x+1]==ans[x])f=0;
        if(f==0)
            printf("Case #%d: IMPOSSIBLE\n",gg);
        else
        {
            printf("Case #%d: ",gg);
            for(int x=1;x<=n;x++)
                putchar(ff[ans[x]]);
            putchar('\n');
        }
    }
    return 0;
}

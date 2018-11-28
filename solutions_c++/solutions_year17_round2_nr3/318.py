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
const int maxn=105;
LL d[maxn][maxn],ho[maxn][2],pp[maxn][maxn];
double ans[maxn];
priority_queue<pair<double,int>, vector<pair<double,int> >, greater<pair<double,int> > > q;
int in[maxn];
int main()
{
    freopen("C-large.in", "r", stdin);;
    freopen("C-large.out", "w", stdout);
    //::iterator iter;                  %I64d
    //for(int x=1;x<=n;x++)
    //for(int y=1;y<=n;y++)
    //scanf("%d",&a);
    //printf("%d\n",ans);
    int T;
    scanf("%d",&T);
    for(int gg=1;gg<=T;gg++)
    {
        int n,qq;
        scanf("%d%d",&n,&qq);
        for(int x=1;x<=n;x++)
            scanf("%d%d",&ho[x][0],&ho[x][1]);
        for(int x=1;x<=n;x++)
            for(int y=1;y<=n;y++)
        {
            scanf("%lld",&d[x][y]);
            if(d[x][y]==-1)d[x][y]=INF;
            pp[x][y]=d[x][y];
        }
        for(int k=1; k<=n; k++)
            for(int i=1; i<=n; i++)
                for(int j=1; j<=n; j++)
                    if(pp[i][k]!=INF && pp[k][j]!=INF && pp[i][j]>pp[i][k]+pp[k][j])
                        pp[i][j]=pp[i][k]+pp[k][j];
//        for(int x=1;x<=n;x++)
//            for(int y=1;y<=n;y++)
//                printf("%lld%c",pp[x][y]," \n"[y==n]);
        printf("Case #%d:",gg);
        for(int g=1;g<=qq;g++)
        {
            int st,ed;
            scanf("%d%d",&st,&ed);
            for(int x=1;x<=n;x++)
                ans[x]=INF;
            ans[st]=0;
            mem(in,0);
            cle(q);
            q.push(mp(0,st));
            while(!q.empty())
            {
                int u=q.top().se;
                q.pop();
                if(in[u])continue;
                in[u]=1;
                for(int x=1;x<=n;x++)
                if(in[x]==0&&pp[u][x]!=INF&&pp[u][x]<=ho[u][0])
                {
                    if(ans[u]+pp[u][x]*1.0/ho[u][1]<ans[x])
                    {
                        ans[x]=ans[u]+pp[u][x]*1.0/ho[u][1];
                        q.push(mp(ans[x],x));
                    }
                }
            }
            printf(" %.6f",ans[ed]);
        }
        puts("");
    }
    return 0;
}

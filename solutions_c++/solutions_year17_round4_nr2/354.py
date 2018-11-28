#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <map>
#include <cstdlib>
#include <cmath>
#include <string>
#include <algorithm>
#include <set>
#include <stack>
#include <queue>
#include <utility>
#include <bitset>
#include <cassert>
#define fi first
#define se second
#define mkp make_pair
#define pb push_back
#define rep(i,a,b) for (int i=(a);i<(b);i++)
#define per(i,b,a) for (int i=(b)-1;i>=(a);i--)
#define REP(i,a,b) for (int i=(a);i<=(b);i++)
#define PER(i,b,a) for (int i=(b);i>=(a);i--)
using namespace std;
typedef long long LL;

const int INF = 0x3f3f3f3f;

const int MAXN = 1005; // 1e6;
int T,n,m,c,z;
vector <int> G[MAXN];
vector <int> P[MAXN];
int tmp[MAXN];
bool C(int x)
{
        rep(i,1,n+1) tmp[i] = P[i].size();
        int cnt = 0;
        for (int i = n; i >= 1; i--)
        {
                if (tmp[i] > x) z +=tmp[i]-x, cnt += tmp[i]-x;
                else cnt = max(0,cnt-(x-tmp[i]));
        }
        if (cnt > 0) return false;
        else return true;
}
int main()
{
        freopen("B-large.in","r",stdin);
        freopen("Large_B.txt","w",stdout);
        scanf("%d",&T);
        rep(cas,1,T+1)
        {
                scanf("%d%d%d",&n,&c,&m);
                rep(i,1,MAXN) G[i].clear();
                rep(i,1,MAXN) P[i].clear();
                rep(i,0,m)
                {
                        int p, c;
                        scanf("%d%d",&p,&c);
                        G[c].pb(p);
                        P[p].pb(c);
                }
                printf("Case #%d: ",cas);
                int l = 0 ,r = 10000;
                z=0;
                rep(i,1,c+1)
                {
                        l = max(l, int(G[i].size()));
                }
                l--;
                while (r-l>1)
                {
                        int m = l+r>>1;
                        if (C(m)) r=m;
                        else l = m;
//                        cout<<l<<" "<<m<<" "<<r<<endl;
                }
                z = 0;
                C(r);
                printf("%d %d\n",r,z);
        }
}

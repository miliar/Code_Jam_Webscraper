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
#define fi first
#define se second
#define rep(i,a,b) for (int i=(a);i<(b);i++)
#define per(i,a,b) for (int i=(b)-1;i>=(a);i--)
#define REP(i,a,b) for (int i=(a);i<=(b);i++)
#define PER(i,a,b) for (int i=(b);i>=(a);i--)
using namespace std;
typedef long long LL;
typedef pair<LL,LL> P;
typedef pair<double,double> PD;
const int INF = 0x3f3f3f3f;
const double PI = 3.1415926535898;
const int MAXN = 1000005; // 1e6;
int n,k,T;
LL r[MAXN],h[MAXN];
P pan[MAXN];
P g[MAXN];
int main()
{
	freopen("A-large.in-2.txt","r",stdin);
	freopen("out_Large.txt","w",stdout);
	scanf("%d",&T);
	rep(cas,1,T+1)
	{
		LL ans = 0;
		printf("Case #%d: ",cas);
		scanf("%d%d",&n,&k);
		rep(i,0,n) scanf("%lld%lld",&r[i],&h[i]);
		rep(i,0,n) {
			g[i].se =r[i]*r[i];
			g[i].fi = 2*r[i]*h[i];
			// cout<<">>"<<g[i].fi<<" "<<g[i].se<<endl;
		}
		sort(g,g+n);
		per(i,0,n)
		{
			LL tmp = g[i].fi + g[i].se;
			int cnt = 1;
			// cout<<">>"<<tmp<<endl;
			per(j,0,n)
			{
				if (i == j) continue;
				// cout<<"---"<<g[j].fi<<" "<<g[j].se<<endl;
				if (cnt == k) break;
				if (g[j].se <= g[i].se) cnt ++, tmp += g[j].fi;
				if (cnt == k) break;
			}
			// cout<<tmp<<endl;
			// cout<<PI*tmp<<endl;
			if (cnt == k) ans = max(ans,tmp);
		}
		printf("%.8f\n", PI*ans);
	}	



}


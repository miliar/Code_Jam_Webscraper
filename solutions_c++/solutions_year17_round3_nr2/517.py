#include <cassert>
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
#define mkp make_pair
#define pb push_back
#define rep(i,a,b) for (int i=(a);i<(b);i++)
#define per(i,a,b) for (int i=(b)-1;i>=(a);i--)
#define REP(i,a,b) for (int i=(a);i<=(b);i++)
#define PER(i,a,b) for (int i=(b);i>=(a);i--)
using namespace std;
typedef long long LL;
typedef pair<int,int> P;
const int INF = 0x3f3f3f3f;

const int MAXN = 1000005; // 1e6;
const int TT = 24*60;
int n,Ac,Aj;
int CASE;
int c[MAXN],d[MAXN],j[MAXN],k[MAXN];
int leftc,leftj;
int t[MAXN];
int main()
{
	// freopen("in.txt","r",stdin);
	freopen("B-large.in-2.txt","r",stdin);
	freopen("Large_out_B.txt","w",stdout);
	scanf("%d",&CASE);
	rep(cas,1,CASE+1)
	{
		scanf("%d%d",&Ac,&Aj);
		rep(i,0,Ac) scanf("%d%d",c+i,d+i);
		rep(i,0,Aj) scanf("%d%d",j+i,k+i);
		leftc =leftj= TT/2;
		int ans = 0;
		vector<P> all;
		rep(i,0,Ac)
		{
			// if (c[i] == d[i]) continue;
			all.pb(mkp(c[i],d[i]));
			leftj -= d[i]-c[i];
			rep(v,c[i],d[i]) t[v]=2;
		}
		rep(i,0,Aj)
		{
			// if (j[i] == k[i]) continue;
			all.pb(mkp(j[i],k[i]));
			leftc -= k[i]-j[i];
			rep(v,j[i],k[i]) t[v]=1;
		}
		sort(all.begin(),all.end());
		priority_queue<int, vector<int>,greater<int> > C,J;
		rep(i,0,all.size())
		{
			if (i > 0 && t[all[i].fi] == t[all[i-1].fi] && t[all[i].fi] == 1) C.push(all[i].fi - all[i-1].se);
			if (i > 0 && t[all[i].fi] == t[all[i-1].fi] && t[all[i].fi] == 2) J.push(all[i].fi - all[i-1].se);
			if (i > 0 && t[all[i].fi] != t[all[i-1].fi]) ans++;
		}
		if (t[all[0].fi] == t[all[all.size()-1].fi] && t[all[0].fi] == 1) C.push(all[0].fi + TT - all[all.size()-1].se);
		if (t[all[0].fi] == t[all[all.size()-1].fi] && t[all[0].fi] == 2) J.push(all[0].fi + TT - all[all.size()-1].se);
		if (t[all[0].fi] != t[all[all.size()-1].fi] && t[all[0].fi] ) ans++;
		// cout<<">>"<<ans<<endl;
		int debug = 5;
		while(!C.empty()) 
		{
			int p = C.top();
			C.pop();
			// if (cas == debug)
			// cout<<"c "<<leftc<<" "<<p<<endl;
			if (p <= leftc) leftc -= p;
			else ans += 2;
		}
		while(!J.empty())
		{
			// cout<<"j "<<leftj<<endl;
			int p = J.top();
			J.pop();
			// if (cas ==debug)
			// cout<<"j "<<leftj<<" "<<p<<endl;
			if (p <= leftj) leftj -= p;
			else ans+=2;
		}
		
		// assert(a)
		// if (cas == debug) 
		// {
		// 	cout<<Ac<<" "<<Aj<<endl;
		// 	rep(i,0,Ac) cout<<c[i]<<" "<<d[i]<<endl;
		// 	rep(i,0,Aj) cout<<j[i]<<" "<<k[i]<<endl;
		// 	printf("Case #%d: %d\n",cas,ans);
		// }
		printf("Case #%d: %d\n",cas,ans);
	}


}


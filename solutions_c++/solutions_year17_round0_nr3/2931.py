#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<string>
#include<cstring>
#include<cstdio>
#include<ctime>
#include<climits>
#include<complex>
#include<cassert>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define sz(x) (int)((x).size())
#define all(x) x.begin(),x.end()
#define clr(x) memset((x),0,sizeof(x))
#define cdp(x) memset((x),-1,sizeof(x))
#define rep(i,n) for (i=0;i<n;i++)
#define Rep(i,a,b) for (i=a;i<=b;i++)
#define ff(i,x) for (i=start[x];i!=-1;i=a[i].next)
#define foreach(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)
using namespace std;
const double eps=1e-8;
const double pi=acos(-1.0);
int dblcmp(double d){if (fabs(d)<eps)return 0;return d>eps?1:-1;}
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<pii> vpi;
set<ll>s;
void dfs(ll n)
{
	if (!n)return;
	if (s.find(n)!=s.end())return;
	s.insert(n);
	if (n==1)return;
	dfs(n/2);
	if (n%2==0)dfs(n/2-1);
}
int main()
{
	freopen("C:\\competition\\gcj\\C-large (2).in","r",stdin);
	freopen("C:\\competition\\gcj\\Cout.out","w",stdout);
	int i,j,k,cas,cc=0;
	scanf("%d",&cas);
	while (cas--)
	{
		ll n,d,ans;
		cin>>n>>d;
		dfs(n);
		vl v(all(s));
		reverse(all(v));
		map<ll,ll>c;
		c[n]=1;
		foreach(e,v)
		{
			ll t=*e;
			if (t%2==1)
			{
				if (t/2)c[t/2]+=2*c[t];
			}
			else 
			{
				if (t/2)c[t/2]+=c[t];
				if (t/2-1)c[t/2-1]+=c[t];
			}
		}
		vector<pair<ll,ll> >p;
		foreach(e,c)
		{
			p.pb(mp(e->fi,e->se));
		}
		reverse(all(p));
		foreach(e,p)
		{
			if (d<=e->se)
			{
				ans=e->fi;
				break;
			}
			d-=e->se;
		}
		if (ans%2==0)cout<<"Case #"<<++cc<<": "<<ans/2<<" "<<ans/2-1<<endl;
		else cout<<"Case #"<<++cc<<": "<<ans/2<<" "<<ans/2<<endl;
	}
	return 0;
}
	
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
ll n;
int a[33],d;
ll dp[33][2][12],ten[20];
ll getdp(int p,int ls,int lt)
{
	int u,i;
	if (p==d)return 0;
	if (dp[p][ls][lt]!=-1)return dp[p][ls][lt];
	if (ls==0)u=a[p];
	else u=9;
	ll ans=-2;
	for (i=lt;i<=u;i++)
	{
		int nls;
		if (ls==0&&i==a[p])nls=0;
		else nls=1;
		ll c=getdp(p+1,nls,i);
		if (c==-2)continue;
		ans=max(ans,(ll)i*ten[d-p-1]+c);
	}
	return dp[p][ls][lt]=ans;
}
ll get(ll t)
{
	d=0;
	while (t)
	{
		a[d++]=t%10;
		t/=10;
	}
	reverse(a,a+d);
	cdp(dp);
	return getdp(0,0,0);
}
int main()
{
	freopen("C:\\competition\\gcj\\B-large (5).in","r",stdin);
	freopen("C:\\competition\\gcj\\Bout.out","w",stdout);
	int i,j,k,cas,cc=0;
	ten[0]=1;
	for (i=1;i<20;i++)ten[i]=10*ten[i-1];
	cin>>cas;
	while (cas--)
	{
		cin>>n;
		cout<<"Case #"<<++cc<<": "<<get(n)<<endl;
	}
	return 0;
}
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
ll r[1111],h[1111];
int n,d;
int main()
{
	freopen("C:\\competition\\gcj\\A-large (5).in","r",stdin);
	freopen("C:\\competition\\gcj\\Aout.txt","w",stdout);
	int i,j,k,cas,cc=0;
	scanf("%d",&cas);
	while (cas--)
	{
		scanf("%d%d",&n,&d);
		for (i=0;i<n;i++)
		{
			int x,y;
			scanf("%d%d",&x,&y);
			r[i]=x;
			h[i]=y;
		}
		double ans=0;
		for (i=0;i<n;i++)
		{
			vector<double>v;
			for (j=0;j<n;j++)
			{
				if (r[j]<=r[i]&&j!=i)
				{
					double sd=2*pi*1.0*r[j]*1.0*h[j];
					v.pb(sd);
				}
			}
			if (sz(v)<d-1)continue;
			sort(all(v));
			reverse(all(v));
			double tot=0;
			for (k=0;k<d-1;k++)
			{
				tot+=v[k];
			}
			double rr=r[i];
			tot+=pi*rr*rr+2*pi*rr*1.0*h[i];
			ans=max(ans,tot);
		}	
		printf("Case #%d: %.10lf\n",++cc,ans);	
	}
	return 0;
}
	
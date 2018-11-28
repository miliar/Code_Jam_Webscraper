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
int n,d;
double u,p[1111];
void gao1(double *pp,double x)
{
	int i;
	double c=x;
	for (i=n-1;i>=0;i--)
	{
		if (pp[i]+c>=1.0)
		{
			c-=(1.0-pp[i]);
			pp[i]=1.0;
		}
		if (c<=0.0)break;
	}
}
double gao2(double*pp,double x,int st)
{
	double c=x;
	int i,j;
	for (i=st;i<n;i++)
	{
		double d;
		if (i+1<n)d=pp[i+1]-pp[i];
		else d=1-pp[i];
		double add=min(d,c/(i-st+1.0));
		for (j=st;j<i+1;j++)
		{
			pp[j]+=add;
			c-=add;
		}
		if (c<=0)break;
	}
}
double dp[111][111];
double calc(double*pp,int st)
{
	clr(dp);
	dp[0][0]=1.0;
	int i,k;
	for (k=0;k<=n;k++)
	{
		for (i=1;i<=n;i++)
		{
			double pc=0;
			pc+=dp[k][i-1]*(1.0-pp[i-1]);
			if (k>0)pc+=dp[k-1][i-1]*pp[i-1];
 			dp[k][i]=pc;
		}
	}
	double res=0;
	for (i=st;i<=n;i++)res+=dp[i][n];
	return res;
}
double get_sum(double *p)
{
	double sum=0;
	for (int i=0;i<n;i++)sum+=p[i];
	return sum;
}
double gao()
{
	int i,j,k;
	double ans=0;
  	for (int it=0;it<2;it++)
  	{
  		double pp[111];
  		for (i=0;i<n;i++)pp[i]=p[i];
  		sort(pp,pp+n);
  		double x=u;
  		if (it)
  		{
  			gao1(pp,x);
  			x=get_sum(p)-get_sum(pp)+u;
  		}
  		for (j=0;j<n;j++)
  		{
  			double t[111];
  			for (k=0;k<n;k++)t[k]=pp[k];
  			gao2(t,x,j);
  			ans=max(ans,calc(t,d));
  		}	
  	}	
  	return ans;
}
int main()
{
	freopen("C:\\competition\\gcj\\C-small-2-attempt0 (1).in","r",stdin);
	freopen("C:\\competition\\gcj\\Cout.txt","w",stdout);
	int i,j,k,cas,cc=0;
	scanf("%d",&cas);
	while (cas--)
	{
		scanf("%d%d%lf",&n,&d,&u);
		for (i=0;i<n;i++)scanf("%lf",p+i);
		double ans=gao();
		printf("Case #%d: %.10lf\n",++cc,ans);	
	}
	return 0;
}
	
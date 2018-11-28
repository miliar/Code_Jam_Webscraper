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

const int INF = 0x3f3f3f3f;

const int MAXN = 1000005; // 1e6;
int n,k;
double U;
double p[MAXN];
int CASE;
int C(double x)
{
	double tmp = U;
	rep(i,0,n)
	{
		if (p[i]<x)  tmp -= x-p[i];
	}
	if (tmp < 0) return 0;
	else return 1;
}
int main()
{
	// freopen("in.txt","r",stdin);
	freopen("C-small-1-attempt1.in.txt","r",stdin);
	freopen("C_small1_out.txt","w",stdout);
	scanf("%d",&CASE) ;
	rep(cas,1,CASE+1)
	{
		scanf("%d%d",&n,&k);
		scanf("%lf",&U);
		rep(i,0,n) scanf("%lf",&p[i]);
		double l = 0.0,r = 1.1;
		rep(qqq,0,100)
		{
			double m = (l+r)/2.0;
			if (C(m)) l = m;
			else r = m;
		}

		double ans = 1;
		rep(i,0,n)
		{
			if (p[i] > l) ans *=p[i];
			else ans*=l;
			// ans *=q;
		}
		printf("Case #%d: %.8f\n",cas,ans);


	}

}


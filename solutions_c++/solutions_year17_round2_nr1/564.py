#include <bits/stdc++.h>
#define si(n) scanf("%d",&n);
#define pi(n) printf("%d\n",n);
#define pl(n) printf("%lld\n",n);
#define sl(n) scanf("%lld",&n);
#define sd(n) scanf("%lf",&n);
#define pd(n) printf("%lf\n",n);
#define ss(s) scanf("%s",s);
#define ps(s) printf("%s\n",s);
#define pb push_back
#define ll long long int
#define maxn 1000001
#define sqrtn 317
#define maxm 51
#define minv(a,b,c) min(a,min(b,c))
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pli pair<ll,int>
#define eps 1e-9
#define mod 1000000007
#define psi pair < string,ll>
#define mp make_pair
#define BLOCK 450
using namespace std;

int main()
{
	int t;
	si(t);
	for(int i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		double d;
		int n;
		sd(d);si(n);
		double time=0;
		for(int i=1;i<=n;i++)
		{
			double k,s;
			sd(k);sd(s);
			double temp=(d-k)/s;
			time=max(time,temp);
		}
		double ans=d/time;
		pd(ans);
	}

}
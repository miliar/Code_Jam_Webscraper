#include <bits/stdc++.h>
using namespace std;

#define sd(x) 		scanf("%d",&x)
#define su(x) 		scanf("%u",&x)
#define slld(x) 	scanf("%lld",&x)
#define sc(x) 		scanf("%c",&x)
#define ss(x) 		scanf("%s",x)
#define sf(x) 		scanf("%f",&x)
#define slf(x)		scanf("%lf",&x)
#define ll 			long long int
#define mod(x,n) 	(x+n)%n
#define pb          push_back
#define mp          make_pair
#define pii         pair<int,int>
#define vi          vector<int>
#define all(a)      (a).begin(),(a).end()
#define F           first
#define S           second
#define sz(x)       (int)x.size()
#define Mod         1000000007

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);

	int i,j,k,l,m,n,x,y,z,a,b,r,tno,t,d,s;
	double time,timeMax;
	// ll i,j,k,l,m,n,x,y,z,a,b,r;

	sd(t);	tno = 1;
	while(tno<=t)
	{
		timeMax = 0;
		sd(d);	sd(n);

		for(i=0;i<n;i++)
		{
			sd(k);	sd(s);

			time = (double)(d-k)/(double)(s);
			timeMax = max(time,timeMax);
		}

		printf("Case #%d: %0.8lf\n", tno, (double)d/timeMax );

		tno++;
	}
	
	return 0;
}
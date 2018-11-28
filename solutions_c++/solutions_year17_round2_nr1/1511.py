#include <bits/stdc++.h>

using namespace std;

#define ll long long int
#define sd(x) scanf("%d",&x)
#define sc(x) scanf("%c",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
#define mod 1000000007
#define pb push_back
#define vint vector<int>

int main()
{
	freopen("input.txt" , "r", stdin);
	freopen("output.txt", "w", stdout);
	ll t,d,n,x,minPos,i,j,k,l;
	double ans,z,timeTaken,y,sp,pos;
	slld(t);
	for(x=1;x<=t;x++){
		slld(d);slld(n);
		y=0;
		for(i=0;i<n;i++){
			scanf("%lf",&pos);
			scanf("%lf",&sp);
			y = max(y,(d-pos)/sp);
		}
		ans = d/y;
		printf("Case #%lld: %0.10lf\n",x,ans);
	}
	return 0;
}
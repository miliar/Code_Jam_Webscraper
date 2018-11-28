#include<bits/stdc++.h>
using namespace std;
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
#define mod 1000000007
#define bitcount __builtin_popcountll
#define ll long long
#define pb push_back
#define pi pair<int,int>
#define pii pair<pi,int>
#define mp make_pair
#define F first
#define S second
struct compare
{
	bool operator()(pi x, pi y)
	{
		if(x.S-x.F==y.S-y.F)
			return x.F>y.F;
		return x.S-x.F<y.S-y.F;
	}
};
int main()
{
	int i,j,k,n;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	sd(t);
	for(int x=1;x<=t;x++)
	{
		sd(n);
		sd(k);
		priority_queue<pi, vector<pi>,compare>pq;
		pq.push(mp(1,n+2));
		int val1,val2;
		while(k--)
		{
			pi z=pq.top();
			int mid=(z.F+z.S)/2;
			if(z.S-mid!=1)
				pq.push(mp(mid,z.S));
			if(mid-z.F!=1)
				pq.push(mp(z.F,mid));
			val1=mid-z.F;
			val2=z.S-mid;
			pq.pop();
		}
		printf("Case #%d: %d %d\n",x,val2-1,val1-1 );
	}
	return 0;
}
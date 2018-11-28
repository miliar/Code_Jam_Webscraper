#include <bits/stdc++.h>
#define ll long long int
#define fio ios_base::sync_with_stdio(0);cin.tie(0)
#define sd(t) scanf("%d",&t)
#define pd(t) printf("%d\n",t)
#define slld(t) scanf("%lld",&t)
#define plld(t) printf("%lld\n",t)
#define sc(t) scanf("%c",&t)
#define pb(x) push_back(x)
#define ii pair<int,int>
#define vi vector<int>
#define vvi vector<vi >
#define vii vector<ii >
#define vvii vector<vii >
#define clr(x) memset(x,0,sizeof(x))
#define rep(i,begin,end) for(__typeof(end) i=begin-(begin>end);i!=end-(begin>end);i+=1-2*(begin>end))
#define M_PI 3.14159265358979323846
#define MOD 1000000007
#define INF 101010101
#define MAX 100005
#define EPS 1e-12
using namespace std;

ll POW(ll b, ll p)
{
	if(p==0) return 1;
	if(p==1) return b;

	ll x = POW(b,p/2);
	x *= x;
	if(p%2) x *= b;
	return x;
}

int main()
{
	int t; sd(t);
	rep(z,1,t+1)
	{
		ll n,k; slld(n); slld(k);

		ll log = log2(k);
		ll p1 = POW(2ll,log+1);
		ll p2 = POW(2ll,log);

		ll minn = (n - k) / p1;
		ll maxx = (n - k + p2) / p1;

		if(minn > maxx) swap(minn, maxx);
		printf("Case #%d: %lld %lld\n", z, maxx, minn);
	}
	return 0;
}

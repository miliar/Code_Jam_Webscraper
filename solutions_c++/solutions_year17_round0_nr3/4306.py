#include <bits/stdc++.h>
#define ff first
#define ss second
#define pb push_back
#define MOD (1000000007LL)
#define LEFT(n) (2*(n))
#define RIGHT(n) (2*(n)+1)
 
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;
 
ll pwr(ll base, ll p, ll mod = MOD){
ll ans = 1;while(p){if(p&1)ans=(ans*base)%mod;base=(base*base)%mod;p/=2;}return ans;
}
 
ll gcd(ll a, ll b){
    if(b == 0)  return a;
    return gcd(b, a%b);
}

typedef vector<double> VD;
typedef vector<VD> VVD;
typedef vector<int> VI;

int t;
ll n,k;
ll a[2],b[2],c[2],d[2];
ll power[65];

set<int> curr, prev, next;

map<ll, ll>cnt;

void cal()
{
	set<ll, greater<ll> > newx;
	set<ll, greater<ll> > :: iterator ii;
	if(a[0] > 0)
	{
		newx.insert(a[0]/2);
		cnt[a[0]/2] += cnt[a[0]];
		newx.insert((a[0]-1)/2);
		cnt[(a[0]-1)/2] += cnt[a[0]];
	}
	if(a[1] > 0)
	{
		newx.insert(a[1]/2);
		cnt[a[1]/2] += cnt[a[1]];
		newx.insert((a[1]-1)/2);
		cnt[(a[1]-1)/2] += cnt[a[1]];
	}

	int i = 0;
	for(ii = newx.begin(); ii != newx.end(); ii++)
	{
		a[i] = *ii;
		i++;
	}
	if(i == 1)
		a[1] = 0;


}
int main()
{
	scanf("%d",&t);
	power[0] = 1;
	for(int i=1;i<64;i++)
		power[i] = 2L*power[i-1];

	for(int z=1;z<=t;z++)
	{
		cnt.clear();
		scanf("%lld %lld",&n,&k);
		int level = 0;
		for(int i=1;i<64;i++)
			if(k < power[i])
			{
				level = i;
				break;
			}

		a[0] = n;
		a[1] = 0;
		cnt[n] = 1;
		for(int i=1;i<level;i++)
			cal();

		// cout<<a[0]<<" "<<cnt[a[0]]<<"\n";
		// cout<<a[1]<<" "<<cnt[a[1]]<<"\n";

		ll rem = k - power[level-1] + 1;
		if(cnt[a[0]] >= rem)
			printf("Case #%d: %lld %lld\n",z,a[0]/2,(a[0]-1)/2);
		else
			printf("Case #%d: %lld %lld\n",z,a[1]/2,(a[1]-1)/2);

	}
	return 0;
}
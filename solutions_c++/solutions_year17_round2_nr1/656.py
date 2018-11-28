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

int t,n;
double d,u,v;
double ti;
int cnt = 1;
int main()
{
	scanf("%d",&t);
	while(t--)
	{
		scanf("%lf %d",&d,&n);
		ti = 0;
		for(int i=0;i<n;i++)
		{
			scanf("%lf %lf",&u,&v);
			ti = max(ti,(d-u)/v);
		}
		printf("Case #%d: %0.9lf\n",cnt,d/ti);
		cnt++;
	}
	return 0;
}
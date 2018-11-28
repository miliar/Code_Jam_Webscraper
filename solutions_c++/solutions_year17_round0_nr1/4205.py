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

string s;
int t,k,n,ans;
int a[1005];
int main()
{
	cin>>t;
	for(int z=1;z<=t;z++)
	{
		cin>>s>>k;
		int n = s.length();
		for(int i=0;i<n;i++)
		{
			if(s[i] == '-')
				a[i] = 0;
			else
				a[i] = 1;
		}

		ans = 0;
		for(int i=0;i<n-k+1;i++)
		{
			if(a[i] == 0)
			{
				for(int j=i;j<i+k;j++)
					a[j] = a[j]^1;
				ans++;
			}
		}

		for(int i=0;i<n;i++)
			if(a[i] == 0)
			{
				ans = -1;
			}

		if(ans == -1)
			cout<<"Case #"<<z<<": IMPOSSIBLE\n";
		else
			cout<<"Case #"<<z<<": "<<ans<<"\n";

	}
	return 0;
}
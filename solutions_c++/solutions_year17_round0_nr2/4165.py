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

int t,n;
string s;
int a[20];
int main()
{
	cin>>t;
	for(int z=1;z<=t;z++)
	{
		cin>>s;
		n = s.length();

		for(int i=0;i<n;i++)
			a[i] = (int)s[i]-'0';

		int f = 1;
		for(int i=1;i<n;i++)
			if(a[i] < a[i-1])
				f = 0;

		if(f)
			cout<<"Case #"<<z<<": "<<s<<"\n";
		else
		{
			int change = -1;
			for(int i=n-2;i>0;i--)
				if(a[i] > a[i-1])
				{
					change = i;
					break;
				}

			if(change == -1)
				change = 0;

			a[change]--;
			for(int i=change+1;i<n;i++)
				a[i] = 9;

			int start = 0;
			for(int i=0;i<n;i++)
				if(a[i] != 0)
				{
					start = i;
					break;
				}

			cout<<"Case #"<<z<<": ";
			for(int i=start;i<n;i++)
				cout<<a[i];
			cout<<"\n";

		}
	}
	return 0;
}
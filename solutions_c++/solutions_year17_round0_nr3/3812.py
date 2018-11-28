#include<bits/stdc++.h>

#define ssync ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0)
#define F first
#define S second
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;
typedef vector<ll> vll;
typedef vector<vll> vvl;
typedef pair<int,int> pii;
typedef pair<int,ll> pil;
typedef pair<ll,ll> pll;
const ll MOD = 1e9+7;
const long double PI = 3.14159265;

ll powerWithMod(ll base, ll exponent, ll modulus = LLONG_MAX)
{
	ll result = 1;
	base %= modulus;
	while(exponent > 0)
	{
		if(exponent % 2 == 1)
			result = (result * base) % modulus;
		exponent >>= 1;
		base = (base * base) % modulus;
	}
	return result;
}

ll modInverse(ll a, ll m = MOD)
{
	return powerWithMod(a, m-2, m);
}

int t, n, k;


int main()
{
	ssync;
	cin >> t;
	for(int cas=1; cas<=t; cas++)
	{
		cin >> n >> k;
		if(k > 3*n/5)
		{
			cout << "Case #" << cas << ": 0 0\n";
			continue;
		}
		set<vi> a;
		a.insert(vi({n,0,n+1}));
		while(a.size() < k)
		{
			auto it = (--a.end());
			vi temp(*it);
			a.erase(it);
			vi a1(3,0), a2(3,0);
			
			a1[0] = (temp[0]-1)/2;
			a1[1] = temp[1];
			a1[2] = a1[0] + a1[1] + 1;

			a2[0] = temp[0]/2;
			a2[2] = temp[2];
			a2[1] = a2[2] - a2[0] - 1;

			a.insert(a1);
			a.insert(a2);
		}
		int ans = (*(--a.end()))[0];
		cout << "Case #" << cas << ": " << ans/2 << " " << (ans-1)/2 << "\n";
	}
	return 0;
}
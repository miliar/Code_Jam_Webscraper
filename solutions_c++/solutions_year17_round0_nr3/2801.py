#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
#define eb emplace_back
#define e1 first
#define e2 second
#define OUT(x) {cout << x; exit(0); }
#define scanf(...) scanf(__VA_ARGS__)?:0
#define boost {ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0); }
#define FOR(i, a, b) for(int i=(a); i<=(b); ++i)
typedef long long int ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef long double ld;
typedef pair <int, int> PII;
typedef pair <PII, int> PPI;
typedef pair <ll, ll> PLL;
typedef pair <PII, PII> PP;
const int mod = 1e9+7;
const int inf = 1e9+9;
const int MOD = 1e9+696969;
const ll INF = (ll)1e18 + 3;
ll N, K;
int T;
map <ll, ll> DP;
ll KK;
inline ll getDP(ll n)
{
	if (DP[n] != NULL) return DP[n];
	if (n <= KK)
	{
		DP[n] = 0;
		return 0;
	}
	
	ll value = 0;
	if (n % 2 == 1)
	{
		value = 2LL * getDP(n / 2) + 1LL;
		DP[n] = value;
		return value;
	}
	
	value = 1 + getDP(n/2) + getDP((n/2)-1);
	DP[n] = value;
	return value;
}
inline void podziel(ll n, ll k)
{
	DP.clear();
	KK = k;
	getDP(n);
}

int main()
{
	boost;
	cin >> T;
	FOR(z, 1, T)
	{
		cin >> N >> K;
		--K;
		ll x = 1, y = N;
		while (x < y)
		{
			ll sr = (x + y) / 2;
			podziel(N, sr);
			if (DP[N] > K) x = ++sr;
			else y = sr;
		}
		
		cout << "Case #" << z << ": " << x/2 << ' ' << (x - 1)/2 << endl;
	}
}

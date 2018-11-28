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
const ll INF = 4e18 + 3;
int n, k, T,t[1010];
string s;
int main()
{
	boost;
	cin >> T;
	FOR(z, 1, T)
	{
		cin >> s >> k;
		n = s.length();
		int res = 0, dasie = 1;
		for (int i=0; i<n; ++i)
			if (s[i] == '+') t[i + 1] = 1;
			else t[i + 1] = 0;
		FOR(i, 1, n)
		if (!t[i])
		{
			++res;
			if (i + k - 1 > n) dasie = 0;
			for (int j=1; j<=k; ++j) t[i+j-1] ^= 1;
		}
		cout << "Case #" << z << ": ";
		if (!dasie) cout << "IMPOSSIBLE\n";
		else cout << res << "\n";
		
	}
}

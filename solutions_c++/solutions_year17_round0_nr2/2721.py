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
int n, k, T,t[1010], LAST[1010];
string s;

string rem(int pozycja)
{
	string ret = "";
	if (t[pozycja] == 1) {
		FOR(i, 2, n) ret += '9';
		return ret;
	}
	t[pozycja]--;
	FOR(i, pozycja+1, n) t[i] = 9;
	FOR(i, 1, n) ret += (char)(t[i] + '0');
}

int main()
{
	boost;
	cin >> T;
	FOR(z, 1, T)
	{
		cin >> s;
		n = s.length();
		FOR(i, 1, n) t[i] = s[i-1] - '0';
		
		LAST[0] = 0; LAST[1] = 1;
		FOR(i, 2, n)
			if (t[i] == t[i-1]) LAST[i] = LAST[i-1];
			else LAST[i] = i;
		
		int swp = -1;
		FOR(i, 1, n-1)
		{
			if (t[i] > t[i+1]) {swp = i; break; }
		}
		
		string output = "";
		if (swp == -1) cout << "Case #" << z << ": " << s << endl;
		else
		{
			int poss = LAST[swp];
			output = rem(poss);
			cout << "Case #" << z << ": " << output << endl;
		}
		
	}
}

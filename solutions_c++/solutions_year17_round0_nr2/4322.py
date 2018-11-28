#include <bits/stdc++.h>
using namespace std;
#define FOR(i, n) for(int i = 0; i < (n); i++)
#define MEM(a, x) memset(a, x, sizeof(a))
#define ALL(a) a.begin(), a.end()
#define UNIQUE(a) a.erase(unique(ALL(a)), a.end())
typedef long long ll;

int t;

ll solve(ll x) {
	string s = to_string(x);
	char last = s[s.size()-1];
	for (int i = s.size()-1; i >= 0; i--) {
		if (s[i] > last) {
			for(int j = i+1; j < s.size(); j++) s[j] = '9';
			s[i] = to_string(s[i]-'1')[0];
		}
		last = s[i];
	}
	return stoll(s);
}

int main(int argc, char const *argv[]) {
	ios_base::sync_with_stdio(false);
	cin >> t;
	vector<ll> v(t);
	FOR(i, t) {
		ll n;
		cin >> n;
		v[i] = solve(n);
	}
	FOR(i, t) {
		cout << "Case #" << i+1 << ": " << v[i] << endl;
	}
	return 0;
}
#include <bits/stdc++.h>

#define pii pair <int, int>
#define pll pair <ll, ll>
#define rep(i, n) for (long long i = 0; i < (long long)n; i++)
#define REP(i, n, m) for (long long i = (long long)n; i < (long long)m; i++)
#define prep(i, n) for (long long i = 1; i <= (long long)n; i++)
#define per(i, n) for (long long i = n; i >= 0; i--)
#define pb push_back
#define vi vector <int>
#define vl vector <ll>
#define vvi vector <vector <int> >
#define vvl vector <vector <ll> >
#define fi first
#define se second
#define mp make_pair


typedef long long ll;
typedef long double ld;

using namespace std;

ifstream fin("B-large.in");
ofstream fout("ans.txt");

int main() {
	int t;
	fin >> t;
	rep (i, t) {
		fout << "Case #" << i + 1 << ": ";
		ll n;
		fin >> n;
		vi a;
		while (n > 0) {
			a.pb(n % 10);
			n /= 10;
		}
		vi ans;
		ans.pb(a[0]);
		for (int i = 1; i < a.size(); ++i) {
			if (a[i] > a[i - 1]) {
				a[i]--;
				ans.pb(a[i]);
				for (int j = 0; j < i; ++j) {
					ans[j] = 9;
				}
			} else {
				ans.pb(a[i]);
			}
		}
		bool b = true;
		rep (i, ans.size()) {
			if (ans[i] < 0) {
				fout << 0 << endl;
				b = false;
			}
		}
		if (b) {
			reverse(ans.begin(), ans.end());
			int j = 0;
			while (j < ans.size() && ans[j] == 0) {
				j++;
			}
			if (j == ans.size()) {
				fout << 0;
			} else {
				for (; j < ans.size(); ++j) {
					fout << ans[j];
				}
			}
			fout << endl;
		}
	}
	return 0;
}


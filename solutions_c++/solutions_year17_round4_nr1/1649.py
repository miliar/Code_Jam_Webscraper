#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vi> vvi;
typedef pair<int, int> pii;
typedef vector<pii> vii;
typedef vector<bool> vb;
typedef vector<string> vs;
const int di[] = { -1,0,1,0 };
const int dj[] = { 0,1,0,-1 };
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
#define mp make_pair

int n, p;
vi g;

int main() {
	ios::sync_with_stdio(false), cin.tie(0);
	ifstream cin("A-small-attempt1.in");
	ofstream cout("output.txt");
	int t, tt = 0; cin >> t;
	while (t--) {
		cin >> n >> p;
		g.resize(n);
		for (int i = 0; i < n; i++)
			cin >> g[i];
		cout << "Case #" << ++tt << ": ";
		if (p == 2) {
			int even = 0, odd = 0;
			for (int i = 0; i < g.size(); i++)
				if (g[i] % 2 == 0) even++;
				else odd++;
				cout << even + ceil(odd / 2.0) << endl;
		}

		else if (p == 3) {
			int m1 = 0, m2 = 0, r = 0;
			for (int i = 0; i < g.size(); i++) {
				if (g[i] % 3 == 0) r++;
				else if (g[i] % 3 == 1) m1++;
				else m2++;
			}
			int mn = min(m1, m2);
			r += mn;
			m1 -= mn, m2 -= mn;
			if (m2)
				r += ceil(m2 / 3.0);
			else
				r += ceil(m1 / 3.0);
			cout << r << endl;
		}

		else if (p == 4) {
			int m1 = 0, m2 = 0, m3 = 0, r = 0;
			for (int i = 0; i < g.size(); i++) {
				if (g[i] % 4 == 0) r++;
				else if (g[i] % 4 == 1) m1++;
				else if (g[i] % 4 == 2) m2++;
				else m3++;
			}
			int mn = min(m1, m3);
			r += mn;
			m1 -= mn, m3 -= mn;
			r += m2 / 2, m2 %= 2;
			if (m2) {
				if (m3 == 1) m3 = 0;
				else if (m3 > 1) m3 -= 2;
				if (m1 == 1) m1 = 0;
				else if (m1 > 1) m1 -= 2;
				m2 = 0;
			}
			if (m1)
				r += ceil(m1 / 4.0);
			else
				r += ceil(m3 / 4.0);
			cout << r << endl;
		}
	}
	//cin.ignore(), cin.get();
}

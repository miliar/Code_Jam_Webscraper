#include <cinttypes>
#include <inttypes.h>
#include <numeric>
#include <vector>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <map>
#include <utility>
#include <cmath>
#include <algorithm>
#include <set>
#include <stack>
#include <string.h>
#include <list>
#include <queue>
#include <bitset>
#include <functional>

#define vi vector<int>
#define vvi vector<vi>
#define pii pair<int,int>
#define vpii vector<pii>
#define ll long long

#define all(s) s.begin(), s.end()

using namespace std;

int nxi() { int a; cin >> a; return a; }

vector<ll> a;
void inc(int i, ll v) {
	for (; i < a.size(); i |= i + 1) {
		a[i] = max(a[i], v);
	}
}

long long get(int r) {
	long long ans = 0;
	for (; r >= 0; r = (r & (r + 1)) - 1) {
		ans = max(ans, a[r]);
	}
	return ans;
}

long long get(int l, int r) {
	return get(r) - get(l - 1);
}


int gcd(int a, int b) { return a == 0 ? b : gcd(b % a, a); }

#define EPS 1e-11

int dyn[201][101][101][101]; //2139062143

int hd_orig, b, d;
int deep = 0;

int main() {

	freopen("data.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

int TCount = nxi();
for (int T = 1; T <= TCount; ++T) {

	printf("Case #%d: ", T);
	cerr << T << endl;

	int n, c, m;
	cin >> n >> c >> m;

	vpii tickets(m);
	vector<vi> used(c, vi(n + 1));


	for (auto & p : tickets) {
		cin >> p.first >> p.second;
		p.second--;

		used[p.second][p.first]++;
	}

	int rols = 0, shifts = 0;
	int k = 0;
		for (int i = 0; i <= n; ++i) {
			for (int j = i + 1; j <= n; ++j) {
				if (used[k][i] > 0 && used[1 - k][j] > 0) {
					int l = min(used[k][i], used[1 - k][j]);
					rols += l;

					used[k][i] -= l, used[1 - k][j] -= l;
				}
			}
			for (int j = i - 1; j > 0; --j) {
				if (used[k][i] > 0 && used[1 - k][j] > 0) {
					
					int l = min(used[k][i], used[1 - k][j]);
					rols += l;
					used[k][i] -= l, used[1 - k][j] -= l;
				}
			}

		}

		for (int i = 0; i <= n; ++i) {
			if (used[k][i] > 0) {
				if (used[1 - k][i] > 0 && i > 1) {
					int l = min(used[k][i], used[1 - k][i]);
					rols += l;
					shifts += l;
					used[k][i] -= l, used[1 - k][i] -= l;
				}
			}

			rols += used[k][i] + used[1 - k][i];
		}
	
	

	cout << rols << ' ' << shifts << endl;
	
}

	return 0;
}


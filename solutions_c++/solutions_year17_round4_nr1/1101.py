#include <iostream>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <set>
#include <cstring>
#include <map>
#include <bitset>
#include <random>
#include <stack>
#include <list>
#include <unordered_set>
#include <unordered_map>
#include <ctime>
#include <cassert> // For debug

using namespace std;

#define ll long long
#define ld long double
#define pb push_back
#define sc second
#define fs first
#define mp make_pair
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()

template<class T> T sqr(T x) { return x*x; }
ld pi = 3.1415926535897932384626433832795;
ll mod = 1e9 + 7;

const int N = 1e2 + 5;

ll gcd(ll a, ll b) {
	return b ? gcd(b, a % b) : a;
}

int tests;

void solve(int test) {
	int ans = 0;
	int n, p;
	vector<int> a;
	bool used[N];
	memset(used, 0, sizeof(used));
	cin >> n >> p;
	for (int i = 0; i < n; i++) {
		int t;
		cin >> t;
		if (t%p == 0)
			ans += 1;
		else
			a.push_back(t);
	}
	int cur = 0;
	for (int i = 0; i < a.size(); i++) {
		for (int j = i + 1; j < a.size(); j++) {
			if (!used[i] && !used[j]) {
				if ((a[i] + a[j])% p == 0) {
					ans++;
					used[i] = 1;
					used[j] = 1;
				}
			}
		}
	}
	vector<int> b;
	b.clear();
	for (int i = 0; i < a.size(); i++) {
		if (!used[i]) b.push_back(a[i]);
	}
	a = b;
	memset(used, 0, sizeof(used));
	for (int i = 0; i < a.size(); i++) {
		for (int j = i + 1; j < a.size(); j++) {
			for (int k = j + 1; k < a.size(); k++) {
				if (!used[i] && !used[j] && !used[k]) {
					if ((a[i] + a[j] + a[k])% p == 0) {
						ans++;
						used[i] = 1;
						used[j] = 1;
						used[k] = 1;
					}
				}
			}

		}
	}
	b.clear();
	for (int i = 0; i < a.size(); i++) {
		if (!used[i]) b.push_back(a[i]);
	}
	a = b;
	memset(used, 0, sizeof(used));
	for (int i = 0; i < a.size(); i++) {
		for (int j = i + 1; j < a.size(); j++) {
			for (int k = j + 1; k < a.size(); k++) {
				for (int k1 = k + 1; k1 < a.size(); k1++) {
					if (!used[i] && !used[j] && !used[k] && !used[k1]) {
						if ((a[i] + a[j] + a[k] + a[k1])% p == 0) {
							ans++;
							used[i] = 1;
							used[j] = 1;
							used[k] = 1;
							used[k1] = 1;
						}
					}
				}

			}
		}
	}
	b.clear();
	for (int i = 0; i < a.size(); i++) {
		if (!used[i]) b.push_back(a[i]);
	}
	a = b;
	if (a.size())
		ans += 1;
	cout << "Case #" << test << ": " << ans << endl;
}

int main() {
	FILE *f1, *f2;
	freopen_s(&f1, "A-large.in", "r", stdin);
	freopen_s(&f2, "A-large.out", "w", stdout);
	
	cin >> tests;
	for (int i = 1; i <= tests; i++) {
		solve(i);
	}
	return 0;
}
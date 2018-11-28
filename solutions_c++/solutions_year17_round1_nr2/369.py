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

ll gcd(ll a, ll b) {
	return b ? gcd(b, a % b) : a;
}

ll _gcd(ll a, ll b, ll & x, ll & y) {
	if (a == 0) {
		x = 0; y = 1;
		return b;
	}
	ll _x1, _y1;
	ll d = _gcd(b%a, a, _x1, _y1);
	x = _y1 - (b / a) * _x1;
	y = _x1;
	return d;
}

ld binpow(ld a, ll n) {
	ld res = 1;
	while (n) {
		if (n & 1)
			res *= a;
		a *= a;
		n >>= 1;
		//a %= mod;
		//res %= mod;
	}
	return res;
}

const int N = 3e5 + 10;

int ptr[1111], fixd[1111], need[1111], a[1111][1111];

pair<ld, ld> process(ld l1, ld r1, ld l2, ld r2) {
	return mp(max(l1, l2), min(r1, r2));
}

void solve(int test) {
	int n, p;
	cin >> n >> p;
	int ans = 0;
	memset(ptr, 0, sizeof(ptr));
	memset(fixd, 0, sizeof(fixd));
	for (int i = 0; i < n; i++) cin >> need[i];
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < p; j++) {
			cin >> a[i][j];
		}
		sort(a[i], a[i] + p);
	}
	ld eps = 1e-9;
	for (int i = 0; i < p; i++) {

		for (int j = 0; j < n; j++) ptr[j] = fixd[j];

		ld r = ((ld)a[0][i] / 0.9)/need[0]+eps, l = ((ld)a[0][i] / 1.1)/need[0]-eps;
		for (int j = 1; j < n; j++) {
			ld r1 = ((ld)a[j][ptr[j]] / 0.9) / need[j]+eps, l1 = ((ld)a[j][ptr[j]] / 1.1) / need[j]-eps;
			while (1) {
				if (ptr[j] >= p) {
					r = 0, l = 1;
					break;
				}
				r1 = ((ld)a[j][ptr[j]] / 0.9) / need[j]+eps, l1 = ((ld)a[j][ptr[j]] / 1.1) / need[j]-eps;
				ld l2, r2;
				pair<ld, ld> pr = process(l, r, l1, r1);
				l2 = pr.fs, r2 = pr.sc;
				if (l2 <= r2 && (int)r2 >= l2) {
					l = l2, r = r2;
					break;
				}
				else ptr[j]++;
			}
		}
		if (l <= r && (int)r >= l) {
			for (int j = 0; j < n; j++) ptr[j]++, fixd[j] = ptr[j];
			ans++;
		}
	}
	printf("Case #%d: %d\n", test, ans);
}


int main() {
	FILE *f1, *f2;
	freopen_s(&f1, "B-large.in", "r", stdin);
	freopen_s(&f1, "B-large.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		solve(i);
	}
	return 0;
}
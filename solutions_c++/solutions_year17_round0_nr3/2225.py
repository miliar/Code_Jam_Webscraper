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
#define re(x) x.rbegin(), x.rend()

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

const int N = 1e3 + 10;


void solve(int test) {
	ll n, k;
	cin >> n >> k;
	set<ll> s;
	map<ll, ll> cnt;
	cnt[n] = 1;
	s.insert(-n);
	ll ans;
	while (1) {
		ll cur = -*s.begin();
		s.erase(s.begin());
		ll cur_cnt = cnt[cur];
		if (k <= cur_cnt) {
			ans = cur;
			break;
		} 
		k -= cur_cnt;
		cnt.erase(cur);
		ll a = cur / 2, b = cur - cur / 2;
		if (a < b) swap(a, b);
		a -= 1;
		cnt[a] += cur_cnt;
		cnt[b] += cur_cnt;
		s.insert(-a);
		s.insert(-b);
	}
	ll a = ans / 2, b = ans - ans / 2;
	if (a < b) swap(a, b);
	a--;
	swap(a, b);
	printf("Case #%d: %I64d %I64d \n", test, a, b);

}

int main() {
	FILE *f1, *f2;
	freopen_s(&f1, "C-large.in", "r", stdin);
	freopen_s(&f1, "C-large.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) solve(i + 1);
	return 0;
}
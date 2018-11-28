#pragma comment(linker, "/STACK:134217728") //128mb
#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <cassert>
#include <climits>
#include <ctime>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <bitset>
#include <complex>
using namespace std;


#define input_txt freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout)
#define in_out(x) freopen(x".in", "r", stdin);freopen(x".out", "w", stdout)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(s) int((s).size())
#define all(x) x.begin(),x.end()

typedef long long ll;
typedef long long llong;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef pair<int, int> pii;

const long long MOD = 1000000000 + 7; //1e9+7
const long long MAGIC = 123123123;
const double PI = 4 * atan(1.);
const double EPS = 1E-7;

void time_elapsed() { cout << "\nTIME ELAPSED: " << (double)clock() / CLOCKS_PER_SEC << " sec\n"; }
#define DOUT_VAR(x) cout << #x << " = " << (x) << endl

template<typename T> T gcd(T a, T b){ return ((!b) ? a : gcd(b, a%b)); }
template<typename T>T gcd(T a, T b, T&x, T&y){ if (!a){ x = 0, y = 1; return b; }T x1, y1; T d = gcd(b%a, a, x1, y1); x = y1 - (b / a)*x1; y = x1; return d; }

template<typename T> T lcm(T a, T b) { return (a / gcd(a, b))*b; }
template<typename T, typename M> T neg_mod(T a, M mod) { return ((a%mod) + mod) % mod; }
ll binpow(ll x, ll p) { ll res = 1; while (p){ if (p & 1) res *= x; x *= x; p >>= 1; }return res; }
ll binpow_mod(ll x, ll p, ll m) { ll res = 1; while (p){ if (p & 1) res = (res*x) % m; x = (x*x) % m; p >>= 1; }return res; }


pair<ll,ll> solve_stupid(ll n, ll k) {
	priority_queue<ll> que;
	que.push(n);
	ll minn, maxx;
	for (int i = 0; i < k; ++i) {
		ll cur = que.top();
		que.pop();
		minn = (cur - 1) / 2;
		maxx = cur / 2;
		que.push(minn);
		que.push(maxx);
	}
	return mp(minn, maxx);
}

pair<ll, ll> solve_smart(ll n, ll k) {
	map<ll, ll> cnt;
	ll total_cnt = 0;
	ll res;
	cnt[n] = 1;
	while (true) {
		auto it = cnt.end();
		it--;
		auto cur = it->first;
		ll ccnt = it->second;
		cnt.erase(it);

		total_cnt += ccnt;
		ll minn = (cur - 1) / 2;
		ll maxx = cur / 2;
		if (total_cnt >= k) {
			return mp(minn, maxx);
		}
		cnt[minn] += ccnt;
		cnt[maxx] += ccnt;
	}
}

int main() {
	input_txt;

	/*ll n;
	cin >> n;
	for (ll k = 1; k <= n; ++k) {
		auto stup = solve_stupid(n, k);
		auto smart = solve_smart(n, k);
		if (stup != smart) {
			cout << n << " " << k << " " << endl;
			printf("stupid: %I64d %I64d\n", stup.second, stup.first);
			printf("smart: %I64d %I64d\n", smart.second, smart.first);
			printf("\n");
		}
	}
	return 0;*/
	int tests_cnt;
	cin >> tests_cnt;

	for (int test = 1; test <= tests_cnt; ++test) {
		ll n, k;
		cin >> n >> k;
		auto res = solve_smart(n, k);
		printf("Case #%d: %I64d %I64d\n", test, res.second, res.first);
	}

	//time_elapsed();
	return 0;
}
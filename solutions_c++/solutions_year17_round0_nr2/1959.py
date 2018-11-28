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

ll n, k;

ll dist_sum = 0;

vector<vector<int>>g;
int used[200000];
ll dp1[200000][6];
ll dp2[200000][6];
ll subtree_sz[200000];



void dfs(int v) {
	used[v] = 1;
	vector<ll> pref_sum_r(k);
	subtree_sz[v] = 1;
	dp1[v][0] = 1;

	for (int i = 0; i < g[v].size(); ++i) {
		int to = g[v][i];
		if (!used[to]) {
			dfs(to);
			//update subtree_sz
			subtree_sz[v] += subtree_sz[to];
			dist_sum += subtree_sz[to] * (n - subtree_sz[to]);

			//update dp1
			for (int curr = 0; curr < k; ++curr) {
				dp1[v][curr] += dp1[to][(curr + k - 1) % k];
			}

			//update dp2
			for (int curr = 0; curr < k; ++curr) {
				dp2[v][curr] += (dp1[to][curr] + dp2[to][curr]);
				for (int first_r = 0; first_r < k; ++first_r) {
					int sec_r = (curr - first_r - 2 + 2*k) % k;
					dp2[v][curr] += dp1[to][sec_r] * pref_sum_r[first_r];
				}
			}

			//update pref_sum_r
			for (int curr = 0; curr < k; ++curr) {
				pref_sum_r[curr] += dp1[to][curr];
			}
		}
	}
}

int main() {
	input_txt;
	int tests_cnt;
	cin >> tests_cnt;

	for (int test = 1; test <= tests_cnt; ++test) {
		string str;
		cin >> str;
		int idx = 0;
		while (idx + 1 < str.length() && str[idx] <= str[idx + 1]) {
			idx++;
		}
		if (idx + 1 < str.length()) {
			while (idx > 0 && str[idx - 1] == str[idx]) {
				idx--;
			}
			str[idx]--;
			for (int i = idx + 1; i < str.length(); ++i) {
				str[i] = '9';
			}
		}
		printf("Case #%d: ", test);
		for (int i = 0; i < str.length(); ++i) {
			if (i == 0 && str[i] == '0') {
				continue;
			}
			printf("%c", str[i]);
		}
		printf("\n");
	}

	//time_elapsed();
	return 0;
}
#include<bits/stdc++.h>
#include <regex>
#include<ext/numeric>
#include<ext/hash_map>
using namespace std;
using namespace __gnu_cxx;

#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz(v)  (int)v.size()
#define WHITE -1
#define GREY   0
#define BLACK  1
#define CLR(a,v) memset(a,v,sizeof a)
#define PC(x) __builtin_popcount(x)
#define PCLL(x) __builtin_popcountll(x)
#define MP make_pair

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<ll> vll;
//typedef unsigned int ui;

typedef complex<double> point;
//#define X real()
//#define Y imag()
#define vec(a,b) ((b)-(a))
#define dot(a,b) ((conj(a)*(b)).real())
#define cross(a,b) ((conj(a)*(b)).imag())
#define colliner pointOnLine
#define same(a,b) (lengthSqr(vec(a,b))<EPS)
#define lengthSqr(v) (dot(v,v))

const double PI = acos(-1.0);

int dx[] = { 0, -1, 0, 1, -1, -1, 1, 1 };
int dy[] = { 1, 0, -1, 0, 1, -1, 1, -1 };

int DX[] = { 1, 1, -1, -1, 2, 2, -2, -2 };
int DY[] = { 2, -2, 2, -2, 1, -1, 1, -1 };

const int MAX = 25, MOD = 1e9 + 7, oo = (1 << 30), MAXN = 1e6 + 5;
const ll OO = 1ll << 60;
const double EPS = 1e-9;

int t;
ll k, n;

struct pair_hash {
	inline std::size_t operator()(const ll & v) const {
		return (v % MOD * 31) % MOD;
	}
};

int main() {
#ifndef ONLINE_JUDGE
	freopen("IN.in", "r", stdin);
//	freopen("access.in", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	scanf("%d", &t);
	for (int T = 1; T <= t; ++T) {
		printf("Case #%d: ", T);
		scanf("%lld%lld", &n, &k);
		if (n == k) {
			puts("0 0");
			continue;
		}
		priority_queue<ll> q;
		hash_map<ll, ll, pair_hash> mp;
		mp.insert(pair<ll, ll>(n, 1));
		q.push(n);
		while (!q.empty()) {
			ll x = q.top();
			q.pop();
			ll occ = mp[x];
			if (occ >= k) {
				if (x & 1)
					printf("%lld %lld\n", x / 2, x / 2);
				else
					printf("%lld %lld\n", x / 2, x / 2 - 1);
				break;
			}
			k -= occ;
			if (x & 1) {
				if (x > 1) {
					if (!mp[x / 2])
						q.push(x / 2);
					mp[x / 2] += occ * 2;
				}
			} else {
				if (x > 2) {
					if (!mp[x / 2 - 1])
						q.push(x / 2 - 1);
					mp[x / 2 - 1] += occ;
				}
				if (!mp[x / 2])
					q.push(x / 2);
				mp[x / 2] += occ;
			}
		}
	}
}


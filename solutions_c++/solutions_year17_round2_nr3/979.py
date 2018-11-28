#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <cstring>
#include <numeric>
#include <algorithm>
#include <functional>
#include <array>
#include <map>
#include <queue>
#include <limits.h>
#include <set>
#include <stack>
#include <random>
#include <complex>
#include <unordered_map>
#include <nmmintrin.h>
#include <chrono>
#define rep(i,s,n) for(int i = (s); (n) > i; i++)
#define REP(i,n) rep(i,0,n)
#define RANGE(x,a,b) ((a) <= (x) && (x) <= (b))
#define DUPLE(a,b,c,d) (RANGE(a,c,d) || RANGE(b,c,d) || RANGE(c,a,b) || RANGE(d,a,b))
#define INCLU(a,b,c,d) (RANGE(a,c,d) && (b,c,d))
#define PW(x) ((x)*(x))
#define ALL(x) (x).begin(), (x).end()
#define MODU 1000000007
#define bitcheck(a,b)   ((a >> b) & 1)
#define bitset(a,b)      ( a |= (1 << b))
#define bitunset(a,b)    (a &= ~(1 << b))
#define MP(a,b) make_pair((a),(b))
#define Manh(a,b) (abs((a).first-(b).first) + abs((a).second - ((b).second))
#define pritnf printf
#define scnaf scanf
#define itn int
#ifdef _MSC_VER
#define __builtin_popcount _mm_popcnt_u32
#define __builtin_popcountll _mm_popcnt_u64
#endif
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
ll gcd(ll a, ll b) {
	if (b == 0) return a;
	return gcd(b, a%b);
}
template<typename A, size_t N, typename T>
void Fill(A(&array)[N], const T &val) {
	std::fill((T*)array, (T*)(array + N), val);
}
template<typename T>
class Graph {
public:
	int vn;
	T sumcost = 0;
	vector<vector<pair<int,T>>> g;

	Graph(int n) {
		vn = n;
		g.resize(n);
	}
	virtual void con(int a, int b, T w) = 0;
	int getWeight(int f, int t) {
		auto itr = lower_bound(ALL(g[f]), make_pair(t, INT_MIN));
		if (itr != g[f].end())
			return itr->second;
		return INT_MIN;
	}
	int Costsum() {
		return sumcost;
	}
	void scan(int edcount, bool oindexed, bool w) {
		REP(i, edcount) {
			int a, b, c = 1;
			scanf("%d %d", &a, &b);
			if (w)scanf("%d", &c);
			con(a - oindexed, b - oindexed, c);
		}
	}
};
template<typename T>
class DGraph : public Graph<T> {//—LŒü
public:
	DGraph(int n) : Graph(n) {}
	void con(int a, int b, T w = 1) {
		g[a].push_back({ b,w });
		sumcost++;
	}
};
template<class T>
double Dijkstra(T g, int st, int en) {
	priority_queue<pair<double,int>, vector<pair<double, int>>, greater<pair<double, int>>> que;

	que.push({ 0, st });
	int kk = 0;
	vector<double> res(g.vn, -1);
	while (kk < g.vn && que.size()) {
		pair<double, int> cur = que.top();
		que.pop();
		if (res[cur.second] != -1)
			continue;
		res[cur.second] = cur.first;
		kk++;
		for (auto itr : g.g[cur.second]) {
			if (res[itr.first] == -1)
				que.push({ cur.first + itr.second,itr.first });
		}
	}
	return res[en];
}
signed main() {
	int t;
	scanf("%d", &t);
	REP(cc, t) {
		int n, q;
		scanf("%d %d", &n, &q);
		vector<pii> po(n);
		REP(i, n) {
			scanf("%d %d", &po[i].first, &po[i].second);
		}

		DGraph<double> g(n),hon(n);

		ll dist[101][101];
		REP(i, n) {
			REP(j, n) {
				scnaf("%lld", &dist[i][j]);
				if (dist[i][j] == -1)dist[i][j] = 1000000000000;
			}
		}
		for (int k = 0; k < n; k++)
			for (int i = 0; i < n; i++)
				for (int j = 0; j < n; j++)
					dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);



		REP(i, n) {
			REP(j, n) {
				if (dist[i][j] != -1 && dist[i][j] <= (ll)po[i].first) {
					g.con(i, j, (double)dist[i][j] / (double)po[i].second);
				}
			}
		}
		printf("Case #%d: ", cc + 1);
		REP(i, q) {
			int a, b;
			scanf("%d %d", &a, &b);
			a--; b--;
			printf("%.7lf", Dijkstra(g,a,b));
			if (i != q - 1)printf(" ");
		}
		printf("\n");
	}
	return 0;
}
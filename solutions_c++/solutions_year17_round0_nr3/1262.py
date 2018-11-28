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
#include <unordered_set>
#define rep(i,s,n) for(int i = (s); (n) > i; i++)
#define REP(i,n) rep(i,0,n)
#define RANGE(x,a,b) ((a) <= (x) && (x) <= (b))
#define DUPLE(a,b,c,d) (RANGE(a,c,d) || RANGE(b,c,d) || RANGE(c,a,b) || RANGE(d,a,b))
#define INCLU(a,b,c,d) (RANGE(a,c,d) && (b,c,d))
#define PW(x) ((x)*(x))
#define ALL(x) (x).begin(), (x).end()
#define RALL(x) (x).rbegin(), (x).rend()
#define MODU 1000000007
#define bitcheck(a,b)   ((a >> b) & 1)
#define bitset(a,b)      ( a |= (1 << b))
#define bitunset(a,b)    (a &= ~(1 << b))
#define MP(a,b) make_pair((a),(b))
#define Manh(a,b) (abs((a).first-(b).first) + abs((a).second - ((b).second))
#define pritnf printf
#define scnaf scanf
#define itn int
#define PI 3.141592653589


#define izryt bool

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
template<typename A, size_t N, typename T>
void Fill(A(&array)[N], const T &val) {
	std::fill((T*)array, (T*)(array + N), val);
}
struct UnionFind {
	vector<int> data;
	UnionFind(int size) : data(size, -1) { }
	bool unionSet(int x, int y) { //‚˜‚Ì“ü‚Á‚Ä‚éW‡‚Æ y‚Ì“ü‚Á‚Ä‚éW‡‚ğ•¹‡
		x = root(x); y = root(y);
		if (x != y) {
			if (data[y] < data[x]) swap(x, y);
			data[x] += data[y]; data[y] = x;
		}
		return x != y;
	}
	bool findSet(int x, int y) { //x‚Æy‚ª“¯‚¶W‡‚É“ü‚Á‚Ä‚¢‚é‚©‚Ç‚¤‚©‚ğ”»’è
		return root(x) == root(y);
	}
	int root(int x) {
		return data[x] < 0 ? x : data[x] = root(data[x]);
	}
	bool isroot(int x) {
		return data[x] < 0;
	}
	int size(int x) {
		return -data[root(x)];
	}
};

signed main() {
	int n;
	scanf("%d", &n);
	
	REP(i, n) {
		ll a, b;
	
		scanf("%lld %lld", &a, &b);

		map<ll, ll> cou;

		cou[-a] = 1;

		ll sum = 0;

		while (1) {
			pll cur = *cou.begin();
			cur.first *= -1;
			ll l = (cur.first-1) / 2, r = (cur.first) / 2;
			sum += cur.second;
			if (sum >= b) {
				printf("Case #%d: %lld %lld\n", i+1, max(l,r), min(l,r));
				break;
			}

			cou.erase(-cur.first);
			
			if(l)
				cou[-l] += cur.second;
			if(r)
				cou[-r] += cur.second;
		}

	}

	return 0;
}
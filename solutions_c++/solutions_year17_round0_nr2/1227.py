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
typedef unsigned long long ll;
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
	REP(cc, n) {
		ll num;

		scanf("%lld", &num);

		ll ans = 0;
		ll base = 1;
		ll inc = 0;
		
		while (num / base) {
			base *= 10;
		}
		base /= 10;
		ll bef = 0;
		ll i;
		ll ren;
		for (i = base; 1 <= i; i /= 10) {
			if (bef <= num/i) {
				if (bef == num / i) ren++;
				else ren = 1;
				bef = num / i;
				inc += i * (num / i);
				num %= i;
			}
			else break;
		}
		i *= pow(10, ren);
		if (i) {
			inc -= i;
			inc /= i;
			inc *= i;
			i /= 10;
		}
		for (; 1 <= i; i /= 10) {
			inc += 9 * i;
		}
		printf("Case #%d: %lld\n",cc+1, inc);
	}

	return 0;
}
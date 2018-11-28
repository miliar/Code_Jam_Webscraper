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
#include <list>
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
#define PI 3.141592653589
#ifdef _MSC_VER
#define __builtin_popcount _mm_popcnt_u32
#define __builtin_popcountll _mm_popcnt_u64
#endif
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
template<typename A, size_t N, typename T>
void Fill(A(&array)[N], const T &val) {
	std::fill((T*)array, (T*)(array + N), val);
}


signed main() {

	int t;
	scanf("%d", &t);
	REP(cc, t) {
		int n, p;
		scanf("%d %d", &n, &p);
		map<int,int> cho;
		int ans = 0, nok = n;
		REP(i, n) {
			int buf;
			scanf("%d", &buf);
			buf %= p;
			if (buf)
				cho[buf]++;
			else
				ans++, nok--;
		}
		if (p == 2) {
			ans += cho[1] / 2;
			nok -= (cho[1] / 2) * 2;
		}
		else if (p == 3) {
			int gen = min(cho[2], cho[1]);
			ans += gen;
			nok -= gen * 2;
			
			cho[2] -= gen;
			cho[1] -= gen;

			ans += cho[1] / 3;
			nok -= (cho[1] / 3) * 3;

			ans += cho[2] / 3;
			nok -= ((cho[2]) / 3)*3;
		}
		else {
			int gen = min(cho[3], cho[1]);
			ans += gen;
			nok -= gen * 2;
			cho[1] -= gen;
			cho[3] -= gen;

			gen = min(cho[2], cho[1]/2);
			ans += gen;
			nok -= gen * 3;
			cho[1] -= gen*2;
			cho[2] -= gen;

			ans += cho[1] / 4;
			nok -= (cho[1] / 4) * 4;
			cho[1] -= (cho[1] / 4) * 4;

			ans += cho[2] / 2;
			nok -= (cho[2] / 2) * 2;
			cho[2] -= (cho[2] / 2) * 2;

			ans += cho[3] / 4;
			nok -= (cho[3] / 4) * 4;
			cho[3] -= (cho[3] / 4) * 4;

		}
		printf("Case #%d: %d\n", cc+1, ans + ((bool)nok),nok);
	}

	return 0;
}
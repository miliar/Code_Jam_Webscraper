#include <iostream>
#include <iomanip>
#include <cstdio>
#include <bitset>
#include <memory>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <string>
#include <cstring>
#include <fstream>
#include <functional>
#include <stack>
#include <complex>
#include <wchar.h>
#include <wctype.h>
#include <cmath>
#include <queue>
#include <ctime>
#include <numeric>
#include <unordered_map>
#include <unordered_set>

#ifdef _MSC_VER
#  include <intrin.h>
#  define __builtin_popcount __popcnt
#endif

using namespace std;

template<typename T> T mabs(const T &a){ return a<0 ? -a : a; }
#define rep(x,y,z) for(int x=(y),e##x=(z);x<e##x;x++)
#define SQR(x) ((x)*(x))
#define all(c) (c).begin(), (c).end()

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef short int si;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<ll, int> pli;
typedef pair<int, ll> pil;


void init() {
	
}

void test() {
    using IntType = uint64_t;
    IntType n, k;
    scanf(" %llu%llu", &n, &k);
    using Pair = std::pair<IntType, IntType>;

    std::map<IntType, IntType, std::greater<IntType>> positions;
    positions[n] = 1;

    Pair result = { -1, -1 };
    while (1) {
        auto curBest = positions.begin();
        auto curLength = curBest->first;
        auto curCount = curBest->second;
        if (curLength == 0) {
            throw 1;
        }
        positions.erase(curBest);
        auto greater = curLength / 2, lesser = (curLength - 1) / 2;
        if (curCount >= k) {
            result = { greater, lesser };
            break;
        }
        k -= curCount;
        positions[greater] += curCount;
        positions[lesser] += curCount;
    }
    if (result.first == -1) {
        throw 1;
    }
    printf("%llu %llu\n", result.first, result.second);
}

void run()
{
	init();
	int tc;
	scanf("%d", &tc);
	rep(i, 0, tc) {
		printf("Case #%d: ", i + 1);
		test();
	}
}

//#define prob "fence"

int main()
{
#ifdef LOCAL_DEBUG
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	time_t st = clock();
#else 
#ifdef prob
	freopen(prob".in", "r", stdin);
	freopen(prob".out", "w", stdout);
#endif
#endif

	run();

#ifdef LOCAL_DEBUG
	fprintf(stderr, "\n=============\n");
	fprintf(stderr, "Time: %.2lf sec\n", (clock() - st) / double(CLOCKS_PER_SEC));
#endif

	return 0;
}
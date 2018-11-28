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
	//return;
	//memset(dyn, -1, sizeof(dyn));
	//dyn[1] = 1;
	//bfs();
}

void test() {
    char buf[100500];
    scanf(" %s", buf+1);
    buf[0] = '0';
    int badPos = -1;
    for (int index = 2; ; index++) {
        if (buf[index] == 0) {
            break;
        }
        if (buf[index] < buf[index - 1]) {
            badPos = index - 1;
            break;
        }
    }

    if (badPos > 0) {
        while (buf[badPos] == buf[badPos - 1]) {
            badPos--;
        }

        buf[badPos++]--;
        while (buf[badPos] != 0) {
            buf[badPos++] = '9';
        }
    }

    int startIndex = 0;
    while (buf[startIndex] == '0') {
        startIndex++;
    }

	printf("%s\n", buf + startIndex);
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
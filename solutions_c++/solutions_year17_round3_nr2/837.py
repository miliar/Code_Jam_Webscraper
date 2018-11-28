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
#include <limits>
#include <tuple>

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

struct Task {
    int start;
    int end;
    int who;
    bool operator<(const Task& other) {
        return start < other.start;
    }
};

void test() {
    int ac, aj;
    scanf("%d%d", &ac, &aj);
    int totalCnt = ac + aj;
    vector<Task> tasks;
    int counts[2] = { ac, aj };
    int freetimes[2] = {720, 720};
    rep(idx, 0, 2) {
        rep(i, 0, counts[idx]) {
            int bg, ed;
            scanf("%d%d", &bg, &ed);
            tasks.push_back({ bg, ed, idx });
            freetimes[idx] -= ed - bg;
        }
    }

    std::sort(all(tasks));

    int changes = 0;
    std::multiset<int> dists[2];
    for (int i = 1; i < totalCnt; i++) {
        if (tasks[i].who != tasks[i - 1].who) {
            changes++;
        }
        else {
            dists[tasks[i].who].insert(tasks[i].start - tasks[i - 1].end);
        }
    }
    if (tasks[0].who != tasks.back().who) {
        changes++;
    }
    else {
        dists[tasks[0].who].insert(1440 + tasks[0].start - tasks.back().end);
    }

    int result = 0;
    rep(idx, 0, 2) {
        auto& cds = dists[idx];
        while (cds.size() > 0) {
            auto it = cds.begin();
            if (*it <= freetimes[idx]) {
                freetimes[idx] -= *it;
                cds.erase(it);
            }
            else {
                break;
            }
        }
        result += cds.size();
    }
    if (ac != 0 && aj != 0)
        result++;
    result *= 2;
    printf("%d\n", result);
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
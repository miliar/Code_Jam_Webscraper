#define _USE_MATH_DEFINES
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

using namespace std;

template<typename T> T mabs(const T &a){ return a<0?-a:a;}
#define rep(x,y,z) for(int x=(y),e##x=(z);x<e##x;x++)
#define SQR(x) ((x)*(x))
#define all(c) (c).begin(), (c).end()

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef short int si;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<ll,int> pli;
typedef pair<int,ll> pil;

void init() {
	//return;
}

const int MAX_CNT = 1005;

ll dyn[MAX_CNT][MAX_CNT] = { 0 };

vector<pll> pancakes;

ll getDyn(int taken, int last) {
    if (taken <= 0) {
        return 0;
    }
    if (taken == 1) {
        return 2 * pancakes[last].first * pancakes[last].second;
    }
    if (taken - 1 > last) {
        return -1e17;
    }
    auto& curVal = dyn[taken][last];
    if (curVal != -1)
        return curVal;
    ll bestVal = 0;
    auto curRad = pancakes[last].first;
    for (int i = std::max(taken - 2, 0); i < last; i++) {
        auto prevRad = pancakes[i].first;
        auto toAdd = SQR(prevRad) - SQR(curRad);
        ll curVal = toAdd + getDyn(taken - 1, i);
        bestVal = std::max(curVal, bestVal);
    }
    ll toAdd = 2 * pancakes[last].first * pancakes[last].second;
    bestVal += toAdd;
    curVal = bestVal;
    return curVal;
}

void test() {
    memset(dyn, -1, sizeof(dyn));
    int n, k;
    scanf(" %d%d", &n, &k);
    pancakes.resize(n);
    for (int i = 0; i < n; i++) {
        scanf(" %lld %lld", &pancakes[i].first, &pancakes[i].second);
    }
    std::sort(pancakes.begin(), pancakes.end());
    std::reverse(pancakes.begin(), pancakes.end());

    ll result = 0;
    for (int i = k - 1; i < n; i++) {
        ll curResult = getDyn(k, i) + SQR(pancakes[i].first);
        if (curResult > result) {
            result = curResult;
        }
    }
    if (result > 1e17)
        throw 1;
    double resultDbl = result * M_PI;
    printf("%lf\n", resultDbl);
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
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    time_t st=clock();
#else 
#ifdef prob
    freopen(prob".in","r",stdin);
    freopen(prob".out","w",stdout);
#endif
#endif

    run();

#ifdef LOCAL_DEBUG
    fprintf(stderr, "\n=============\n");
    fprintf(stderr, "Time: %.2lf sec\n",(clock()-st)/double(CLOCKS_PER_SEC));
#endif
    
    return 0;
}
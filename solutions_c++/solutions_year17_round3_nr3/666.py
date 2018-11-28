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
}

void test() {
    int n, k;
    double u;
    std::vector<double> probs;
    scanf(" %d%d%lf", &n, &k, &u);
    rep(i, 0, n) {
        double cprob;
        scanf("%lf", &cprob);
        probs.push_back(cprob);
    }

    sort(all(probs));
    probs.push_back(1.0);
    double totalProb = 1.0;
    bool oop = false;
    rep(i, 0, n) {
        double diff = probs[i + 1] - probs[i];
        if (oop) {
            totalProb *= probs[i];
        }
        else if (u >= diff * (i + 1)) {
            u -= diff * (i + 1);
        }
        else {
            oop = true;
            probs[i] += u / (i + 1);
            totalProb = std::pow(probs[i], i + 1);
        }
    }

    printf("%lf\n", totalProb);
}

void run()
{
	init();
	int tc;
	scanf("%d", &tc);
	rep(i, 0, tc) {
        fprintf(stderr, "%d\n", i);
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
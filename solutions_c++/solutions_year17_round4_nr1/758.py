#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <functional>
#include <numeric>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#include <list>
#include <stack>
#include <tuple>
#include <utility>
#include <complex>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <climits>
#include <typeinfo>
using namespace std;

typedef long long lint;
typedef pair<int,int> pii;
typedef pair<lint,lint> pll;

#define REP(i,n) for(int i=0; i<(n); i++)
#define REPA(i,s,e) for(int i=(s); i<=(e); i++)
#define REPD(i,s,e) for(int i=(s); i>=(e); i--)
#define ALL(a) (a).begin(), (a).end()

#define PRT(a) cerr << #a << " = " << (a) << endl
#define PRT2(a, b) cerr << #a << " = " << (a) << ", " << #b << " = " << (b) << endl
#define PRT3(a, b, c) cerr << #a << " = " << (a) << ", " << #b << " = " << (b) << ", " << #c << " = " << (c) <<  endl
template <class Ty> void print_all(Ty b, Ty e) {
    cout << "[ ";
    for(Ty p=b; p!=e; ++p) {
        cout << (*p) << ", ";
    }
    cout << " ]" << endl;
}

// -----------------------------------------------------------------------------
// Code starts 
// -----------------------------------------------------------------------------

int N, P;
int G[111];
bool used[111];

void solve() {
    cin >> N >> P;
    REP(i, N) cin >> G[i];

    REP(i, N) G[i] %= P;
    sort(G, G+ N);
    memset(used, 0, sizeof(used));

    int ans = 0;
    int res = 0;
    REP(p, N) {
        if (used[p]) continue;
        if (G[p] == 0) {
            ans += 1;
            used[p] = true;        
            continue;
        }

        if (res == 0) {
            res = P - G[p];
            used[p] = true;
            ans += 1;
        } else {
            res -= G[p];
            if (res < 0) {
                res += P;
            }
        }

        if (res != 0) {
            bool found = false;
            for (int q = p + 1; q < N; q++) {
                if (!used[q] && res == G[q]) {
                    res = 0;
                    used[q] = true;
                    found = true;
                    break;
                }
            }
        }
    }

    printf("%d\n", ans);
}

// -----------------------------------------------------------------------------
// Code ends 
// -----------------------------------------------------------------------------

void coding() {
    int T;
    cin >> T;
    REPA(t,1,T) {
        fprintf(stderr, "%3d / %d\n", t, T);
        printf("Case #%d: ", t);
        solve();
    }
}

#define _LOCAL_TEST 1

int main() {
#if _LOCAL_TEST == 0
    clock_t startTime = clock();
    freopen("a.in", "r", stdin);
#elif _LOCAL_TEST == 1
    freopen("../input/A-small-attempt0.in", "r", stdin);
    freopen("../output/A-small.out", "w", stdout);
#elif _LOCAL_TEST == 2
    freopen("../input/A-large.in", "r", stdin);
    freopen("../output/A-large.out", "w", stdout);
#endif

    coding();

#if _LOCAL_TEST == 0
    clock_t elapsedTime = clock() - startTime;
    cerr << endl;
    cerr << (elapsedTime / 1000.0) << " sec elapsed." << endl;
    cerr << "This is local test" << endl;
    cerr << "Do not forget to comment out _LOCAL_TEST" << endl << endl;
#endif

}

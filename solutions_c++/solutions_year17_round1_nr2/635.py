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
int R[55];
int Q[55][55];
int used[55][55];

int temp[55];

bool check(int m) {
    bool ok = true;

    REP(i, N) temp[i] = -1;

    REP(i, N) {
        REP(p, P) {
            if (!used[i][p] && Q[i][p] >= R[i] * m * 0.9 && Q[i][p] <= R[i] * m * 1.1) {
                temp[i] = p;
                break;
            }
        }

        if (temp[i] < 0) {
            ok = false;
            break;
        }
    }

    if (ok) {
        REP(i, N) {
            used[i][temp[i]] = true;
        }
    }
    return ok;
}

void solve() {
    cin >> N >> P;
    REP(i, N) cin >> R[i];
    REP(i, N) {
        REP(j, P) {
            cin >> Q[i][j];
        }
    }

    REP(i, N) {
        sort(Q[i], Q[i] + P);
    }

    int lower = 1 << 25;
    int upper = 1;
    REP(i, N) {
        int l = (int)floor(Q[i][0] / (1.1 * R[i]));
        int u = (int)ceil(Q[i][P - 1] / (0.9 * R[i]));
        lower = min(l, lower);
        upper = max(u, upper);
    }

    if (lower > upper) {
        printf("0\n");
        return;
    }

    memset(used, 0, sizeof(used));

    int ans = 0;
    REPA(m, lower, upper) {
        while (check(m)) {
            ans += 1;
        }
    }

    cout << ans << endl;
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

#define _LOCAL_TEST 2

int main() {
#if _LOCAL_TEST == 0
    clock_t startTime = clock();
    freopen("b.in", "r", stdin);
#elif _LOCAL_TEST == 1
    freopen("../input/B-small-attempt0.in", "r", stdin);
    freopen("../output/B-small.out", "w", stdout);
#elif _LOCAL_TEST == 2
    freopen("../input/B-large.in", "r", stdin);
    freopen("../output/B-large.out", "w", stdout);
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

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

int check(std::string &line, int n) {
    int ret = 0;
    int m = line.size();
    for (int i = 0; i < m - n + 1; i++) {
        if (line[i] == '-') {
            for (int j = i; j < i + n; j++) {
                if (line[j] == '-') {
                    line[j] = '+';
                } else {
                    line[j] = '-';
                }
            }
            ret += 1;
        }
    }

    for (int i = 0; i < m; i++) {
        if (line[i] == '-') {
            return -1;
        }
    }

    return ret;
}

void solve() {
    std::string line, rev;
    int n;
    cin >> line >> n;

    rev = line;
    reverse(ALL(rev));

    int a = check(line, n);
    int b = check(rev, n);
    if (a >= 0 || b >= 0) {
        if (a == -1) {
            printf("%d\n", b);
        } else if (b == -1) {
            printf("%d\n", a);
        } else {
            printf("%d\n", std::min(a, b));
        }
    } else {
        printf("IMPOSSIBLE\n");
    }
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

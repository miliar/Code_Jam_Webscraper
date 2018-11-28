#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
#include <string>
#include <sstream>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

typedef pair<double, double> PDD;
typedef pair<double, int> PDI;

#define MP make_pair
#define PB push_back
#define FF first
#define SS second

#define FORN(i, n) for (int i = 0; i <  (int)(n); i++)
#define FOR1(i, n) for (int i = 1; i <= (int)(n); i++)
#define FORD(i, n) for (int i = (int)(n) - 1; i >= 0; i--)

#define DEBUG(X) { cout << #X << " = " << (X) << endl; }
#define PR0(A,n) { cout << #A << " = "; FORN(_,n) cout << A[_] << ' '; cout << endl; }

#define MOD 1000000007

int GLL(LL& x) {
    return scanf("%lld", &x);
}

int GI(int& x) {
    return scanf("%d", &x);
}

int T;

int d, n; double k, s;

void solve() {
    GI(d); GI(n);

    double worst = 0.0;

    FORN(i, n) {
        cin >> k >> s;
        worst = max(worst, (d - k) / s);
    }

    cout << setprecision(12) << d / worst << "\n";
}

int main() {
    GI(T);

    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        solve();
    }
    
    return 0;
}

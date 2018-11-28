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
#define INF 2000000000

int GLL(LL& x) {
    return scanf("%lld", &x);
}

int GI(int& x) {
    return scanf("%d", &x);
}

int T;

LL n, k;

map<LL, LL> gapcnt;

int main() {
    cin >> T;

    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";

        GLL(n); GLL(k);

        gapcnt = map<LL, LL>();
        gapcnt[n]++;

        LL left = k;

        while (left > 0) {
            auto largest = gapcnt.rbegin();

            LL ldist = (largest->FF - 1) / 2;
            LL rdist = (largest->FF) / 2;

            if (largest->SS < left) {
                if (ldist > 0) gapcnt[ldist] += largest->SS;
                if (rdist > 0) gapcnt[rdist] += largest->SS;
                left -= largest->SS;

                gapcnt.erase(largest->FF);
            }
            else {
                cout << rdist << " " << ldist << "\n";
                break;
            }
        }
    }
    
    return 0;
}

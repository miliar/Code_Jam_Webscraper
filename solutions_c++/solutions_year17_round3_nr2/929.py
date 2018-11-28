#include <algorithm>
#include <string>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iostream>
#include <fstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <stdlib.h>
#include <stdio.h>
#include <bitset>
#include <iterator>
#include <ctime>

using namespace std;

#define FOR(i, n) for (int i=0; i<n; ++i)
#define FORE(i, n) for (int i=0; i<=n; ++i)
#define REP(i, a, b) for (int i=a; i<b; ++i)
#define REPE(i, a, b) for (int i=a; i<=b; ++i)
#define mp make_pair
#define pb push_back

typedef long double dbl;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long int LL;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<VI> VVI;
const dbl pi = 3.14159265358979323846;
const int inf = (int) 1e9;
const dbl eps = 1e-9;


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    FOR(TT, T) {
        cout << "Case #" << TT + 1 << ": ";
        cerr << TT + 1 << "\n";
        int nc,nj;
        cin >> nc >> nj;
        VPII ac(nc);
        VPII aj(nj);
        FOR(i,nc) {
            cin >> ac[i].first >> ac[i].second;
        }
        FOR(i,nj) {
            cin >> aj[i].first >> aj[i].second;
        }
        if (nc == 1 || nj == 1) {
            cout << "2\n";
            continue;
        }
        if (nc == 2) {
            if (ac[0].first > ac[1].first) {
                swap(ac[0], ac[1]);
            }
            if (ac[1].second - ac[0].first > 720
                    && ac[1].first - ac[0].second < 720) {
                cout << "4\n";
            } else {
                cout << "2\n";
            }
            continue;
        }
        if (aj[0].first > aj[1].first) {
            swap(aj[0], aj[1]);
        }
        if (aj[1].second - aj[0].first > 720
                && aj[1].first - aj[0].second < 720) {
            cout << "4\n";
        } else {
            cout << "2\n";
        }
    }
    return 0;
}
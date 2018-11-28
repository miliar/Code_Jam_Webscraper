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
        string s;
        cin >> s;
        int k;
        cin >> k;
        int res = 0;
        FORE(i, (int) s.size() - k) {
            if (s[i] == '+') {
                continue;
            }
            ++res;
            REP(j, i, i + k) {
                if (s[j] == '-') {
                    s[j] = '+';
                } else {
                    s[j] = '-';
                }
            }
        }
        bool ok = true;
        FOR(i,(int)s.size()) {
            if (s[i] == '-') {
                ok = false;
                break;
            }
        }
        if (ok) {
            cout << res << "\n";
        } else {
            cout << "IMPOSSIBLE\n";
        }
    }
    return 0;
}
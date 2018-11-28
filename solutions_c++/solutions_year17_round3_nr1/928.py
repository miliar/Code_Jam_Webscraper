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

bool pred(const PII &i, const PII &j) {
    if (i.first == j.first) {
        return i.second > j.second;
    }
    return i.first > j.first;
}

LL v[1005];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    FOR(TT, T) {
        cout << "Case #" << TT + 1 << ": ";
        cerr << TT + 1 << "\n";
        int n, k;
        cin >> n >> k;
        VPII a(n);
        FOR(i, n) {
            cin >> a[i].first >> a[i].second;
        }
        sort(a.begin(), a.end(), pred);
        vector<LL> b(n);
        FOR(i, n) {
            b[i] = a[i].first * 2ll * a[i].second;
        }
        LL res = 0;
        FORE(i, n - k) {
            LL now = b[i] + a[i].first * 1ll * a[i].first;
            int cnt = 0;
            REP(j, i + 1, n) {
                v[cnt++] = b[j];
            }
            sort(v, v + cnt);
            reverse(v, v + cnt);
            FOR(j, k - 1) {
                now += v[j];
            }
            res = max(res, now);
        }
        double out = (double) res;
        out *= pi;
        cout << fixed << setprecision(9) << out << "\n";
    }
    return 0;
}
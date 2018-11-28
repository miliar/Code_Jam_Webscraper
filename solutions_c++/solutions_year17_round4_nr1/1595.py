#include <algorithm>
#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <cassert>
#include <string>
using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); ++i)
#define forv(i, v) forn(i, (v).size())
#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair


int findMaxFresh(const vector<int>& a, int p) {
    vector<int> c(p);
    int res = 0;
    for (int x : a) ++c[x % p];
    if (c[0]) res += c[0];
    if (p == 2) {
        res += (c[1] + 1) / 2;
    } else if (p == 3) {
        int m = min(c[1], c[2]);
        res += m;
        c[1] -= m;
        c[2] -= m;
        m = c[1] + c[2];
        res += (m + 2) / 3;
    } else {
        assert(p == 4);
        int m = c[2];
        res += m / 2;
        c[2] = m % 2;
        m = min(c[1], c[3]);
        res += m;
        c[1] -= m;
        c[3] -= m;
        if (c[2] || c[1] || c[3]) {
            ++res;
            c[2] = 0;
            m = c[1] + c[3];
            m -= min(2, m);
            if (m) {
                res += (m + 3) / 4;
            }
        }
    }
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    int numTests;
    cin >> numTests;
    //cout.precision(10);
    //cout << fixed;
    forn(tId, numTests) {
        int n, p;
        cin >> n >> p;
        vector<int> a(n);
        forn(i,  n) cin >> a[i];
        cout << "Case #" << tId + 1 << ": " << findMaxFresh(a, p) << endl;
    }
    return 0;
}

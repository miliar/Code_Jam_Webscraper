#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iterator>
#include <utility>
#include <algorithm>
#include <list>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>

using namespace std;

#define pb push_back
#define sz(v) ((long long)v.size())
#define mp make_pair
#define FOR(i,n) for(long long i = 0;i < (n);++i)
#define MOD 1000000007

void solve() {
    //cerr << "#######################" << endl;
    long long n, p;
    cin >> n >> p;
    vector<long long> r(n);
    FOR(i, n) {
        cin >> r[i];
    }
    vector<vector<long long>> q(n);
    FOR(i, n) {
        q[i] = vector<long long>(p);
        FOR(j, p) {
            cin >> q[i][j];
        }
        sort(q[i].begin(), q[i].end());
    }

    vector<long long> pointers(n);
    long long ans = 0;

    for (long long k = 1; k < 1001000; ++k) {
        bool stop = false;
        bool ok = true;
        FOR(i_ing, n) {
            while(pointers[i_ing] < p && q[i_ing][pointers[i_ing]] * 10 < r[i_ing] * k * 9) {
                ++pointers[i_ing];
            }
            if (pointers[i_ing] == p) {
                stop = true;
                ok = false;
            } else {
                if (q[i_ing][pointers[i_ing]] * 10 > r[i_ing] * k * 11) {
                    ok = false;
                    break;
                }
            }
        }
        if (stop) {
            break;
        }
        if (ok) {
            ++ans;
            //cerr << k << endl;
            k -= 1;
            FOR(i_ing, n) {
                ++pointers[i_ing];
            }
        }
    }
    cout << ans << endl;
}

int main() {
    int T;
    cin >> T;
    FOR(iter, T) {
        cout << "Case #" << iter + 1 << ": ";
        solve();
    }
}
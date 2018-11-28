/* Task solution for GCJ 2017
 * Tested with GCC 5.4.0
 * Build command line:
 *  g++ -std=gnu++14 -O2 -o <executable> <source.cpp>
 */

#include <cstdio>
#include <iostream>
#include <queue>

using namespace std;

typedef unsigned long long ull;

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int TN;
    cin >> TN;
    for (int T = 1; T <= TN; T++) {
        ull n, k;
        cin >> n >> k;
        struct E_a {
            ull w, k;
            E_a(ull w, ull k): w(w), k(k) {}
        };
        queue<E_a> a;
        a.emplace(n, 1);
//        cout << k << " (" << n << ",1)" << endl;
        while (k > a.front().k) {
            ull t = a.front().k;
            k -= t;
            ull w = a.front().w;
            ull v = ((w - 1) + 1) / 2;
            w = (w - 1) - v;
            if (a.back().w != v) {
                a.emplace(v, t);
            } else {
                a.back().k += t;
            }
            if (a.back().w != w) {
                a.emplace(w, t);
            } else {
                a.back().k += t;
            }
            a.pop();
//            {
//                auto q = a;
//                cout << k;
//                while (!q.empty()) {
//                    cout << " (" << q.front().w << ',' << q.front().k << ')';
//                    q.pop();
//                }
//                cout << endl;
//            }
        }
        ull w = a.front().w;
        ull v = ((w - 1) + 1) / 2;
        w = (w - 1) - v;
        cout << "Case #" << T << ": " << v << ' ' << w << endl;
    }
    return 0;
}

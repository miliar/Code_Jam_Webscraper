#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <map>
#include <ctime>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second

typedef long long ll;

double a[110];
double e[110], s[110];
double d[110];

int main() {
    freopen("C-small-attempt0.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    ios::sync_with_stdio(false);
    int t;
    cin >> t;
    forn (q, t) {
        int n, Q;
        cin >> n >> Q;
        forn (i, n) {
            a[i] = 0;
            cin >> e[i] >> s[i];
        }
        forn (i, n) {
            forn (j, n) {
                int x;
                cin >> x;
                if (j == i + 1) {
                    a[i + 1] = a[i] + x;
                }
            }
        }
        cout.precision(10);
        cout << "Case #" << q + 1 << ": ";
        forn (q1, Q) {
            int S, T;
            cin >> S >> T;
            --S;
            --T;
            forn (i, n) {
                d[i] = 1e20;
            }
            d[S] = 0;
            forn (i, n - 1) {
                for (int j = i + 1; j < n; ++j) {
                    if (a[j] - a[i] > e[i] + 1e-7) {
                        break;
                    }
                    d[j] = min(d[j], d[i] + (a[j] - a[i]) / s[i]);
                }
            }
            cout << fixed << d[T];
            if (q1 < Q - 1) {
                cout << " ";
            }
        }
        cout << endl;
    }
    return 0;
}

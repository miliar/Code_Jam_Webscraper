#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <queue>
#define MAXN 55
#define MAXR 1000010

using namespace std;

int n,p;
long long r[MAXN];

int main() {
    int T;
    cin >> T;
    for (int TC = 1; TC <= T; TC++) {
        priority_queue<pair<int,int> > a[MAXN],b[MAXN];

        cin >> n >> p;
        cerr << TC << ": " << n << ' ' << p << endl;
        for (int i = 0; i < n; i++) {
            cin >> r[i];
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < p; j++) {
                long long q;
                cin >> q;
                int lo = -1, hi = -1;
                for (int x = 1; x < MAXR; x++) {
                    if (9 * x * r[i] <= 10 * q && 10 * q <= 11 * x * r[i]) {
                        if (lo == -1) lo = x;
                        hi = x;
                    }
                }
                if (lo == -1) continue;
                a[i].push(make_pair(-lo, hi));
            }
        }

        int ans = 0;
        for (int x = 1; x < MAXR; x++) {
            int minsz = MAXN;
            for (int i = 0; i < n; i++) {
                while (!a[i].empty() && -a[i].top().first == x) {
                    int lo = -a[i].top().first;
                    int hi = a[i].top().second;
                    a[i].pop();
                    b[i].push(make_pair(-hi, lo));
                }
                while (!b[i].empty() && -b[i].top().first < x) b[i].pop();
                minsz = min(minsz, (int)b[i].size());
            }
            ans += minsz;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < minsz; j++) b[i].pop();
            }
        }

        cout << "Case #" << TC << ": ";
        cout << ans << '\n';
    }
}

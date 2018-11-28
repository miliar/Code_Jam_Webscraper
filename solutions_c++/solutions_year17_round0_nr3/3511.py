#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

const int maxN = 1010;

#define foru(i, l, r) for (int i = l; i <= r; ++i)
#define ford(i, r, l) for (int i = r; i >= l; --i)
#define repu(i, r) for (int i = 0; i < r; ++i)
#define ll long long
#define F first
#define S second
#define mp make_pair

ll a[10], c[10], n, k, res1, res2;
pair < int, int > b[10];
int nn, test;

void split() {
    int tt = 0;
    foru(i, 1, nn) {
        b[++tt] = mp((a[i] - 1) / 2, c[i]);
        b[++tt] = mp((a[i] - 1) - (a[i] - 1) / 2, c[i]);
    }
    sort(b + 1, b + tt + 1);
    nn = 1;
    a[nn] = b[1].F;
    c[nn] = b[1].S;
    foru(i, 2, tt) {
        if (b[i].F == a[nn]) c[nn] += b[i].S;
        else { a[++nn] = b[i].F; c[nn] = b[i].S; }
    }
}

int main() {
    cin >> test;
    foru(t, 1, test) {
        cin >> n >> k;
        int h = 1;
        ll num = 1;
        a[1] = n;
        c[1] = 1;
        nn = 1;
        while (k) {
            //cout << nn << endl;
            //foru(i, 1, nn) cout << a[i] << " " << c[i] << endl;
            //cout << "DEBUG" << endl;
            if (a[1] == 0) { res1 = res2 = 0; break; }
            ford(i, nn, 1) {
                if (a[i] == 0) continue;
                if (k <= c[i]) {
                    res1 = max((a[i] - 1) / 2, (a[i] - 1) - ((a[i] - 1) / 2));
                    res2 = min((a[i] - 1) / 2, (a[i] - 1) - ((a[i] - 1) / 2));
                    k = 0;
                    break;
                }
                else k -= c[i];
            }
            if (k == 0) break;
            split();
        }
        cout << "Case #" << t << ": " << res1 << " " << res2 << endl;
    }
}

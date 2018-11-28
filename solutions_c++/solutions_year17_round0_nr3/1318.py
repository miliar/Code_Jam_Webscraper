#include <iostream>

using namespace std;
typedef long long ll;

int main() {
    freopen("/Users/vino/Desktop/C-large.in", "r", stdin);
    freopen("/Users/vino/Desktop/C-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        printf("Case #%d: ", cas);
        ll n, k;
        cin >> n >> k;
        ll cnt = 1, a, b;
        while (true) {
            if (k <= cnt) {
                n -= cnt;
                ll lower = n / cnt;
                ll mxer = lower + 1;
                ll c = (n - lower * cnt);
                if (k > c) {
                    b = lower / 2;
                    a = lower - b;
                } else {
                    b = mxer / 2;
                    a = mxer - b;
                }
                break;
            }
            n -= cnt;
            k -= cnt;
            cnt *= 2;

        }
        cout << a << " " << b << endl;

    }

    return 0;
}
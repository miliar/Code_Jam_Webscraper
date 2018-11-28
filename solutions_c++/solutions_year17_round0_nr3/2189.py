#include <iostream>

using namespace std;


int main() {
    freopen("/Users/philip/Downloads/C-large.in", "r", stdin);
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        long long n, k;
        cin >> n >> k;
        k--;
        long long m, a, b;
        m = n;
        a = 0;
        b = 1;
        while (k > 0) {
            //cout << k << ' ' << m << ' ' << a << ' ' << b << '\n';
            if (b > k) {
                k = 0;
                break;
            }
            long long c = 0, d = 0;
            k -= b;
            d = b;
            if ((m - 1) % 2 == 0) {
                d += b;
            }
            else {
                c += b;
            }
            if (a > k) {
                k = 0;
                b = 0;
                break;
            }
            k -= a;
            c += a;
            if ((m - 2) % 2 == 0) {
                c += a;
            }
            else {
                d += a;
            }
            a = c;
            b = d;
            m = m / 2;
        }
        cout << "Case #" << i + 1 << ": ";
        if (b > 0) {
            cout << m / 2 << ' ' << (m - 1) / 2 << '\n';
        }
        else {
            cout << (m - 1) / 2 << ' ' << (m - 2) / 2 << '\n';
        }
    }
}

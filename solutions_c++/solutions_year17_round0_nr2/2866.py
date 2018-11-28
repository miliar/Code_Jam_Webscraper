#include <iostream>
#include <cstdio>
using namespace std;

int T;

void read() {
    cin >> T;
}

void solve() {
    unsigned long long x, transport, result, pow;
    for (int i = 0; i < T; ++i) {
        cin >> x;
        result = 0;
        pow = 1;
        transport = 0;
        while (x > 9) {
            x -= transport;
            transport = 0;
            if (x % 10 < x / 10 % 10) {
                result = 9 * pow;
                for (unsigned long long j = pow / 10; j > 0; j /= 10) {
                    result += 9 * j;
                }
                transport = 1;
            } else {
                result += x % 10 * pow;
            }
            x /= 10;
            pow *= 10;
        }
        x -= transport;
        if (x) {
            result += x * pow;
        }
        cout << "Case #" << i + 1 << ": " << result << endl;
    }
}

int main() {
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
    read();
    solve();
    return 0;
}

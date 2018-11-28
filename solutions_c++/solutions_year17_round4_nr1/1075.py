#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;

int x[10];

int main() {
    ios_base::sync_with_stdio(false);
    int T, N, P;
    cin >> T;
    for (int times = 1; times <= T; ++times) {
        cin >> N >> P;
        memset(x, 0, sizeof(x));
        for (int i = 0; i < N; ++i) {
            int a;
            cin >> a;
            ++x[a % P];
        }

        cout << "Case #" << times << ": ";
        if (P == 2) {
            cout << x[0] + (x[1] + 1) / 2 << endl;
        } else
        if (P == 3) {
            int ans = x[0];
            if (x[1] > x[2]) {
                ans += x[2];
                x[1] = x[1] - x[2];
                cout << ans + (x[1] + 2) / 3 << endl;
            } else {
                ans += x[1];
                x[2] = x[2] - x[1];
                cout << ans + (x[2] + 2) / 3 << endl;
            }
        } else {
            int ans = x[0];
            if (x[2] % 2 == 0) {
                ans += x[2] / 2;
                x[2] = 0;
            } else {
                ans += x[2] / 2;
                x[2] = 1;
            }

            if (x[1] > x[3]) {
                ans += x[3];
                x[1] -= x[3];
                if (x[2] == 0) {
                    ans += (x[1] + 3) / 4;
                } else {
                    ans += 1;
                    if (x[1] >= 2) {
                        x[1] -= 2;
                        ans += (x[1] + 3) / 4;
                    }
                }
            } else {
                ans += x[1];
                x[3] -= x[1];
                if (x[2] == 0) {
                    ans += (x[3] + 3) / 4;
                } else {
                    ans += 1;
                    if (x[3] >= 2) {
                        x[3] -= 2;
                        ans += (x[3] + 3) / 4;
                    }
                }
            }
            cout << ans << endl;
        }
    }
    return 0;
}
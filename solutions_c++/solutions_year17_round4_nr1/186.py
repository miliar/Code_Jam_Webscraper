#include <cstdint>
#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;

void solve() {
    int N, P;
    int remainder[4];
    for (int i = 0; i < 4; i++) remainder[i] = 0;

    cin >> N >> P;
    int ans = 0;
    for (int i = 0; i < N; i++) {
        int g;
        cin >> g;
        if (g % P == 0) {
            ans++;
            continue;
        } else {
            remainder[g % P]++;
        }
    }

    if (P == 2) {
        while (remainder[1] > 0) {
            remainder[1] -= 2;
            ans++;
        }
    } else if (P == 3) {
        while (remainder[1] + remainder[2] > 0) {
            if (remainder[1] > 0 && remainder[2] > 0) {
                remainder[1]--;
                remainder[2]--;
                ans++;
            } else if (remainder[1] > 0) {
                remainder[1] -= 3;
                ans++;
            } else {
                remainder[2] -= 3;
                ans++;
            }
        }
    } else {
        while (remainder[1] + remainder[2] + remainder[3] > 0) {
            if (remainder[1] > 0 && remainder[3] > 0) {
                remainder[1]--;
                remainder[3]--;
                ans++;
            } else if (remainder[2] > 1) {
                remainder[2] -= 2;
                ans++;
            } else if (remainder[1] > 1 && remainder[2] > 0) {
                remainder[1] -= 2;
                remainder[2]--;
                ans++;
            } else if (remainder[3] > 1 && remainder[2] > 0) {
                remainder[3] -= 2;
                remainder[2]--;
                ans++;
            } else if (remainder[1] > 3) {
                remainder[1] -= 4;
                ans++;
            } else if (remainder[3] > 3) {
                remainder[3] -= 4;
                ans++;
            } else {
                ans++;
                break;
            }
        }
    }
    cout << ans << endl;
}

int main() {
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; testcase++) {
        cout << "Case #" << testcase << ": ";
        solve();
    }
    return 0;
}

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

int N, P;
uint64_t R[100];
uint64_t Q[100][100];

void solve() {
    cin >> N >> P;
    for (int i = 0; i < N; i++) cin >> R[i];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < P; j++) {
            cin >> Q[i][j];
        }
        sort(&Q[i][0], &Q[i][P]);
    }

    int avail[100];
    memset(avail, 0, sizeof(avail));
    int ans = 0;
    uint64_t k = 1;
    while (k <= 1100000) {
        int match[100];
        bool all_found = true;
        for (int j = 0; j < N; j++) {
            bool found = false;
            int curr = avail[j];
            while (curr < P) {
                if (Q[j][curr] * 10 >= R[j] * k * 9 && Q[j][curr] * 10 <= R[j] * k * 11) {
                    found = true;
                    break;
                }
                curr++;
            }
            if (found) {
                match[j] = curr;
            } else {
                all_found = false;
                break;
            }
        }
        if (all_found) {
            ans++;
            bool all_used = false;
            for (int j = 0; j < N; j++) {
                avail[j] = match[j] + 1;
                if (avail[j] >= P) all_used = true;
            }
            if (all_used) break;
        } else {
            k++;
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

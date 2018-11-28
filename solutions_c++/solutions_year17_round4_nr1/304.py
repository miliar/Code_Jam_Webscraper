
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int N, P;
int g[200];

int solve() {
    cin >> N >> P;
    vector <int> cnt(P);
    for (int i = 0; i < N; i++) {
        cin >> g[i];
        cnt[g[i] % P]++;
    }
    int total = cnt[0];
    if (P == 2) {
        total += (cnt[1] + 1) / 2;
    }
    else if (P == 3) {
        int add = min(cnt[1], cnt[2]);
        total += add;
        cnt[1] -= add;
        cnt[2] -= add;
        total += (cnt[1] + cnt[2] + 2) / 3;
    }
    else {
        int add = min(cnt[1], cnt[3]);
        total += add;
        cnt[1] -= add;
        cnt[3] -= add;

        int add2 = cnt[2] / 2;
        total += add2;
        cnt[2] -= 2 * add2;

        int left = cnt[1] + cnt[3];
        if (cnt[2] == 1) {
            if (left >= 2) {
                cnt[2]--;
                left -= 2;
                total++;
            }
            else {
                total++;
                left = 0;
            }
        }
        total += (left + 3) / 4;
    }
    return total;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": " << solve() << endl;
    }
}

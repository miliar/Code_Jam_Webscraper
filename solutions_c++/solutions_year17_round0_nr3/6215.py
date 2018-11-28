#include <bits/stdc++.h>

using namespace std;

const int MAX_N = 1e6 + 10;

int tc, n, k;
int cnt[MAX_N];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> tc;
    for (int t = 0; t < tc; t++) {
        cout << "Case #" << t + 1 << ": ";
        cin >> n >> k;
        fill(cnt, cnt + n + 1, 0);
        cnt[n] = 1;
        int pos = n;
        for (int i = 0; i < k; i++) {
            while (!cnt[pos]) {
                pos--;
            }
            int r = pos;
            if (r % 2) {
                cnt[r / 2] += 2;
                if (i == k - 1) {
                    cout << r / 2 << " " << r / 2 << "\n";
                }
            } else {
                cnt[r / 2]++;
                cnt[r / 2 - 1]++;
                if (i == k - 1) {
                    cout << r / 2 << " " << r / 2 - 1 << "\n";
                }
            }
            cnt[pos]--;
        }
    }
}

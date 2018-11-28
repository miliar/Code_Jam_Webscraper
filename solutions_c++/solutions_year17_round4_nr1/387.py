#include <bits/stdc++.h>

using namespace std;

int main() {
    ifstream in("input.txt");
    ofstream out("output.txt");
    cin.rdbuf(in.rdbuf());
    cout.rdbuf(out.rdbuf());
    int T;
    cin >> T;
    for (int test = 1; test <= T; test++) {
        cout << "Case #" << test << ": ";
        int n, p;
        cin >> n >> p;
        vector<int> cnt(p, 0);
        for (int i = 0; i < n; ++i) {
            int g;
            cin >> g;
            ++cnt[g % p];
        }
        if (p == 2) {
            cout << cnt[0] + cnt[1] / 2 + (cnt[1] % 2 > 0) << endl;
        }
        else if (p == 3) {
            int left = abs(cnt[1] - cnt[2]);
            cout << cnt[0] + min(cnt[1], cnt[2]) + left / 3 + (left % 3 > 0) << endl;
        }
        else if (p == 4) {
            int left1 = abs(cnt[1] - cnt[3]), left = 0;
            if (cnt[2] % 2 && left1 > 1) {
                left1 -= 2;
                --cnt[2];
                ++left;
            }
            if (cnt[2] % 2 == 0)
                left += left1 / 4 + (left1 % 4 > 0);
            else
                ++left;
            cout << cnt[0] + min(cnt[1], cnt[3]) + cnt[2] / 2 + left << endl;
        }
    }
}
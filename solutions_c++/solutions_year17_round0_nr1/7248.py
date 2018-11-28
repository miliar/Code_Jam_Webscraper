#include <bits/stdc++.h>

using namespace std;

void Run(int number) {
    string S;
    int i, j, n, k, ans = 0;
    cin >> S >> k;
    n = S.size();
    for (i = 0; i <= n - k; ++i) {
        if (S[i] == '-') {
            for (j = 0; j < k; ++j) {
                if (S[i + j] == '+') S[i + j] = '-';
                else S[i + j] = '+';
            }
            ans++;
        }
    }
    bool check = 1;
    for (i = 0; i < S.size(); ++i) check *= (S[i] == '+');
    cout << "Case #" << number << ": ";
    if (check == 1) {
        cout << ans << "\n";
    }
    else cout << "IMPOSSIBLE\n";
    return;
}

int main() {
    int i, t;
    cin >> t;
    for (i = 1; i <= t; ++i) {
        Run(i);
    }
    return 0;
}

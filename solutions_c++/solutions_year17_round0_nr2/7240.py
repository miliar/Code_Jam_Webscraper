#include <bits/stdc++.h>

using namespace std;

void Run(int number) {
    string S, ans;
    cin >> S;
    cout << "Case #" << number << ": ";
    int i, left, j, n = S.size();
    i = 0;
    while (i < n) {
        left = i;
        while (i + 1 < n && S[i] == S[i + 1]) {
            ++i;
        }
        if (i + 1 < n && S[i] > S[i + 1]) break;
        if (i + 1 >= n) {
            i = n;
            break;
        }
        ++i;
    }
    if (i == n) {
        cout << S << "\n";
        return;
    }
    char c = S[left];
    if (c == '1') {
        for (i = 0; i < left; ++i) {
            ans += S[i];
        }
        for (i = left; i < n - 1; ++i) {
            ans += '9';
        }
        cout << ans << "\n";
        return;
    }
    for (i = 0; i < left; ++i) {
        ans += S[i];
    }
    ans += S[i] - 1;
    for (i = left + 1; i < n; ++i) {
        ans += '9';
    }
    cout << ans << "\n";
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

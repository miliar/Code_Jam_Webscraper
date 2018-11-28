#include <bits/stdc++.h>

using namespace std;

typedef long long li;

void solve(int);

int main() {
    ios_base::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        solve(i + 1);
    }
}

void solve(int test_case) {
    string s;
    int k;
    cin >> s >> k;
    int res = 0;
    for (int i = 0; i < (int)s.length(); i++) {
        if (s[i] == '-') {
            res++;
            for (int j = i; j < i + k; j++) {
                if (j >= (int)s.length()) {
                    cout << "Case #" << test_case << ": IMPOSSIBLE" << endl;
                    return;
                }
                if (s[j] == '-') {
                    s[j] = '+';
                } else {
                    s[j] = '-';
                }
            }
        }
    }
    cout << "Case #" << test_case << ": " << res << endl;
}

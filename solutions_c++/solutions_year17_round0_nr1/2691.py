#include <bits/stdc++.h>

using namespace std;

char r(char s) {
    if (s == '-') return '+';
    return '-';
}
void solve(int x) {
    cout << "Case #" << x << ':' << ' ';
    string s;
    int k;
    cin >> s >> k;
    int n = s.size();
    int cnt = 0;
    for (int i = 0; i + k <= n; i++) {
        if (s[i] == '-') {
            cnt++;
            for (int j = i; j < i + k; j++) {
                s[j] = r(s[j]);
            }
        }
    }
    for (int i = 0; i < n; i++) {
        if (s[i] == '-') {
            cout << "IMPOSSIBLE\n";
            return ;
        }
    }
    cout << cnt << '\n';
}
int main() {
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) solve(i);
    return 0;
}

#include <bits/stdc++.h>

using namespace std;

bool solve(int i, int digit[], int prev_digit, int n)
{
    if (i >= n) {
        return true;
    }
    if (digit[i] < prev_digit) {
        return false;
    }
    bool suc = solve(i + 1, digit, digit[i], n);
    if (suc) {
        return true;
    }
    if (digit[i] == prev_digit) {
        return false;
    }
    digit[i]--;
    for (int j = i + 1; j < n; j++) {
        digit[j] = 9;
    }
    return true;
}

int main()
{
    ios_base::sync_with_stdio(false);
    freopen("B-large.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int t;
    cin >> t;
    for (int x = 1; x <= t; x++) {
        char s[20];
        cin >> s;
        int n = strlen(s);
        int digit[n];
        for (int i = 0; i < n; i++) {
            digit[i] = (int)s[i] - (int)'0';
        }
        solve(0, digit, 0, n);
        int i = 0;
        while (digit[i] == 0) {
            i++;
        }
        cout << "Case #" << x << ": ";
        while (i < n) {
            cout << digit[i];
            i++;
        }
        cout << endl;
    }
    return 0;
}

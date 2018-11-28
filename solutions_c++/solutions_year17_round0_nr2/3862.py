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

li calc(li n) {
    string s = to_string(n);
    li res = 0;
    for (int i = 1; i < (int)s.length(); i++) {
        if (s[i] < s[i - 1]) {
            int j = i - 1;
            while (s[j] == s[j - 1]) {
                j--;
                res /= 10;
                if (j == 0) {
                    break;
                }
            }
            res = res * 10LL + s[j] - '0' - 1; 
            for (int k = j + 1; k < (int)s.length(); k++) {
                res = res * 10LL + 9;
            }
            return res;
        }
        res = res * 10LL + s[i - 1] - '0';
    }
    return n;
}

void solve(int test_case) {
    li n;
    cin >> n;
    cout << "Case #" << test_case << ": " << calc(n) << endl;
}

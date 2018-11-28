#include <bits/stdc++.h>

#define sz(s) ((int) s.size ())
#define all(s) s.begin (), s.end ()

using namespace std;

/**

1 => 9
2 => 9 + 8 + 7 + ... + 1 = 45
3 =>

dp[n][d] = sum (dp[n - 1][nd], d <= nd)

**/

const int N = 29;
const int D = 19;

int dp[N][D];

bool tidy (int x) {
    vector<int> d;
    for (; x > 0; x /= 10) {
        d.push_back (x % 10);
    }
    reverse (all (d));
    return is_sorted (all (d));
}
int slowGet (int r) {
    int cnt = 0;
    for (int i = 1; i <= r; i++) {
        cnt += tidy (i);
    }
    return cnt;
}
int main () {
    #define name "B-large"
    freopen (name".in", "r", stdin);
    freopen (name".out", "w", stdout);
    for (int digit = 1; digit <= 9; digit++) {
        dp[1][digit] = 1;
    }
    for (int len = 2; len <= 19; len++) {
        for (int digit = 0; digit <= 9; digit++) {
            for (int nextDigit = digit; nextDigit <= 9; nextDigit++) {
                dp[len][digit] += dp[len - 1][nextDigit];
            }
        }
    }
    int t; cin >> t;
    for (int tt = 1; tt <= t; tt++) {
        string n; cin >> n;
        int len = sz (n);
        int lastDigit = 0;
        long long cur = 0;
        for (int i = len; i >= 1; i--) {
            int curDigit = n[len - i] - '0';
            if (curDigit < lastDigit) {
                break;
            }
            for (int digit = lastDigit; digit < curDigit + (i == 1); digit++) {
                cur += dp[i][digit];
            }
            lastDigit = curDigit;
//            cerr << cur << endl;
        }
//        cerr << "Number of tidy numbers from 1 to n is " << cur << " == " << slowGet (atoi (n.c_str ())) << " " << atoi (n.c_str ()) << endl;
        lastDigit = 0;
        string ans = "";
        for (int i = len; i >= 1; i--) {
            for (int digit = lastDigit; digit <= 9; digit++) {
                if (cur - dp[i][digit] > 0) {
                    cur -= dp[i][digit];
//                    cerr << i << " " << digit << " == " << dp[i][digit] << endl;
                } else {
                    if ((ans == "" && digit > 0) || ans != "") {
                        ans += char (digit + '0');
                    }
                    lastDigit = digit;
                    break;
                }
            }
        }
        cout << "Case #" << tt << ": ";
        cout << ans << endl;
    }
    return 0;
}

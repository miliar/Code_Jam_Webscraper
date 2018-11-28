#include <bits/stdc++.h>

using namespace std;
using lld = long long int;

bool tidy_number(lld n) {
        int last_digit = 10;
        while(n) {
                int curr_digit = n % 10;
                if( curr_digit > last_digit ) {
                        return false;
                } else {
                        last_digit = curr_digit;
                        n /= 10;
                }
        }
        return true;
}

int main() {
        ios_base::sync_with_stdio(false);
        int tests;
        cin >> tests;
        for(int tc = 1; tc <= tests; ++tc) {
                string s;
                cin >> s;
                lld ans = s[0] - '0';
                if(tidy_number(stoll(s))) {
                        ans = stoll(s);
                } else {
                        for(int i = 0; s[i]; ++i) {
                                int curr_digit = s[i] - '0';
                                if(curr_digit) {
                                        string r = s;
                                        r[i]--;
                                        for(int j = i + 1; r[j]; ++j) {
                                                r[j] = '9';
                                        }
                                        lld n = stoll(r);
                                        if(tidy_number(n)) {
                                                ans = max(ans, n);
                                        }
                                }
                        }
                }
                cout << "Case #" << tc << ": " << ans << endl;
        }
        return 0;
}

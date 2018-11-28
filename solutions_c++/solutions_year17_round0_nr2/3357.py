#include<bits/stdc++.h>
using namespace std;
#define LL long long int

int T;
LL N;

string toString(LL n) {
    string ret = "";
    while (n > 0) {
        int cur = n % 10;

        ret = (char) (cur + '0') + ret;

        n /= 10;
    }

    return ret;
}

int main() {
    cin >> T;
    for (int cases = 1; cases <= T; cases++) {
        cin >> N;

        string S = toString(N);
        string ans = "";
        bool triggered = false;

        for (int i = 0; i < S.length(); i++) {
            if (triggered) {
                ans += '9';
                continue;
            }

            for (char digit = '9'; digit >= '0'; digit--) {
                bool can = true;
                for (int j = i; j < S.length(); j++) {
                    if (S[j] > digit)
                        break;

                    if (S[j] < digit)
                        can = false;
                }

                if (can) {
                    if (digit < S[i])
                        triggered = true;

                    ans += digit;
                    break;
                }
            }
        }

        cout << "Case #" << cases << ": ";
        
        bool nonzero = false;
        for (int i = 0; i < ans.length(); i++) {
            if (ans[i] != '0')
                nonzero = true;

            if (nonzero)
                cout << ans[i];
        }

        cout << endl;
    }
}

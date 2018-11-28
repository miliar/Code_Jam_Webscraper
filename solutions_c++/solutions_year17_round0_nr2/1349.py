#include <bits/stdc++.h>
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
typedef long long ll;
typedef long double ld;
using namespace std;

int main() {
    //ios_base::sync_with_stdio(false)
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        long long x;
        cin >> x;
        string s = "";
        while(x > 0) {
            s += '0' + x % 10;
            x /= 10;
        }
        reverse(s.begin(), s.end());
        string ans = "";
        bool ok = true;
        for(int i = 0; i < (int)s.size(); i++) {
            for(int j = 9; j >= (ans.size() ? ans.back() - '0' : 1); j--) {
                string temp = ans;
                for(int k = i; k < (int)s.size(); k++)
                    temp += '0' + j;
                if(temp <= s) {
                    ans += '0' + j;
                    break;
                }
            }
            if(i + 1 != (int)ans.size())
                ok = false;
        }
        cout << "Case #" << t << ": ";
        if(ok && ans <= s)
            cout << ans << "\n";
        else {
            for(int i = 1; i < (int)s.size(); i++)
                cout << "9";
            cout << "\n";
        }
    }
    return 0;
}
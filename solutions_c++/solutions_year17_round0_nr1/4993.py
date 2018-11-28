#include <iostream>
#include <string.h>
#include <map>
using namespace std;

int t;
#define rr 1000000007

char flip(char now) {
    if (now == '+')
        return '-';
    return '+';
}

void solve () {
    string s;
    int k;
    cin >> s;
    int len = s.size();
    cin >> k;
    int ans = 0;
    for (int i=0; i<len; i++) {
        if (s[i] == '+')
            continue;
        if (i + k > len) {
            ans = -1;
            break;
        }
        for (int j=i; j<i+k; j++)
            s[j] = flip (s[j]);
        ans ++;
    }
    if (ans == -1)
        cout << "IMPOSSIBLE\n";
    else
        cout << ans << endl;
}

int main () {
    cin >> t;
    int tmp  = 1;
    while (t--) {
        cout << "Case #" << tmp << ": ";
        solve();
        tmp ++;
    }
                        
}
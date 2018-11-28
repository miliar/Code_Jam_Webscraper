#include<bits/stdc++.h>
using namespace std;

int main(void)
{
    int t, ti, i, j, k, n;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin >> t;
    string s;
    for (ti = 1; ti <= t; ti++) {
        cin >> s >> k; n = 0;
        for (i = 0; i+k-1 < s.size(); i++) {
            if (s[i]=='-') {
                for (j = 0; j < k; j++) {
                    if (s[i+j]=='-') s[i+j] = '+';
                    else s[i+j] = '-';
                }
                n++;
            }
        }
        for ( ; i < s.size(); i++) if (s[i]=='-') break;
        if (i==s.size()) cout << "Case #" << ti << ": " << n << endl;
        else cout << "Case #" << ti << ": IMPOSSIBLE" << endl;
    }



    return 0;
}

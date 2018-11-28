#include <bits/stdc++.h>

using namespace std;

int main()
{

    int t;
    cin >> t;

    for(int o = 1; o <= t; o ++) {

        int k;
        string s;
        cin >> s >> k;

        int n = s.size(), lim = n - k;
        int nmb = 0;
        for(int i = 0; i <= lim; i ++) {
            if(s[i] == '-') {
                nmb ++;
                for(int j = 1, now = i; j <= k; j ++, now ++) {
                    if(s[now] == '-') s[now] = '+';
                    else s[now] = '-';
                }
            }
        }

        bool right = true;
        for(int i = 0; i < n; i ++) {
            if(s[i] == '-') right = false, i = n;
        }

        if(right == true) cout << "Case #" << o << ": " << nmb;
        else cout << "Case #" << o << ": IMPOSSIBLE";
        cout << "\n";
    }

    return 0;
}

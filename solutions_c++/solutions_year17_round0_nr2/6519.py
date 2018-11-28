#include<bits/stdc++.h>
using namespace std;


int main(void)
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t, ti, i, j;
    cin >> t;
    string s, p;
    for (ti = 1; ti <= t; ti++) {
        cin >> s;
        for (i = 0; i+1 < s.size(); i++) {
            if (s[i]>s[i+1]) {
                for (j = i-1; j >= 0; j--) if (s[i]!=s[j]) break;
                j++;
                s[j] = s[j] - 1;
                for (j++; j < s.size(); j++) s[j] = '9';
                break;
            }
        }
        for (i = 0; i < s.size(); i++) if (s[i]-'0') break;
        p = "";
        for ( ; i < s.size(); i++) p += s[i];
        cout << "Case #" << ti << ": " << p << endl;
    }



    return 0;
}

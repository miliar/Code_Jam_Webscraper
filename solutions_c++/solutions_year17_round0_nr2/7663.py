#include<bits/stdc++.h>
using namespace std;
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    cin >> T;
    for(int cs = 1; cs <= T; cs++) {
        string s;
        cin >> s;
       // cout << s << endl;
        printf("Case #%d: ", cs);
        int len = (int)s.size(), i, j, k;
        for(i = 0; s[i]; i++) {
            if(i && (s[i] < s[i - 1])) break;
        }
        if(!s[i]) {
            cout << s << endl;
            continue;
        }
        k = i - 1;
        for(i = k - 1; i >= 0; i--) {
            if(s[i] != s[i + 1]) break;
        }
        j = i;
        s[j + 1]--;

       // cout << j << " " << k << endl;

        for(i = j + 2; s[i]; i++)s[i] = '9';
        i = 0;

        while(s[i] == '0') i++;
        for(; s[i]; i++) printf("%c", s[i]);
        printf("\n");
    }
    return 0;
}


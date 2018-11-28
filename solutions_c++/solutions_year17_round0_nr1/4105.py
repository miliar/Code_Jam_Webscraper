#include <bits/stdc++.h>
using namespace std;
char s[1005];
int main(){

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);int t; cin >> t;
    for (int T = 1; T <= t; T++){
        cin >> s;
        int k; cin >> k;
        int len = strlen(s);
        int ans = 0, i;
        for (i = 0; i < len - k + 1; i++){
            if (s[i] == '-'){
                ans++;
                for (int j = i; j < i + k; j++){
                    if (s[j] == '-') s[j] = '+';
                    else s[j] = '-';
                }
            }
        }
        for (; i < len; i++){
            if (s[i] == '-') ans = -1;
        }
        if (ans != -1) printf("Case #%d: %d\n", T, ans);
        else printf("Case #%d: IMPOSSIBLE\n", T);
    }
    return 0;
}

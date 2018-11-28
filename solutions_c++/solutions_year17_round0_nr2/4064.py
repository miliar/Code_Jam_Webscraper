#include <bits/stdc++.h>
using namespace std;
char s[1005];
int main(){

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);int t; cin >> t;
    for (int T = 1; T <= t; T++){
        cin >> s;
        int len = strlen(s);
        for (int i = 0; i < len; i++){
            bool chk = 1;
            for (int j = i + 1; j < len; j++){
                if (s[j] > s[i]) {break;}
                else if (s[j] < s[i]) {chk = 0; break;}
            }
            if (!chk){
                s[i]--;
                for (int j = i + 1; j < len; j++){
                    s[j] = '9';
                }
                break;
            }
        }
        if (s[0] == '0'){
            for (int i = 1; i < len; i++){
                s[i - 1] = s[i];
            }
            s[len - 1] = 0;
        }
        printf("Case #%d: %s\n", T, s);
    }
    return 0;
}

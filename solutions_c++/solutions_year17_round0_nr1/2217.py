#include <bits/stdc++.h>

using namespace std;

int main(){

    int t;
    scanf ("%d", &t);
    int cc = 1;
    while (t--){
        string s;
        cin >> s;
        int k;
        scanf ("%d", &k);
        int ans = 0;
        for (int i = 0; i < (int)s.size() - k + 1; i++){
            if (s[i] == '-'){
                for (int j = 0; j < k; j++){
                    if (s[i+j] == '-') s[i+j] = '+'; else s[i+j] = '-';
                }
                ans++;
            }
        }

        for (int i = 0; i < s.size(); i++){
            if (s[i] == '-'){
                ans = -1;
            }
        }
        printf ("Case #%d: ", cc++);
        if (ans == -1) printf ("IMPOSSIBLE\n"); else printf ("%d\n", ans);
    }

    return 0;
}

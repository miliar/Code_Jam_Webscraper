#include<bits/stdc++.h>
using namespace std;

typedef long long LL;

char s[1024];

int main(){
    freopen("2.txt", "r", stdin);
    freopen("1.txt", "w", stdout);
    int T; scanf("%d", &T);
    for(int cas = 1; cas <= T; cas ++){
        int k; scanf("%s%d", s, &k);
        int ans = 0;
        for(int i = 0; s[i + k - 1]; i ++){
            if(s[i] == '-'){
                for(int j = i; j < i + k; j ++){
                    if(s[j] == '-') s[j] = '+';
                    else s[j] = '-';
                }
                ans ++;
            }
        }
        bool ok = 1;
        printf("Case #%d: ", cas);
        for(int i = 0; s[i]; i ++) if(s[i] != '+') ok = 0;
        if(!ok) puts("IMPOSSIBLE");
        else printf("%d\n", ans);
    }
    return 0;
}

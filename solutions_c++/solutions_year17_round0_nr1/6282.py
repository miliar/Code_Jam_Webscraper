#include <bits/stdc++.h>
using namespace std;
char s[1010];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    scanf("%d", &t);
    int cas = 0;
    while(t --) {
        int k;
        scanf("%s%d", s, &k);
        int n = strlen(s);
        int flag = 1;
        int cnt = 0;
        for(int i = 0; s[i]; i++) {
            if(s[i] == '-') {
                if(i+k > n) { flag = 0; break;}
                for(int j = i; j < i+k; j ++) {
                    if(s[j] == '-') s[j] = '+';
                    else s[j] = '-';
                }
                cnt++;
            }
        }
        printf("Case #%d: ", ++cas);
        if(flag) {
            printf("%d\n", cnt);
        } else puts("IMPOSSIBLE");
    }
}

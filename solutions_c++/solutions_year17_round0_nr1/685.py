#include <bits/stdc++.h>

using namespace std;

char s[1005];
int a[1005];
int n, k;

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int kase=1; kase<=T; kase++) {
        scanf("%s%d", s, &k);
        n = strlen(s);
        for(int i = 0; i < n; i ++) {
            if(s[i] == '+') a[i] = 1;
            else a[i] = 0;
        }
        int cnt = 0;
        for(int i = 0; i < n; i ++) {
            if(a[i] == 1) continue;
            else {
                if(i + k > n) {
                    cnt = -1;
                    break;
                }
                for(int j = i; j < i + k; j ++) {
                    a[j] = 1 - a[j];
                }
                cnt ++;
            }
        }
        printf("Case #%d: ", kase);
        if(cnt == -1) printf("IMPOSSIBLE\n");
        else printf("%d\n", cnt);
    }
    return 0;
}

#include <bits/stdc++.h>
using namespace std;
int n, f;
char s[1005];
int main() {
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    scanf("%d", &n);
    for (int i=0;i<n;i++) {
        scanf("%s %d", s, &f);
        int len = strlen(s), ans = 0;
        for (int j=0;j<=len-f;j++) {
            if (s[j]=='-') {
                ans++;
                for (int k=j;k<j+f;k++) {
                    if (s[k]=='+') s[k]='-';
                    else s[k]='+';
                }
            }
        }
        bool ok = 1;
        for (int j=0;j<len;j++) {
            if (s[j]=='-') ok = 0;
        }
        printf("Case #%d: ", i+1);
        if (ok) printf("%d\n", ans);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}

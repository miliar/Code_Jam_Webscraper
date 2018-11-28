#include <bits/stdc++.h>
using namespace std;
int n;
char s[25];
int main() {
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    scanf("%d", &n);
    for (int i=0;i<n;i++) {
        scanf("%s", s);
        int len = strlen(s);
        for (int j=len-1;j>=1;j--) {
            if (s[j]<s[j-1]) {
                s[j-1]--;
                for (int k=j;k<len;k++) s[k]='9';
            }
        }
        printf("Case #%d: ", i+1);
        int x;
        for (int j=0;j<len;j++) if (s[j]!='0') {
            x = j;
            break;
        }
        for (int j=x;j<len;j++) printf("%c", s[j]);
        printf("\n");
    }
    return 0;
}

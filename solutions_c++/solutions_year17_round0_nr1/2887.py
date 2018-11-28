#include <bits/stdc++.h>

using namespace std;

char s[1050];

int main() {
    int t;
    scanf("%d", &t);
    for(int te=1;te<=t;te++) {
        int k;
        scanf("%s", s);
        scanf("%d", &k);
        int n = strlen(s);
        int count = 0;
        printf("Case #%d: ", te);
        for(int i=0;i<=n-k;i++) {
            if (s[i] == '-') {
                count++;
                for(int j=0;j<k;j++) {
                    s[i+j] = s[i+j] == '-' ? '+' : '-';
                }
            }
        }
        for(int i=0;i<n;i++) {
            if (s[i] == '-') {
                count = -1;
                printf("IMPOSSIBLE\n");
                break;
            }
        }
        if (count >= 0) printf("%d\n", count);
    }
    return 0;
}


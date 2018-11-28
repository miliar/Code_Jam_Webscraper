#include <bits/stdc++.h>

using namespace std;

char s[50];

void nines(int x) {
    for(int i=0;i<x;i++) printf("9");
    printf("\n");
}

int main() {
    int t;
    scanf("%d", &t);
    for(int k=1;k<=t;k++) {
        scanf("%s", s);
        int mx = s[0] - '0';
        printf("Case #%d: ", k);
        int n = strlen(s);
        for(int i=1; i<n; i++) {
            mx = max(mx, s[i]-'0');
            if (s[i] == '0') {
                if (mx == 1) {
                    mx = -1;
                    nines(n-1);
                    break;
                }
            }
            if (s[i] < s[i-1]) {
                mx = -1;
                s[i-1]--;
                for(int j=i;j<n;j++) s[j] = '9';
                for(int j=i-1;j>=0;j--) {
                    if (s[j] > s[j+1]) {
                        s[j]--;
                        s[j+1] = '9';
                    }
                }
                printf("%s\n", s);
                break;
            }
        }
        if (mx == -1) continue;
        else printf("%s\n", s);
    }
    return 0;
}


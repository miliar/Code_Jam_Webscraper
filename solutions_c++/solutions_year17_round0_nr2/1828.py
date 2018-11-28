#include <bits/stdc++.h>

const int maxn = 20;

int T, n;
char s[maxn];

int main() {
    scanf("%d", &T);
    for (int test = 1; test <= T; test++) {
        scanf(" %s", s);
        n = strlen(s);
        for (int i = n-2; i >= 0; i--) {
            if (s[i] > s[i+1]) {
                s[i]--;
                for (int j = i+1; j < n; j++) {
                    s[j] = '9';
                }
            }
        }
        printf("Case #%d: ", test);
        if (s[0] != '0') {
            printf("%c", s[0]);
        }
        printf("%s\n", s+1);
    }
}


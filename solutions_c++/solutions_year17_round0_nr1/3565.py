#include <bits/stdc++.h>
using namespace std;

int solve(char s[], int k) {
    int l = strlen(s);
    int ans = 0;
    for (int i = 0; i <= l - k; ++i) {
        if (s[i] == '-') {
            for (int j = i + 1; j < i + k; ++j) {
                s[j] = s[j] == '-' ? '+' : '-';
            }
            ++ans;
        }
    }
    for (int i = max(l - k + 1, 0); i < l; ++i) {
        if (s[i] == '-') {
            return -1;
        }
    }
    return ans;
}

int main() {
    int t;
    scanf("%d", &t);
    char s[1007];
    for (int i = 0; i < t; ++i) {
        int k;
        scanf("%s%d", s, &k);
        int ans = solve(s, k);
        printf("Case #%d: ", (i + 1));
        if (ans < 0) {
            printf("IMPOSSIBLE");
        } else {
            printf("%d", ans);
        }
        if (i + 1 < t) {
            printf("\n");
        }
    }
    return 0;
}
#include <bits/stdc++.h>

int main (void) {
    int t;
    char s[1001];
    scanf ("%d", &t);
    for (int c = 1; c <= t; c++) {
        int k;
        scanf ("%s%d", s, &k);
        int l = strlen(s);
        int cnt = 0;
        for (int i = 0; i <= l-k; i++) {
            if (s[i] == '-') {
                cnt++;
                for (int j = i; j < i+k; j++) {
                    s[j] = ((s[j] == '+') ? '-' : '+');
                }
            }
        }
        for (int i = 0; i < l; i++) {
            if (s[i] == '-')    cnt = -1;
        }
        if (cnt == -1)  printf ("Case #%d: IMPOSSIBLE\n", c);
        else    printf ("Case #%d: %d\n", c, cnt);
    }
}

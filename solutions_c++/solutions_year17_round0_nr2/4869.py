#include <bits/stdc++.h>

int main (void) {
    int t;
    char s[20];
    scanf ("%d", &t);
    for (int c = 1; c <= t; c++) {
        scanf ("%s", s);
        int l = strlen(s);
        int st = 0;
        for (int i = 0; i < l-1; i++) {
            if (s[i] > s[i+1]) {
                s[st]--;
                for (int j = st+1; j < l; j++)   s[j] = '9';
                break;
            } else if (s[i] < s[i+1]) {
                st = i+1;
            }
        }
        printf ("Case #%d: %s\n", c, s[0] == '0' ? s+1 : s);
    }
}

#include <stdio.h>
#include <string.h>

int main() {
    char s[222];
    char out[222];
    int tn, cn;
    for (scanf("%d", &tn), cn = 1; cn <= tn; cn++) {
        scanf("%s", s);
        int l = strlen(s);
        while (1) {
            bool ok = true;
            for (int i = 0; i < l - 1; i++) {
                if (s[i] > s[i + 1]) {
                    s[i]--;
                    for (int j = i + 1; j < l; j++) {
                        s[j] = '9';
                    }
                    ok = false;
                    break;
                }
            }
            if (ok) break;
        }
        int st = 0;
        while (s[st] == '0') st++;
        printf("Case #%d: %s\n", cn, s + st);
    }
    return 0;
}

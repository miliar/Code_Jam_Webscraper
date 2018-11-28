#include<stdio.h>
#include<string.h>
int main() {
    int t, k, len, i, j;
    char s[1005];
    scanf("%d", &t);
    for (i = 1; i <= t; i += 1) {
        scanf("%s", s);
        len = strlen(s);
        for (j = len - 1; j > 0; j -= 1) {
            if (s[j] < s[j-1]) {
                s[j-1] -= 1;
                for (k = j; k < len; k += 1) {
                    s[k] = '9';
                }
            }
        }
        j = 0;
        while(s[j] == '0') {
            j += 1;
        }
        printf("Case #%d: ", i);
        while (j < len) {
            printf ("%c", s[j]);
            j += 1;
        }
        printf("\n");
    }
    return 0;
}

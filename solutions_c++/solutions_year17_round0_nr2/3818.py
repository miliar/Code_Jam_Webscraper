#include <stdio.h>
#include <string.h>
int main() {
    char a[20];
    int t, cas = 0;
    scanf("%d", &t);
    while (t--) {
        cas++;
        scanf("%s", a);
        printf("Case #%d: ", cas);
        bool first = true;
        for (int i = 0; i < strlen(a) - 1; ++i) {
            if (a[i] > a[i+1]) {
                a[i]--;
                for (int j = i - 1; j >=0; --j) {
                    if (a[j] > a[j+1]) {
                        a[j+1] = '9';
                        a[j]--;
                    }
                }
                for (int j = i + 1; j < strlen(a); ++j) {
                    a[j] = '9';
                }
                break;
            }
        }
        int i = 0;
        while (a[i] == '0') {
            i++;
        }
        printf("%s\n", a + i);
    }
    return 0;
}

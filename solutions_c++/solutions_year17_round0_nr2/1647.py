#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    int cs = 0;
    char c[50];
    scanf("%d", &t);
    while (t--) {
        cs++;
        scanf("%s", c);
        int n = strlen(c);
        int cur = 0;
        while (cur < n && c[cur] <= c[cur + 1]) {
            cur = cur + 1;
        }
        printf("Case #%d: ", cs);
        if (cur == n - 1) {
            printf("%s\n", c);
        } else {
            int cur2 = cur;
            while (cur2 > 0 && c[cur2] == c[cur2 - 1]) {
                cur2 = cur2 - 1;
            }
            for (int i = 0; i < cur2; i++) {
                printf("%c", c[i]);
            }
            if (cur2 == 0 && c[cur2] == '1') {
            } else {
                printf("%c", c[cur2] - 1);
            }
            for (int i = cur2 + 1; i < n; i++) {
                printf("9");
            }
            printf("\n");

        }
    }
}

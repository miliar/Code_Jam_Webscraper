#include <cstdio>
#include <cstring>

char input[1001];

int main() {
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        int k;
        scanf("%s %d", input, &k);

        int len = strlen(input);
        int flips = 0;
        for (int j = 0; j <= len - k; j++) {
            if (input[j] == '-') {
                flips++;
                for (int l = 0; l < k; l++) {
                    input[j + l] = input[j + l] == '-' ? '+' : '-';
                }
            }
        }

        bool ok = true;
        for (int j = len - k + 1; j < len; j++) {
            if (input[j] == '-') {
                ok = false;
                break;
            }
        }

        if (ok) {
            printf("Case #%d: %d\n", i, flips);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", i);
        }
    }
    return 0;
}
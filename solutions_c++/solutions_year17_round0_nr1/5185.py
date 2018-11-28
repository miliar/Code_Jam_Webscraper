#include <cstdio>
#include <cstring>

#pragma warning(disable:4996)

using namespace std;

char turn(char x) {
    if (x == '+') return '-';
    else return '+';
}

int main() {
    freopen("pancake.in", "r", stdin);
    freopen("pancake.out", "w", stdout);

    char buffer[2222];
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        int k;
        scanf("%s %d", buffer, &k);
        int len = strlen(buffer);

        int ans = 0;
        for (int i = 0; i <= len - k; i++) {
            if (buffer[i] == '-') {
                ans++;
                for (int j = 0; j < k; j++) {
                    buffer[i + j] = turn(buffer[i + j]);
                }
            }
        }
        for (int i = len - k; i < len; i++) {
            if (buffer[i] == '-') {
                ans = -1;
            }
        }
        if (ans == -1)
            printf("Case #%d: IMPOSSIBLE\n", t);
        else
            printf("Case #%d: %d\n", t, ans);
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}
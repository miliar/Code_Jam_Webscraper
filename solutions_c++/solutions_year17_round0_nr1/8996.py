#include <cstdio>
#include <cstring>

using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int bot, top, T, len, K, tries;
    int i, tcase;
    bool possible, right;
    char s[1005];

    scanf("%d", &T);
    for (tcase = 1; tcase <= T; ++tcase) {
        scanf("%s%d", s, &K);
        tries = 0;
        bot = 0;
        len = strlen(s);
        top = len - 1;

        right = false;
        while (top - bot + 1 >= K) {
            if (right) {
                if (s[top] != '+') {
                    for (i = top; i > top - K; --i) {
                        s[i] = s[i] == '+' ? '-' : '+';
                    }
                    ++tries;
                }
                --top;
            }
            else {
                if (s[bot] != '+') {
                    for (i = bot; i < bot + K; ++i) {
                        s[i] = s[i] == '+' ? '-' : '+';
                    }
                    ++tries;
                }
                ++bot;
            }
            right = !right;
        }

        possible = true;
        for (i = 0; i < len; ++i) {
            if (s[i] != '+') {
                possible = false;
                break;
            }
        }

        printf("Case #%d: ", tcase);
        if (possible) {
            printf("%d", tries);
        }
        else {
            printf("IMPOSSIBLE");
        }
        printf("\n");
    }
    return 0;
}

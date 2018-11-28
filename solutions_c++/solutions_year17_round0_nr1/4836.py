#include <cstdio>
#include <cstring>
using namespace std;

int z, k, res;
char s[1000];

int solution() {
    int res = 0, i;
    for (i = 0; i + k - 1 < strlen(s); i++) {
        if (s[i] == '-') {
            res++;
            for (int j = 0; j < k; j++) {
                if (s[i + j] == '+') {
                    s[i + j] = '-';
                }
                else {
                    s[i + j] = '+';
                }
            }
        }
    }
    for (; i < strlen(s); i++) {
        if (s[i] == '-') {
            return -1;
        }
    }
    return res;
}

int main() {
    scanf("%d", &z);

    for (int nr = 1; nr <= z; nr++) {
        scanf(" %s%d", s, &k);
        printf("Case #%d: ", nr);
        res = solution();
        if (res == -1) {
            printf("IMPOSSIBLE\n");
        }
        else {
            printf("%d\n", res);
        }
    }
}
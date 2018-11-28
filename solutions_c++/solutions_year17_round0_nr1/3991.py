#include <stdio.h>
#include <string.h>
#define MAXS 1010

int T, K;
char S[MAXS];

void flip(char &c) {
    if (c == '-') c = '+';
    else if (c == '+') c = '-';
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d\n", &T);
    int count = 0;
    while (T-- > 0) {
        scanf("%s %d", S, &K);
        int Slen = strlen(S);
        int result = 0;
        for (int i = 0; i < Slen-K+1; i++) {
            if (S[i] == '-') {
                for (int j = 0; j < K; j++)
                    flip(S[i+j]);
                result++;
            }
        }
        bool good = true;
        for (int j = 0; j < Slen && good; j++) {
            if (S[j] == '-') good = false;
        }
        if (good) {
            printf("Case #%d: %d\n", ++count, result);
        }
        else {
            printf("Case #%d: IMPOSSIBLE\n", ++count);
        }
    }
    return 0;
}

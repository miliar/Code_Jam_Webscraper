#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

const int maxs = 1010;

char s[maxs];

int main() {
    int T;
    scanf("%d", &T);
    for (int test = 0; test < T; test++) {
        int K;
        scanf("%s %d", s, &K);
        int N = strlen(s);
        int x = 0;
        for (int i = 0; i < N; i++) {
            if (s[i] == '+')
                continue;
            x += 1;
            if (i + K > N) {
                x = -1;
                break;
            }
            for (int j = 0; j < K; j++) {
                s[i + j] = (s[i + j] == '-') ? '+' : '-';
            }
        }
        printf("Case #%d: ", test + 1);
        if (x == -1) {
            printf("IMPOSSIBLE");
        }
        else {
            printf("%d", x);
        }
        printf("\n");
    }
    
    return 0;
};

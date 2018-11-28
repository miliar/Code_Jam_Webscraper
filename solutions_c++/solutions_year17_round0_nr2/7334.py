#include <cstdio>
#include <cstring>

int main(void) {
    int T, len, k;
    char N[20];

    //freopen("B-large.in", "r", stdin);
    //freopen("B-large.out", "w", stdout);

    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++cas) {
        scanf("%s", N);

        len = strlen(N);

        for(int i = 0; i < len-1; ++i) {
            if(N[i] > N[i+1]) {
                while(N[i-1] == N[i] && i > 0) --i;
                --N[i];
                for(int j = i+1; j < len; ++j) N[j] = '9';
                break;
            }
        }

        printf("Case #%d: ", cas);
        for(k = 0; N[k] == '0'; ++k);
        for(; k < len; ++k) printf("%c", N[k]);
        printf("\n");
    }
}

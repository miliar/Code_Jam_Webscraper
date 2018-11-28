#include <stdio.h>
#include <string.h>

int main()
{
    int cas;
    scanf("%d", &cas);
    for (int ca = 1; ca <= cas; ++ ca) {
        static char buffer[1000 + 1];
        int K;
        scanf("%s%d", buffer, &K);
        int n = strlen(buffer);
        int bit[1000 + 1];
        for (int i = 0; i < n; ++ i)
            bit[i] = buffer[i] == '-';
        int result = 0;
        for (int i = 0; i + K <= n; ++ i) if (bit[i]) {
            for (int j = 0; j < K; ++ j)
                bit[i + j] ^= 1;
            result ++;
        }
        bool flag = true;
        for (int i = 0; i < n; ++ i)
            flag &= bit[i] == 0;
        printf("Case #%d: ", ca);
        if (!flag) puts("IMPOSSIBLE");
        else printf("%d\n", result);
    }
}

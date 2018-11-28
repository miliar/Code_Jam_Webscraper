#include <stdio.h>
#include <string.h>

using namespace std;

char S[1005];
int T, K;

int main()
{
        freopen("date.in","r",stdin);
        freopen("date.out","w",stdout);

        int i, leng, countx = 0, test, j;
        scanf("%d", &T);

        for (test = 1; test <= T; test++) {
                scanf("%s %d\n",S, &K);
                leng = strlen(S);
                countx = 0;
                for (i = 0; i < leng-K+1; i++)
                        if (S[i] == '-') {
                                for (j = i; j <= i+K-1; j++)
                                        if (S[j] == '-') S[j] = '+';
                                        else
                                              S[j] = '-';
                                countx++;
                        }

                for (i = 0; i < leng; i++)
                        if (S[i] == '-') countx = -1;

                if (countx == -1) printf("Case #%d: IMPOSSIBLE\n", test);
                else
                        printf("Case #%d: %d\n", test, countx);
        }

        return 0;
}

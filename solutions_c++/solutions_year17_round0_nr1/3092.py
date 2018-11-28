#include <stdio.h>

int tc, tt;

char s[1010];
int k;

int main()
{
    scanf("%d", &tt);
    for (tc = 0; tc < tt; tc++){
        printf("Case #%d: ", tc + 1);

        scanf("%s", s);
        scanf("%d", &k);
        int ansv = 0;
        for (int i = 0; s[i] && ansv >= 0; i++){
            if (s[i] == '-'){
                ++ansv;
                for (int j = 0; j < k; j++){
                    if (!s[i+j]){
                        ansv = -1;
                        break;
                        }
                    s[i+j] = s[i+j] == '+' ? '-' : '+';
                    }
                }
            }
        if (ansv >= 0)
            printf ("%d\n", ansv);
        else
            printf ("IMPOSSIBLE\n") ;


        }
    return 0;
}

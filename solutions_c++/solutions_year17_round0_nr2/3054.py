#include <stdio.h>
#include <string.h>

int tc, tt;

char s[20];
int main()
{
    scanf("%d", &tt);
    for (tc = 0; tc < tt; tc++){
        printf("Case #%d: ", tc + 1);

        scanf("%s", s);

        char *p = s;
        for (; p[1]; ++p){
            if (p[0] > p[1]){
                for (char *t = p+1; t[0]; ++t)
                    t[0] = '9';
                --p[0];
                break;
                }
            }
        while (p != s){
            --p;
            if (p[0] > p[1]){
                p[1] = '9';
                p[0]--;
                }
            }
        if (p[0] == '0')
            ++p;
        puts(p);

        }
    return 0;
}

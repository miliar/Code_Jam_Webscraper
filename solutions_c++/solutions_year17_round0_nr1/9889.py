#include<stdio.h>

FILE *out;


int main ()
{
    int t;
    scanf("%d", &t);

    out = fopen("asas.out", "w");

    for(int c = 0; c < t; c++) {
        char *s = new char[1000];
        int inv;
        scanf("%s %d", s, &inv);
        //fprintf(out, "%s %d asdasd\n", s, inv);

        int i = 0;
        while(s[i] != 0) {
            i++;
        }
        int n = i;
        int tota = 0;
        for(int i = 0; i <= n - inv; i++) {
            if(s[i] == '-') {
                tota++;
                for(int j = 0; j < inv; j++) {
                    if(s[i + j] == '-') {
                        s[i + j] = '+';
                    } else {
                        s[i + j] = '-';
                    }
                }
            }
        }
        int f = 1;
        for(int i = n - inv + 1; i < n; i++) {
            if(s[i] == '-') {
                f = 0;
            }
        }
        fprintf(out, "Case #%d: ", c + 1);
        if(f) {
            fprintf(out, "%d\n", tota);
        } else {
            fprintf(out, "IMPOSSIBLE\n");
        }
    }

    return 0;
}


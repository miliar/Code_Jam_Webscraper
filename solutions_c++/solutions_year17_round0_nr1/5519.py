#include <iostream>
#include <stdio.h>

using namespace std;
FILE * f = fopen("date.in", "r");
FILE * g = fopen("date.out", "w");
char v[1002];

int main()
{
    int t, j, flip, cnt, num, ok;
    char x;
    fscanf(f, "%d", &t);
    for (int i = 1; i <= t; ++i) {
        j = 0; num = 0; ok = 1;
        fscanf(f, "%c", &x);
        while (x != ' ') {
            v[j++] = x;
            fscanf(f, "%c", &x);
        }
        fscanf(f, "%d", &flip);
        cnt = j;


        for (int k = 0; k <= cnt - flip; ++k) {
            if (v[k] == '-') {
                for (int pos = k; pos < k + flip; ++pos) {
                    if (v[pos] == '-')
                        v[pos] = '+';
                    else
                        v[pos] = '-';
                }
                ++num;
            }
        }
        for (int k = 0; k < cnt && ok; ++k)
            if (v[k] == '-')
                ok = 0;

        if (!ok)
            fprintf(g, "Case #%d: IMPOSSIBLE\n", i);
        else
            fprintf(g, "Case #%d: %d\n", i, num);
    }
    return 0;
}

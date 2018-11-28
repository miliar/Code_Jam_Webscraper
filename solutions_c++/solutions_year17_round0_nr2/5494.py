#include <iostream>
#include <stdio.h>

using namespace std;
FILE * f = fopen("date.in", "r");
FILE * g = fopen("date.out", "w");
int v[20];

void tidy_gen(int cnt, int nr)
{
    int pos = 0, ok = 1;
    while (pos < cnt - 1 && ok) {
        if (v[pos + 1] < v[pos])
            ok = 0;
        ++pos;
    }

    if (!ok) {
    for (int i = pos; i < cnt; ++i)
        v[i] = 9;

    --pos;
    --v[pos];
    while (v[pos] < v[pos - 1] && pos > 0) {
        v[pos] = 9;
        --pos;
        if (v[pos] == 0) {
            v[pos] = 9;
            --v[pos];
        }
        else
            --v[pos];
    }

    }

    pos = 0;
    while (v[pos] == 0)
        ++pos;
    fprintf(g, "Case #%d: ", nr);
    for (int i = pos; i < cnt; ++i)
        fprintf(g, "%d", v[i]);
    fprintf(g, "\n");
}

int main()
{
    int t, nr = 0;
    char dump;
    fscanf(f, "%d%c", &t, &dump);
    for (int i = 0; i < t; ++i) {
        char x;
        int cnt = 0;
        fscanf(f, "%c", &x);
        while (x != '\n') {
            v[cnt++] = x - 48;
            fscanf(f, "%c", &x);
        }
        ++nr;
        tidy_gen(cnt, nr);
    }
    return 0;
}

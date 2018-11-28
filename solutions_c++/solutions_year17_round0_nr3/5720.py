#include <stdio.h>
#include <iostream>

using namespace std;
FILE * f = fopen ("date.in", "r");
FILE * g = fopen ("date.out", "w");
int stall[1000002];

void occupy(int n, int nr, int cnt)
{
    int pos_l, pos_r, mijl, mijl_min, small_min, big_min, small, big, ls, rs;
    int first;
    /*if (n % 2)
        mijl = n / 2 - 1;
    else
        mijl = n / 2;*/
    for (int i = 1; i <= nr; ++i) {
    first = 1;
    for (int j = 1; j < n + 2; ++j) {
        pos_l = j - 1;
        while (!stall[j] && j < n + 2)
            ++j;
        pos_r = j;

        mijl = pos_l + (pos_r - pos_l) / 2;
        ls = mijl - pos_l - 1;
        rs = pos_r - mijl - 1;
        if (ls < rs) {
            small = ls;
            big = rs;
        }
        else {
            small = rs;
            big = ls;
        }
        if (!first && small == small_min)
        if (big > big_min) {
            mijl_min = mijl;
            small_min = small;
            big_min = big;
        }

        if (small > small_min || first == 1) {
            mijl_min = mijl;
            small_min = small;
            big_min = big;
            first = 0;
            }
    }
    stall[mijl_min] = 1;
    }
    fprintf(g, "Case #%d: %d %d\n", cnt, big_min, small_min);
}

int main()
{
    int t, n, nr, cnt;
    fscanf(f, "%d", &t);
    for (int i = 0; i < t; ++i) {
        fscanf(f, "%d%d", &n, &nr);
        for (int j = 0; j < n + 2; ++j)
            stall[j] = 0;
        stall[0] = 1;
        stall[n + 1] = 1;
        cnt = i + 1;
        occupy(n, nr, cnt);
    }
    return 0;
}

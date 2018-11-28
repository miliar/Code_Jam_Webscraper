#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

struct Blin
{
    int r;
    int h;
    double dvapr;
};

bool comparator (Blin &i, Blin &j)
{
    if (i.dvapr > j.dvapr)
        return true;
    else if (i.dvapr < j.dvapr)
        return false;

    return i.r > j.r;
}

void solving(int t)
{
    double answer = 0;
    int n, k;
    scanf("%d %d", &n, &k);

    std::vector<Blin> a;

    int r, h;
    double dvapr;
    for (int i = 0; i < n; i++)
    {
        scanf("%d %d", &r, &h);
        dvapr = 2 * (double)r * (double)h * M_PI;
        a.push_back({r, h, dvapr});
    }

    std::sort (a.begin(), a.end(), comparator);

    int besti = 0;
    int best = a[0].r;
    int worsti = 0;
    int worst = a[0].h;

    for (int i = 0; i < k-1; i++)
    {
        if (best < a[i].r)
        {
            best = a[i].r;
            besti = i;
        }
        if (worst < a[i].h)
        {
            worst = a[i].h;
            worsti = i;
        }
        answer += a[i].dvapr;
    }
    //answer += (double)a[besti].r * (double)a[besti].r * M_PI;

    double answer2, answerbest = answer;
    for (int i = k-1; i < n; i++) {
        answer2 = answer + a[i].dvapr;
        if (best < a[i].r) {
            answer2 += ((double)a[i].r * (double)a[i].r * M_PI);
        } else {
            answer2 += (double)a[besti].r * (double)a[besti].r * M_PI;
        }
        if (answerbest < answer2) {
            answerbest = answer2;
        }
    }

    printf("Case #%d: %lf\n", t, answerbest);
    fflush(stdout);
}

int main()
{
    int t, T;
    scanf("%d", &T);

    for (int t = 1; t <= T; t++)
        solving(t);

    return 0;
}

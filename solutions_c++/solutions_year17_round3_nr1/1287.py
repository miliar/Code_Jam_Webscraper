#include <cstdio>
#define _USE_MATH_DEFINES
#include <cmath>
#include <algorithm>

using namespace std;

#define NMAX 1000

struct Pancake {
    int r;
    int h;
    long long side;
};

bool cmp_r(const Pancake &a, const Pancake &b)
{
    return a.r > b.r ? true : (a.r == b.r ? a.h > b.h : false);
}

bool cmp_side(const Pancake &a, const Pancake &b)
{
    return a.side > b.side;
}

int main()
{
    int t;
    static Pancake pancakes[NMAX];

    scanf("%d", &t);
    for (int tc = 1; tc <= t; ++tc) {
        int n, k;
        long long max_area = 0;

        scanf("%d %d", &n, &k);
        for (int i = 0; i < n; ++i) {
            scanf("%d %d", &pancakes[i].r, &pancakes[i].h);
            pancakes[i].side = (long long)pancakes[i].r*pancakes[i].h;
        }

        for (int i = 0; i < n-k+1; ++i) {
            long long area = 0;

            //printf("i: %d\n", i);

            /*for (int j = i+1; j < n; ++j) {
                if (pancakes[i].r < pancakes[j].r) {
                    swap(pancakes[i], pancakes[j]);
                }
            }*/
            sort(pancakes, pancakes+n, cmp_r);
            //printf("i-th pancake: %d %d\n", pancakes[i].r, pancakes[i].h);
            sort(pancakes+i+1, pancakes+n, cmp_side);
            area = (long long)pancakes[i].r*pancakes[i].r;
            for (int j = i; j < i+k; ++j) {
                //printf("\tadding pancake: %d %d\n", pancakes[j].r, pancakes[j].h);
                area += 2LL*pancakes[j].side;
            }
            //printf("area: %lld\n", area);
            max_area = max(max_area, area);
        }

        printf("Case #%d: %f\n", tc, M_PI*max_area);
    }
}

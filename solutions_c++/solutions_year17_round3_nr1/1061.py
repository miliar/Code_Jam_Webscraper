#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <cstddef>
#include <iostream>

#define PI 3.1415926535897932384626433832795

using namespace std;

struct Pancake
{
    uint64_t r;
    uint64_t h;
    uint64_t s;
};

struct RComp
{
    bool operator()(const Pancake& p1, const Pancake& p2) const
    {
        if (p1.r > p2.r)
            return true;
        if (p2.r > p1.r)
            return false;
        return p1.h > p2.h;
    }
};

struct SComp
{
    bool operator()(const Pancake& p1, const Pancake& p2) const
    {
        return p1.s > p2.s;
    }
};

#define MAXPANCAKES 1000

int n, k;
Pancake pancakes[MAXPANCAKES];
Pancake subpan[MAXPANCAKES];

double solve()
{
    cin >> n >> k;
    for (int i = 0; i < n; ++i)
    {
        cin >> pancakes[i].r >> pancakes[i].h;
        pancakes[i].s = 2 * pancakes[i].r*pancakes[i].h;
    }

    uint64_t best = 0;
    sort(pancakes, pancakes + n, RComp());
    for (int i = 0; i <= (n - k); ++i)
    {
        for (int j = i + 1; j < n; ++j)
        {
            subpan[j - i - 1] = pancakes[j];
        }
        sort(subpan, subpan + (n - i - 1), SComp());
        uint64_t score = pancakes[i].r*pancakes[i].r + pancakes[i].s;
        for (int j = 0; j < (k-1); ++j)
        {
            score += subpan[j].s;
        }
        if (score > best)
        {
            best = score;
        }
    }

    return PI*(double)best;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        printf("Case #%d: %.9f\n", i, solve());
    }
}

#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstdlib>

using namespace std;

ifstream in("A-large.in");
ofstream out("output.txt");

#define out cout

struct pancake {
    long long r;
    long long h;
};

bool cmp(struct pancake a, struct pancake b) {
    if (a.r == b.r) return a.h > b.h;
    else return a.r > b.r;
}

bool cmp2(struct pancake a, struct pancake b) {
    return a.h*a.r > b.h*b.r;
}

int main()
{
    FILE *fout = fopen("A-large.out", "w");
    int t;
    in >> t;
    for (int i = 0; i < t; ++i) {
        int n, k;
        in >> n >> k;
        struct pancake p[n];
        for (int j = 0; j < n; ++j) {
            long long r, h;
            in >> r >> h;
            p[j].r = r;
            p[j].h = h;
        }
        sort(p, p + n, cmp);
        double ans = 0.0;
        for (int j = 0; j < n - k + 1; ++j) {
            double a = 0.0;
            a += M_PI * pow(p[j].r, 2);
            a += 2.0 * M_PI * p[j].r * p[j].h;
            if (n-j-1 == 0) {
                    if (ans < a) ans = a;
                    continue;
            }
            struct pancake tmp[n-j-1];
            for (int l = 0; l < n-j-1; ++l) tmp[l] = p[j+l+1];
            sort(tmp, tmp + n-j-1, cmp2);
            for (int l = 0; l < k-1; ++l) {
                a += 2.0 * M_PI * tmp[l].r * tmp[l].h;
            }
            if (ans < a) ans = a;
        }
        fprintf(fout, "Case #%d: %.9f\n", i+1, ans);
        //out << "Case #" << i + 1 << ": " <<
    }
    return 0;
}

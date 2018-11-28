#include <stdio.h>
#include <math.h>
#include <string.h>
#include <algorithm>

using namespace std;

const int N = 1100;

struct PCK {
    double s;
    double r;
};



int base;
int comp(PCK &a, PCK &b) {
    if (a.r>base) return 0;
    if (b.r>base) return 1;
    return a.s!=b.s ? a.s>b.s : a.r>b.r;
}

int n, k;
double r[N], h[N];
int sel[N];
double PI = acos(-1);
PCK p[N];
PCK p2[N]; int np2;


int main() {
    int t;
    int nw = 0;
    double nws = 0;
    double mx = 0;
    double nwa = 0;
    scanf("%d", &t);
    for (int o=1; o<=t; o++) {
        scanf("%d %d", &n, &k);
        mx = 0;
        for (int i=0; i<n; i++) {
            scanf("%lf %lf", r+i, h+i);
            p[i].s = h[i]*r[i]*2*PI;
            p[i].r = r[i];
        }

        for (int b=0; b<n; b++) {
            base = p[b].r;
            nwa = p[b].s + p[b].r*p[b].r*PI;
            np2 = 0;
            for (int i=0; i<n; i++)
                if (i!=b)
                    p2[np2++] = p[i];
            sort(p2, p2+n-1, comp);
            for (int i=0; i<k-1 && p2[i].r<=base; i++)
                nwa += p2[i].s;
            if (mx<nwa)
                mx = nwa;
        }
        printf("Case #%d: %f\n", o, mx);
    }
}

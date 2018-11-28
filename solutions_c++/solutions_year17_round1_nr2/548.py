#include <bits/stdc++.h>

using namespace std;

bool valid (int a, double x) {
    return a*0.9 <= x && x <= a*1.1;
}

int findl(int beg, int end, double x) {
    int h = end;
    while (beg <= end) {
        h = (beg+end)/2;
        if (valid(h, x))    end = h-1;
        else    beg = h+1;
    }
    if (!valid(h, x))   h++;
    return h;
}

int findr(int beg, int end, double x) {
    int h = beg;
    while (beg <= end) {
        h = (beg+end)/2;
        if (valid(h, x))    beg = h+1;
        else    end = h-1;
    }
    if (!valid(h, x))   h--;
    return h;
}

int M[50][50];
int v[50];

int main (void) {
    int t;
    scanf ("%d", &t);
    for (int c = 1; c <= t; c++) {
        printf ("Case #%d: ", c);
        int n, p;
        scanf ("%d%d", &n, &p);
        for (int i = 0; i < n; i++) {
            scanf ("%d", &v[i]);
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < p; j++) {
                scanf ("%d", &M[i][j]);
            }
            sort(M[i], M[i]+p);
        }
        int curr[n];
        memset(curr, 0, sizeof curr);
        bool ok = true;
        int ans = 0;
        while (ok) {
            int mn = 0, mx = 1000001;
            int mnmx = 1000001;
            int mnmxi = -1;
            for (int i = 0; i < n; i++) {
                int l, r;
                do {
                    int x = M[i][curr[i]]/v[i];
                    double dx = M[i][curr[i]]/(double)v[i];
                    l = findl(0, x, dx);
                    r = findr(x+1, 1000000, dx);
                //    printf ("%d %.2lf, l: %d r: %d\n", M[i][curr[i]], dx, l, r);
                    if (l > r)  curr[i]++;
                } while (l > r && curr[i] < p);
                if (curr[i] == p) {
                    ok = false;
                    break;
                }
                mn = max(mn, l);
                mx = min(mx, r);
                if (mnmx > r) {
                    mnmx = r;
                    mnmxi = i;
                }
            }
            if (ok) {
                if (mn <= mx) {
                    for (int i = 0; i < n; i++) curr[i]++;
                    ans++;
                } else {
                    curr[mnmxi]++;
                }

                for (int i = 0; i < n; i++) {
                    if (curr[i] == p)   ok = false;
                }
            }
        }
        printf ("%d\n", ans);
    }
}

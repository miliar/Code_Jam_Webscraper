#include <bits/stdc++.h>
#define VMAX 1005
#define PI 3.141592653

using namespace std;

ifstream fin("pancake.in");
ofstream fout("pancake.out");

long double Max;
int x[VMAX], n, k;

struct Pancake {
    long double r, h, aLat, a;
} v[VMAX], w[VMAX];

bool compareA(Pancake a, Pancake b) {
    return a.aLat + a.a > b.aLat + b.a ||
           a.aLat + a.a == b.aLat + b.a &&
           (a.r > b.r || a.r == b.r && a.h >= b.h);
}

bool compare(Pancake a, Pancake b) {
    return a.r <= b.r;
}

void afisareSol() {
    for (int i = 1; i <= k; i++)
        w[i] = v[x[i]];
    sort(w + 1, w + k + 1, compare);
    long double sum = w[1].a + w[1].aLat;
    for (int i = 2; i <= k; i++)
        sum += w[i].a - w[i - 1].a + w[i].aLat;
    if (sum > Max)
        Max = sum;
}

void comb(int K) {
    if (K == k + 1)
        afisareSol();
    else
        for (int i = x[K - 1] + 1; i <= n - k + K; i++) {
            x[K] = i;
            comb(K + 1);
        }
}

int main() {
    int t; fin >> t;
    for (int test = 1; test <= t; test++) {
        fin >> n >> k;
        for (int i = 1; i <= n; i++) {
            fin >> v[i].r >> v[i].h;
            v[i].aLat = PI * v[i].r * v[i].h * 2;
            v[i].a = PI * v[i].r * v[i].r;
        }
        sort(v + 1, v + n + 1, compareA);
        for (int i = 1; i <= n; i++)
            x[i] = i;
        Max = 0.0; comb(1);
        fout << fixed << setprecision(9) << "Case #" << test << ": " << Max << '\n';
    }
    fout.close();
    return 0;
}

#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

const int MX = 24 * 60;
const int HMX = MX / 2;
const int oo = MX * 2;

int mark[MX+5], f[MX+5][MX+5][2][2];

void solve(int nt) {
    int n, m;
    scanf("%d%d", &n, &m);

    for (int i = 0; i < MX; i++) mark[i] = 0;

    while (n--) {
        int l, r;
        scanf("%d%d", &l, &r);
        while (l < r) {
            mark[l] = 1;
            l++;
        }
    }

    n = m;

    while (n--) {
        int l, r;
        scanf("%d%d", &l, &r);
        while (l < r) {
            mark[l] = 2;
            l++;
        }
    }

    for (int j = 0; j < 2; j++)
    for (int k = 0; k < 2; k++)
    for (int z = 0; z < 2; z++)
        f[0][j][k][z] = oo;

    if (mark[0] != 2) {
        f[0][1][0][0] = 0;
    }
    if (mark[0] != 1) {
        f[0][0][1][1] = 0;
    }

    for (int i = 1; i < MX; i++) {
        for (int z = 0; z <= i+1; z++)
        for (int j = 0; j < 2; j++)
        for (int k = 0; k < 2; k++)
            f[i][z][j][k] = oo;
        for (int z = 0; z <= i; z++)
        for (int j = 0; j < 2; j++)
        for (int k = 0; k < 2; k++)
            if (f[i-1][z][j][k] < oo) {
                if (mark[i] != 2) {
                    f[i][z+1][0][k] = min(f[i][z+1][0][k], f[i-1][z][j][k] + (j));
                }
                if (mark[i] != 1) {
                    f[i][z][1][k] = min(f[i][z][1][k], f[i-1][z][j][k] + (j^1));
                }
            }
    }

    int ans = oo;
    for (int i = 0; i < 2; i++)
    for (int j = 0; j < 2; j++)
        ans = min(ans, f[MX-1][MX/2][i][j] + (i^j));

    printf("Case #%d: %d\n", nt, ans);
}

int main() {
    int ct;
    scanf("%d", &ct);
    for (int nt = 1; nt <= ct; nt++) {
        solve(nt);
        fprintf(stderr, "Case %d done.\n", nt);
    }
}

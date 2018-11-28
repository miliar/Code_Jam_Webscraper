#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

const char kt[3][2] = {'R', 'G', 'Y', 'V', 'B', 'O'};

int ans[10], a[10][10], don[10], kep[10], rem[10], mi[10], ma[10], vt[10];

inline bool cmp(int i, int j) { return ans[i] > ans[j]; }

void solve(int nt) {
    int n, rr, oo, yy, gg, bb, vv;
    scanf("%d%d%d%d%d%d%d", &n, &a[0][0], &a[2][1], &a[1][0], &a[0][1], &a[2][0], &a[1][1]);
    printf("Case #%d: ", nt);

    for (int i = 0; i < 3; i++)
        if (a[i][0] + a[i][1] == n) {
            if (a[i][0] != a[i][1]) {
                printf("IMPOSSIBLE\n"); return;
            }
            while (a[i][0]--) {
                printf("%c%c", kt[i][0], kt[i][1]);
            }
            printf("\n"); return;
        }
        else if (a[i][0] + a[i][1] > 0 && a[i][0] <= a[i][1]) {
            printf("IMPOSSIBLE\n"); return;
        }

    for (int i = 0; i < 3; i++) {
        ma[i] = a[i][0] - a[i][1];
        mi[i] = ma[i] - max(min(ma[i]-1, a[i][1]), 0);
    }

    bool ok = false;

    for (int i0 = mi[0]; !ok && i0 <= ma[0]; i0++) {
    for (int i1 = mi[1]; !ok && i1 <= ma[1]; i1++) {
    for (int i2 = mi[2]; !ok && i2 <= ma[2]; i2++) {
        if (max(max(i0,i1),i2) * 2 <= i0+i1+i2) {
            ans[0] = i0; ans[1] = i1; ans[2] = i2; ok = true; break;
        }
    }
    }
    }

    if (!ok) {
        printf("IMPOSSIBLE\n"); return;
    }

    vt[0] = 0; vt[1] = 1; vt[2] = 2;
    sort(vt, vt+3, cmp);

    vector<int> res;

    for (int i = 1; i <= ans[vt[0]]; i++) {
        res.push_back(vt[0]);
        if (i <= ans[vt[1]]) res.push_back(vt[1]);
        if (ans[vt[0]]-i+1 <= ans[vt[2]]) res.push_back(vt[2]);
    }

    for (int i = 0; i < 3; i++) {
        if (a[i][1] == 0) {
            don[i] = a[i][0]; continue;
        }
        kep[i] = min(ma[i]-1, a[i][1]);
        don[i] = ma[i] - 1 - kep[i];
        rem[i] = a[i][1] - kep[i];
    }

    for (int i = 0; i < res.size(); i++) {
        int u = res[i];
        if (don[u] > 0) {
            don[u]--;
            printf("%c", kt[u][0]);
        }
        else if (kep[u] > 0) {
            kep[u]--;
            printf("%c%c", kt[u][0], kt[u][1]);
        }
        else {
            while (rem[u]--) printf("%c%c", kt[u][0], kt[u][1]);
            printf("%c", kt[u][0]);
        }
    }
    printf("\n");
}

int main() {
    int ct;
    scanf("%d", &ct);
    for (int nt = 1; nt <= ct; nt++) {
        solve(nt);
        fprintf(stderr, "Case %d done.\n", nt);
    }
}

#include <bits/stdc++.h>
using namespace std;

int N, o[100][100], f[100][100], mta[100], mtb[199], vta[100], vtb[199];
vector<pair<pair<int, int>, char> > v;

int aua(int i) {
    if (vta[i]) return 0;
    vta[i] = 1;
    for (int j = 0; j < N; j++) if (mta[j] == -1 || (mta[j] > -1 && aua(mta[j]))) {mta[j] = i; return 1;}
    return 0;
}

int aub(int i) {
    if (vtb[i]) return 0;
    vtb[i] = 1;
    for (int j = max(N - i - 1, i + 1 - N); j <= (N - 1) * 2 - max(N - i - 1, i + 1 - N); j += 2) if (mtb[j] == -1 || (mtb[j] > -1 && aub(mtb[j]))) {mtb[j] = i; return 1;}
    return 0;
}

int main() {
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int T, tI, M, a, b, r, i, j;
    char c;
    scanf("%d", &T);
    for (tI = 0; tI < T; tI++) {
        scanf("%d %d", &N, &M);
        for (i = 0; i < N; i++) mta[i] = -1, vta[i] = 0;
        for (i = 0; i < N * 2 - 1; i++) mtb[i] = -1, vtb[i] = 0;
        r = 0;
        for (i = 0; i < N; i++) for (j = 0; j < N; j++) o[i][j] = f[i][j] = 0;
        for (i = 0; i < M; i++) {
            scanf("\n%c %d %d", &c, &a, &b);
            a--;
            b--;
            if (c == 'x') {
                o[a][b] = f[a][b] = 1;
                vta[a] = -1;
                mta[b] = -2;
                r++;
            }
            if (c == '+') {
                o[a][b] = f[a][b] = 2;
                vtb[a - b + N - 1] = -1;
                mtb[a + b] = -2;
                r++;
            }
            if (c == 'o') {
                o[a][b] = f[a][b] = 3;
                vta[a] = -1;
                mta[b] = -2;
                vtb[a - b + N - 1] = -1;
                mtb[a + b] = -2;
                r += 2;
            }
        }
        for (i = 0; i < N; i++) {
            for (j = 0; j < N; j++) if (vta[j] > -1) vta[j] = 0;
            r += aua(i);
        }
        for (i = 0; i < N * 2 - 1; i++) {
            for (j = 0; j < N * 2 - 1; j++) if (vtb[j] > -1) vtb[j] = 0;
            r += aub(i);
        }
        for (i = 0; i < N; i++) if (mta[i] > -1) {
            a = mta[i];
            b = i;
            f[a][b] |= 1;
        }
        for (i = 0; i < N * 2 - 1; i++) if (mtb[i] > -1) {
            a = (i + mtb[i] - N + 1) / 2;
            b = (i - mtb[i] + N - 1) / 2;
            f[a][b] |= 2;
        }
        v.clear();
        char trc[4] = {'.', 'x', '+', 'o'};
        for (i = 0; i < N; i++) for (j = 0; j < N; j++) if (o[i][j] != f[i][j]) v.push_back(make_pair(make_pair(i + 1, j + 1), trc[f[i][j]]));
        printf("Case #%d: %d %d\n", tI + 1, r, v.size());
        for (i = 0; i < v.size(); i++) printf("%c %d %d\n", v[i].second, v[i].first.first, v[i].first.second);
    }
    return 0;
}

#include <bits/stdc++.h>

using namespace std;

constexpr int MAXN = 1e3;


vector<int> fuck(int t, int o, int z) {
    const int n = t + o + z;
    vector<int> ret(n);

    int idx = 0;

    int tmp = t - o;
    for (int i = 0; i < tmp; ++i) {
        ret[idx++] = 0;
        ret[idx++] = 2;
        ret[idx++] = 1;
        ret[idx++] = 2;
    }
    z -= tmp;
    o -= tmp;
    t -= tmp * 2;

    tmp = z;
    for (int i = 0; i < tmp; ++i) {
        ret[idx++] = 0;
        ret[idx++] = 1;
        ret[idx++] = 2;
    }
    z -= tmp;
    o -= tmp;
    t -= tmp;

    assert (o == t);

    tmp = t;
    for (int i = 0; i < tmp; ++i) {
        ret[idx++] = 1;
        ret[idx++] = 2;
    }

    return ret;
}


void jizz() {
    int n; scanf("%d", &n);

    int r, o, y, g, b, v;
    scanf("%d%d%d%d%d%d", &r, &o, &y, &g, &b, &v);

    assert (o == 0 and g == 0 and v == 0);

    pair<int, char> ps[3];
    ps[0] = {r, 'R'};
    ps[1] = {y, 'Y'};
    ps[2] = {b, 'B'};
    sort(ps, ps+3);

    if (ps[2].first * 2 > n) {
        puts("IMPOSSIBLE");
        return ;
    }

    vector<int> out = fuck(ps[2].first, ps[1].first, ps[0].first);
    for (int i = 0; i < n; ++i) putchar(ps[out[i]].second);
    putchar('\n');
}

int main() {
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);
        jizz();
    }
    return 0;
}

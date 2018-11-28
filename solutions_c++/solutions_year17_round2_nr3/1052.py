#include <bits/stdc++.h>

using namespace std;

struct state {
    int city, horse, horse_left;
};

state make_state(int c, int h, int hl) {
    state s;
    s.city  =c;
    s.horse = h;
    s.horse_left = hl;
    return s;
}

struct comp {
    bool operator()(const state &a, const state &b) const {
        if(a.city < b.city)
            return true;
        if(a.city == b.city && a.horse < b.horse)
            return true;
        if(a.city == b.city && a.horse == b.horse && a.horse_left < b.horse_left)
            return true;
        return false;
    }
};

int n, q;
int e[107], s[107];
vector<pair<int, int> > G[107];
bool odw[107];
map<state, double, comp> mem;

double odl(state S, int b) {
    if(mem.count(S))
        return mem[S];

    if(S.city == b)
        return 0;

    odw[S.city] = true;

    double res = 10e13;
    for(auto p : G[S.city]) {
        int dist = p.first;
        int nekst = p.second;

        if(odw[nekst])
            continue;

        if(S.horse_left >= dist)
            res = min(res, (double(dist) / double(s[S.horse])) + odl(make_state(nekst, S.horse, S.horse_left - dist), b));
        if(e[S.city] >= dist)
            res = min(res, (double(dist) / double(s[S.city])) + odl(make_state(nekst, S.city, e[S.city] - dist), b));
    }

    odw[S.city] = false;
    mem[S] = res;
    return res;
}

int main() {
    int t;
    scanf("%d", &t);

    for(int c = 1 ; c <= t ; c++) {
        scanf("%d %d", &n, &q);

        for(int i = 1 ; i <= n ; i++) {
            scanf("%d %d", &e[i], &s[i]);
            G[i].clear();
        }

        int d;
        for(int a = 1 ; a <= n ; a++) {
            for(int b = 1 ; b <= n ; b++) {
                scanf("%d", &d);
                if(d != -1)
                    G[a].push_back(make_pair(d, b));
            }
        }

        printf("Case #%d:", c);
        while(q--) {
            int u, v;
            scanf("%d %d", &u, &v);
            memset(odw, 0, sizeof odw);
            mem.clear();
            printf(" %.7f", odl(make_state(u, u, e[u]), v));
        }
        printf("\n");
    }

    return 0;
}

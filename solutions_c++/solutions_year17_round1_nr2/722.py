#include <bits/stdc++.h>

#define EPS 1e-6

using namespace std;

int rz[55], x, t, n, p;

struct range {
    int l, r;

    range() : l(0), r(0) {};

    range(int g, int it) {
        double l_ = g / 1.1 / rz[it];
        double r_ = g / 0.9 / rz[it];

        l = ceil(l_ - EPS);
        r = floor(r_ + EPS);
    }

    range intersec(range o) {
        range ret;
        ret.l = max(l, o.l);
        ret.r = min(r, o.r);
        return ret;
    }

    bool valid() {
        return l <= r && l > 0;
    }
};

vector<range> pckg[55];

bool cmp(range a, range b) {
    if(a.l == b.l) return a.r < b.r;
    return a.l < b.l;
}

int main() {
    freopen("B-large__.in", "r", stdin);
    freopen("B-large__.out", "w", stdout);

    scanf("%d",&t);
    for(int T=1; T<=t; T++) {
        int ans = 0;
        scanf("%d %d", &n, &p);

        for(int i=0;i<n;i++) {
            scanf("%d", &rz[i]);
            pckg[i].clear();
        }

        for(int i=0;i<n;i++) {
            for(int j=0;j<p;j++) {
                scanf("%d", &x);
                pckg[i].push_back(range(x, i));

            } sort(pckg[i].begin(), pckg[i].end(), cmp);

            //for(int z=0;z<p;z++) {
            //    printf("%d %d\n", pckg[i][z].l, pckg[i][z].r);
            //} puts("");
        }

        int flag = true, pointer[55];
        memset(pointer, 0, sizeof pointer);

        while(flag) {

            range rg = pckg[0][pointer[0]];
            for(int i=0; i<n;i++) {
                if(!flag) break;

                range atual = pckg[i][pointer[i]];
                while(!atual.valid()) {
                    pointer[i]++;

                    if(pointer[i] >= p) {
                        flag = 0;
                        break;
                    }

                    atual = pckg[i][pointer[i]];
                }


                range new_r = rg.intersec(pckg[i][pointer[i]]);
                if(new_r.valid()) rg = new_r;

                else {
                    range atual = pckg[i][pointer[i]];
                    while(!rg.intersec(atual).valid() && cmp(atual, rg)) {
                        pointer[i]++;

                        if(pointer[i] >= p) {
                            flag = 0;
                            break;
                        }

                        atual = pckg[i][pointer[i]];
                    }

                    range new_r = rg.intersec(atual);
                    if(new_r.valid()) rg = new_r;
                    else {
                        rg = atual;
                        i = -1;
                        continue;
                    }
                }
            }


            if(!flag) continue;
            if(rg.valid()) {
                ans++;
                for(int i=0; i<n; i++)  {
                    pointer[i]++;
                    if(pointer[i] >= p) {
                        flag = 0;
                        break;
                    }
                }
            }
        }

        printf("Case #%d: %d\n", T, ans);
    }
    return 0;
}
/*

*/

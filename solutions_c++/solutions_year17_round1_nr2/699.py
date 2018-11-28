#include <cstdio>
#include <cmath>
#include <vector>

using namespace std;

struct Dat {
    int lr, rr;
    bool used;

    Dat() {}
    Dat(int lv, int rv): lr(lv), rr(rv), used(false) {};
    bool operator < (const Dat &dat) const {
        if (lr == dat.lr) {
            return rr < dat.rr;
        } else {
            return lr < dat.lr;
        }
    }
};

int main() {
    int T;
    scanf("%d", &T);

    for (int times = 0; times < T; times++) {
        int n, p;
        scanf("%d%d", &n, &p);

        vector<int> rec(n, 0);
        for (int i = 0; i < n; i++) {
            scanf("%d", &rec[i]); 
        }

        vector<vector<Dat>> tbl(n, vector<Dat>());
        int val;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < p; j++) {
                scanf("%d", &val);
                int lv = ceil(val / 1.1 / rec[i]);
                int rv = floor(val / 0.9 / rec[i]);
                tbl[i].emplace_back(lv, rv);
            }
            sort(tbl[i].begin(), tbl[i].end());
        }

        int ans = 0;
        for (int v = 1; v <= 1000000;) {
            vector<int> sol;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < p; j++) {
                    if (tbl[i][j].lr <= v and tbl[i][j].rr >= v and tbl[i][j].used == false) {
                        sol.push_back(j);
                        break;
                    }
                }
            }
            
            if (sol.size() == n) {
                ans += 1;
                for (int i = 0; i < n; i++) {
                    tbl[i][sol[i]].used = true;
                }
            } else {
                v += 1;
            }
        }

        printf("Case #%d: %d\n", times+1, ans);
    }
}

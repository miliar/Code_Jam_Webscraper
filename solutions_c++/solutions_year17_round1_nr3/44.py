#include "bits/stdc++.h"
using namespace std;

const int N = 101;

int vis[N][N][N][N];
#define pii pair < int, int >
#define F first
#define S second

int main() {
    freopen ("inp.in", "r", stdin);
    freopen ("A.out", "w", stdout);
    int t; cin >> t;
    for (int qq = 1; qq <= t; qq++) {
       int hd, ad, hk, ak, b, d;
       cin >> hd >> ad >> hk >> ak >> b >> d;
       for (int i = 0; i <= hd; i++) {
            for (int j = 0; j <= 100; j++) {
                for (int k = 0; k <= hk; k++) {
                    for (int l = 0; l <= ak; l++) {
                        vis[i][j][k][l] = -1;
                    }
                }
            }
       }
       vis[hd][ad][hk][ak] = 0;

       queue < pair < pii, pii > > bfs;
       bfs.push(make_pair(pii(hd, ad), pii(hk, ak)));
       int ans = -1; bool rekt = true;

       while (!bfs.empty()) {
            pair < pii, pii > cur = bfs.front();
            bfs.pop();
            int myh = cur.F.F;
            int mya = cur.F.S;
            int oph = cur.S.F;
            int opa = cur.S.S;
            ans = vis[myh][mya][oph][opa];

            if (oph <= 0) {
                ans = vis[myh][mya][oph][opa];
                rekt = false;
                break;
            }

            // attack
            int noph = oph - mya;
            int nmyh = myh - opa;
            if (noph <= 0) {
                nmyh += opa;
            }
            if (nmyh > 0) {
                noph = max(noph, 0);
                if (vis[nmyh][mya][noph][opa] == -1) {
                    vis[nmyh][mya][noph][opa] = ans + 1;
                    bfs.push(make_pair(pii(nmyh, mya), pii(noph, opa)));
                }
            }

            // buff
            int nmya = mya + b;
            nmyh = myh - opa;
            if (nmyh > 0) {
                nmya = min(oph, nmya);
                if (vis[nmyh][nmya][oph][opa] == -1) {
                    vis[nmyh][nmya][oph][opa] = ans + 1;
                    bfs.push(make_pair(pii(nmyh, nmya), pii(oph, opa)));
                }
            }

            // debuff
            int nopa = opa - d;
            nopa = max(nopa, 0);
            nmyh = myh - nopa;
            if (nmyh > 0) {
                if (vis[nmyh][mya][oph][nopa] == -1) {
                    vis[nmyh][mya][oph][nopa] = ans + 1;
                    bfs.push(make_pair(pii(nmyh, mya), pii(oph, nopa)));
                }
            }

            // cure
            nmyh = hd - opa;
            if (nmyh > 0) {
                if (vis[nmyh][mya][oph][opa] == -1) {
                    vis[nmyh][mya][oph][opa] = ans + 1;
                    bfs.push(make_pair(pii(nmyh, mya), pii(oph, opa)));
                }
            }
       }

       cout << "Case #" << qq << ": ";
       if (rekt) {
            cout << "IMPOSSIBLE\n";
       } else {
            cout << ans << "\n";
       }
    }
}
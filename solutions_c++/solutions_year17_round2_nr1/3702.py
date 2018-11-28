#include<bits/stdc++.h>
#define INF 0x7fffffff
#define INFLL 1e17
#define PI 2*acos(0.0)
#define show(x) cout<< #x <<" is "<< x <<"\n"
using namespace std;

#define FS first
#define SC second
#define PB(t) push_back(t)
#define ALL(t) t.begin(),t.end()
#define MP(x, y) make_pair((x), (y))
#define Fill(a,c) memset(&a, c, sizeof(a))

typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<LL> VLL;
typedef vector<PII> VPII;

int main() {
    #ifndef ONLINE_JUDGE
        freopen("R1BA-large.in", "rt", stdin);
        freopen("outputA.txt", "wt", stdout);
    #endif

    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    for (int cas = 0; cas < T; cas++) {
        int dest, nHor, idxMen;
        double t, x;
        cin >> dest >> nHor;

        VPII horses(nHor);

        for (auto& horse : horses) {
            cin >> horse.FS >> horse.SC;
        }

        sort(ALL(horses));
        idxMen = 0;
        for (int i = 1; i < nHor; i++) {
            if (horses[idxMen].SC > horses[i].SC) {
                t = (horses[idxMen].FS - horses[i].FS);
                t = t/(horses[i + 1].SC - horses[idxMen].SC);

                x = horses[idxMen].FS + horses[idxMen].SC * t;
                if (x < dest) {
                    idxMen = i;
                }
            }
        }
        t = (dest - horses[idxMen].FS) * 1.0 / horses[idxMen].SC;
        int isValid;
        double inf, sup, mid, eps = 1e-6;
        double res = dest / t;
        inf = 0; sup = res + 10;

        while (nHor > 1 && inf + eps < sup) {
            mid = inf + (sup - inf) / 2.0;

            t = dest / mid;
            isValid = 1;
            for (int i = 0; i < nHor; i++) {
                x = horses[i].FS + horses[i].SC * t;
                if (x < dest){
                    isValid = 0;
                    break;
                }
            }

            if (isValid) {
                res = mid;
                inf = mid;
            } else {
                sup = mid;
            }
        }

        //cout << "Case #" << cas + 1 << ": " << res << "\n";
        printf("Case #%d: %.10f\n", cas + 1, res);
    }
return 0;
}

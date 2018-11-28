#include <bits/stdc++.h>
#include <cstring>
#define MAXN 101

using namespace std;

typedef int Arr4Type[MAXN][MAXN][MAXN][MAXN];

Arr4Type vis, d;
deque< pair<pair<int, int>, pair<int, int> > > deq;

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int caseCnt;
    scanf("%d", &caseCnt);
    //caseCnt = 100;
    int caseNow = 0;
    while (caseNow < caseCnt) {
        ++caseNow;
        printf("Case #%d: ", caseNow);
        int Hd, Ad, Hk, Ak, B, D;
        scanf("%d%d%d%d%d%d", &Hd, &Ad, &Hk, &Ak, &B, &D);
      //  Hd = 3, Ad = 1, Hk = 3, Ak = 2, B = 1, D = 0;
//            3 1 3 2 1 0

        memset(vis, 0, sizeof(vis));
        memset(d, 0, sizeof(d));
        vis[Hd][Ad][Hk][Ak] = 1;
        d[Hd][Ad][Hk][Ak] = 0;
        deq.clear();
        deq.push_back({{Hd, Ad}, {Hk, Ak}});
        int ans = -1;
        while (!deq.empty()) {
            auto item = deq.front();
            deq.pop_front();
            int Hdi = item.first.first;
            int Adi = item.first.second;
            int Hki = item.second.first;
            int Aki = item.second.second;
            int stepCnt = d[Hdi][Adi][Hki][Aki];

            // attack
            int Hdj = Hdi - Aki;
            int Hkj = Hki - Adi;
            if (Hkj <= 0) {
                ans = stepCnt + 1;
                break;
            }
            if (Hdj > 0 && !vis[Hdj][Adi][Hkj][Aki]) {
                vis[Hdj][Adi][Hkj][Aki] = 1;
                d[Hdj][Adi][Hkj][Aki] = stepCnt + 1;
                deq.push_back({{Hdj, Adi}, {Hkj, Aki}});
            }

            // cure
            Hdj = Hd - Aki;
            Hkj = Hki;
            if (Hdj > 0 && !vis[Hdj][Adi][Hkj][Aki]) {
                vis[Hdj][Adi][Hkj][Aki] = 1;
                d[Hdj][Adi][Hkj][Aki] = stepCnt + 1;
                deq.push_back({{Hdj, Adi}, {Hkj, Aki}});
            }

            // Debuff
            int Adj = Adi;
            int Akj = max(0, Aki - D);
            Hdj = Hdi - Akj;
            Hkj = Hki;
            if (Hdj > 0 && !vis[Hdj][Adj][Hkj][Akj]) {
                vis[Hdj][Adj][Hkj][Akj] = 1;
                d[Hdj][Adj][Hkj][Akj] = stepCnt + 1;
                deq.push_back({{Hdj, Adj}, {Hkj, Akj}});
            }

            // buff
            if (Adi >= Hki) continue;
            Adj = Adi + B;
            Akj = Aki;
            Hdj = Hdi - Akj;
            Hkj = Hki;
            if (Hdj > 0 && !vis[Hdj][Adj][Hkj][Akj]) {
                vis[Hdj][Adj][Hkj][Akj] = 1;
                d[Hdj][Adj][Hkj][Akj] = stepCnt + 1;
                deq.push_back({{Hdj, Adj}, {Hkj, Akj}});
            }
        }
        if (ans >= 0) {
            printf("%d\n", ans);
        } else {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}

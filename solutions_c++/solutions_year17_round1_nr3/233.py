#include <iostream>
#include <cmath>
#include <queue>
#include <set>

using namespace std;

long long const inf = 1e9 + 10ll;

class State {
    public:
        int round, H1, A1, H2, A2;
};

typedef pair<int, int> pii;
typedef pair<pii, pii> mytype;

set<mytype> S;
queue<State> que;

int main(void) {

    int test_num;
    cin >> test_num;

    for (int Case = 1 ; Case <= test_num ; ++Case) {
        int Hd, Ad, Hk, Ak, B, D;
        cin >> Hd >> Ad >> Hk >> Ak >> B >> D;

        /*
        long long lo = 0, hi = inf;
        while (lo < hi) {
            long long mid = (lo + hi) / 2 + 1;
            if (canWin(mid, Hd, Ad, Hk, Ak, B, D)) {
                lo = mid;
            } else {
                hi = mid - 1ll;
            }
        }
        */

        S.clear();
        while (!que.empty()) que.pop();

        que.push({1, Hd, Ad, Hk, Ak});

        int ans = -1;

        for (int i = 0 ; !que.empty() ; ++i) {
            auto top = que.front();
            que.pop();

            if (S.find({{top.H1, top.A1}, {top.H2, top.A2}}) != S.end()) {
                --i;
                continue;
            }
            S.insert({{top.H1, top.A1}, {top.H2, top.A2}});

            // cerr << top.round << " | " << top.H1 << " " << top.A1 << " # " << top.H2 << " " << top.A2 << endl;
            if (top.A1 >= top.H2) {
                ans = top.round;
                break;
            }

            if (top.A2 != 0) {
                // decrease atk
                int nwAtk = max(0, top.A2 - D);
                if (nwAtk < top.H1)
                que.push({top.round+1, top.H1 - nwAtk, top.A1, top.H2, nwAtk});
            }
            if (top.A2 < top.H1) {
                // bulk up
                que.push({top.round+1, top.H1 - top.A2, top.A1 + B, top.H2, top.A2});
                // attack
                que.push({top.round+1, top.H1 - top.A2, top.A1, top.H2 - top.A1, top.A2});
            }
            if (top.H1 < Hd) {
                // heal
                if (top.A2 < Hd)
                que.push({top.round+1, Hd - top.A2, top.A1, top.H2, top.A2});
            }
        }

        cout << "Case #" << Case << ": ";
        if (ans == -1) cout << "IMPOSSIBLE" << endl;
        else cout << ans << endl;

        cerr << Case << endl;
    }

    return 0;
}

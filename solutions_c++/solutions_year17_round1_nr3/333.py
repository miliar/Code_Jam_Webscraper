#include <bits/stdc++.h>

using namespace std;

struct state_t{
    int Hd, Ad, Hk, Ak;
};

bool operator<(const state_t& lhs, const state_t &rhs) {
    return make_pair(make_pair(make_pair(lhs.Hd, lhs.Ad), lhs.Hk), lhs.Ak) < 
           make_pair(make_pair(make_pair(rhs.Hd, rhs.Ad), rhs.Hk), rhs.Ak);
}

int main() {
    int T;
    scanf("%d", &T);
    for (int tc = 1; tc <= T; tc++) {
        int Hd, Ad, Hk, Ak, B, D;
        queue<pair<state_t, int>> q;

        scanf("%d %d %d %d %d %d", &Hd, &Ad, &Hk, &Ak, &B, &D);

        q.push(make_pair(state_t({Hd, Ad, Hk, Ak}), 1));

        map<state_t, bool> visited;
        visited[q.front().first] = true;

        int turn = -1;
        while (!q.empty()) {
            state_t s = q.front().first;
            int st = q.front().second;
            q.pop();


            if (s.Hd <= 0)
                continue;

            if (s.Hk <= s.Ad) {
                turn = st;
                break;
            }

            if (s.Hd < Hd) {
                state_t nstate({Hd - s.Ak, s.Ad, s.Hk, s.Ak});
                if (!visited[nstate]) {
                    visited[nstate] = true;
                    q.push({nstate, st + 1});
                }
            }

            if (s.Ak > 0) {
                int atk = max(0, s.Ak - D);
                state_t nstate({s.Hd - atk, s.Ad, s.Hk, atk});
                if (!visited[nstate]) {
                    visited[nstate] = true;
                    q.push({nstate, st + 1});
                }
            }

            state_t nstate = state_t({s.Hd - s.Ak, s.Ad + B, s.Hk, s.Ak});
            if (!visited[nstate]) {
                visited[nstate] = true;
                q.push({nstate, st + 1});
            }

            nstate = state_t({s.Hd - s.Ak, s.Ad, s.Hk - s.Ad, s.Ak});
            if (!visited[nstate]) {
                visited[nstate] = true;
                q.push({nstate, st + 1});
            }
        }
        printf("Case #%d: ", tc);
        if (turn == -1)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", turn);
    }
    return 0;
}

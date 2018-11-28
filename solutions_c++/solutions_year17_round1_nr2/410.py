#include <bits/stdc++.h>
using namespace std;

int Q[55][55];
typedef pair<int, int> pii;
pii seg[55][55];
#define fst first
#define snd second

int main(void) {
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++ t) {
        int N, P;
        cin >> N >> P;
        vector<int> R(N);
        for (int i = 0; i < N; ++ i) {
            cin >> R[i];
        }

        for (int i = 0; i < N; ++ i) {
            for (int j = 0; j < P; ++ j) {
                cin >> Q[i][j];
                int ub = Q[i][j] * 10.0 / (9 * R[i]);
                int lb = ceil(Q[i][j] * 10.0 / (11 * R[i]));
                seg[i][j] = pii(lb, ub);
            //    cerr << i << ' ' << j << ": " << lb << ' ' << ub << endl;
            }
            sort(begin(seg[i]), begin(seg[i]) + P);
        }


        int ans = 0;
        if (N == 1) {
            for (int j = 0; j < P; ++ j) {
                int ub = Q[0][j] * 10.0 / (9 * R[0]);
                int lb = ceil(Q[0][j] * 10.0 / (11 * R[0]));
                if (ub >= lb) ++ ans;
            }
        } else if (N >= 2) {
            priority_queue<int, vector<int>, greater<int>> pq[50];
            vector<int> k(N, 0);
            for (int j = 0; j < P; ++ j) {
                int li = seg[0][j].fst, ui = seg[0][j].snd;
                if (ui < li) continue;

                bool flag = true;
                for (int i = 1; i < N; ++ i) {
                    while (k[i] < P and seg[i][k[i]].snd < li) ++ k[i];
                    while (!pq[i].empty() && pq[i].top() < li) pq[i].pop();

                    while (k[i] < P and seg[i][k[i]].fst <= ui) {
                        if (seg[i][k[i]].fst <= seg[i][k[i]].snd)
                            pq[i].push(seg[i][k[i]].snd);
                        ++ k[i];
                    }
                    if (pq[i].empty()) flag = false;
                }
                if (flag) {
                    ++ ans;
                }
            }
        }

        cout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}

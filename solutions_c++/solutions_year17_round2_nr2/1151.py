#include <bits/stdc++.h>
using namespace std;

const int kN = 1e3 + 10;
char S[3] = {'R', 'Y', 'B'};

int main(int argc, char** argv) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T, t = 1;
    cin >> T;
    while (t <= T) {
        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;
        cout << "Case #" << t++ << ": ";
        int M = N >> 1;
        if (R > M || Y > M || B > M) cout << "IMPOSSIBLE\n";
        else {
            vector<pair<int, int>> C{{R, 0}, {Y, 1}, {B, 2}};
            sort(C.begin(), C.end(), greater<pair<int, int>>());
            string out(N, S[C[0].second]);
            //cout << C[0].second << " " << C[1].second << " " << C[2].second << endl;
            //cout << C[0].first << " " << C[1].first << " " << C[2].first << endl;

            int i, col, cnt, last_ind0 = (C[0].first - 1) << 1;
            for (i = N - 1, col = 0; i > last_ind0; --i, col ^= 1) {
                //cout << i << " " << col << " " << cnt << " " << C[1].first << " " << C[2].first << "::\n";
                if (col && C[2].first > 0) {
                    out[i] = S[C[2].second];
                    C[2].first--;
                } else {
                    C[1].first--;
                    out[i] = S[C[1].second];
                }
            }
            if (C[1].first < C[2].first) swap(C[1], C[2]);
            for (i = 1, col = 0, cnt = 1; i < last_ind0; i += 2, col ^= 1) {
                //cout << i << " " << col << " " << cnt << " " << C[1].first << " " << C[2].first << "::\n";
                if (col && C[2].first > 0) {
                    out[i] = S[C[2].second];
                    C[2].first--;
                } else {
                    C[1].first--;
                    out[i] = S[C[1].second];
                }
            }
            cout << out << "\n";
        }
    }
    return 0;
}

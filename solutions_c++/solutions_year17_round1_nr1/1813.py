#include <bits/stdc++.h>
using namespace std;

int main(int argc, char** argv) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T, t = 1;
    cin >> T;
    while (t <= T) {
        int R, C;
        cin >> R >> C;
        string S[R];
        vector<pair<int, int>> V;
        int f_row = -1;
        for (int i = 0; i < R; ++i) {
            cin >> S[i];
            for (int j = 0; j < C; ++j) {
                if (S[i][j] != '?') {
                    V.push_back({i, j});
                    if (f_row < 0) f_row = i;
                }
            }
        }
        for (int i = 0; i < V.size(); ++i) {
            int r = V[i].first, c = V[i].second;
            char ch = S[r][c];
            for (int j = c - 1; j >= 0; --j) {
                if (S[r][j] == '?') S[r][j] = ch;
                else break;
            }
            for (int j = c + 1; j < C; ++j) {
                if (S[r][j] == '?') S[r][j] = ch;
                else break;
            }
        }

        for (int i = 0; i < R; ++i) {
            if (S[i][0] == '?') {
                if (i == 0) {
                    for (int j = 0; j < f_row; ++j) {
                        S[j] = S[f_row];
                    }
                } else S[i] = S[i - 1];
            }
        }
        cout << "Case #" << t++ << ": " << "\n";
        for (int i = 0; i < R; ++i) {
            cout << S[i] << "\n";
        }
    }
    return 0;
}

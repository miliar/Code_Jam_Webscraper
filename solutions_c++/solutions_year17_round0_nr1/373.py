#include <bits/stdc++.h>

using namespace std;

int T, K;
string S;

int main() {
    ifstream fin("A.in");
    ofstream fout("A.out");

    fin >> T;
    for (int t = 1; t <= T; t++) {
        fin >> S >> K;
        fout << "Case #" << t << ": ";

        int ans = 0;

        for (int i = 0; i <= (int)S.size() - K; i++) {
            if (S[i] == '-') {
                ++ans;
                for (int j = 0; j < K; j++) {
                    if (S[i + j] == '+') S[i + j] = '-';
                    else S[i + j] = '+';
                }
            }
        }

        for (int i = (int)S.size() - K + 1; i < (int)S.size(); i++) {
            if (S[i] == '-') {
                ans = -1;
                break;
            }
        }

        if (ans == -1) fout << "IMPOSSIBLE\n";
        else fout << ans << "\n";
    }

    fin.close();
    fout.close();

    return 0;
}

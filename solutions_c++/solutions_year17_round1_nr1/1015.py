#include <bits/stdc++.h>
using namespace std;

#define MAX 100
char grid[MAX][MAX];

int main() {

    ifstream cin ("input.txt");
    ofstream cout ("ans.txt");

    int T; cin >> T;
    for (int t = 1; t <= T; t++) {

        int N, M; cin >> N >> M;
        for (int i = 1; i <= N; i++) {
            string s; cin >> s;
            for (int k = 1; k <= M; k++) {
                grid[i][k] = s[k - 1];
            }
        }

        for (int i = 1; i <= N; i++) {
            for (int k = 1; k <= M; k++) {
                if (grid[i][k] == '?') continue;
                char cur = grid[i][k];
                int j = k - 1;
                while (j >= 1 && grid[i][j] == '?') {
                    grid[i][j] = cur;
                    j--;
                }

                j = k + 1;
                while (j <= M && grid[i][j] == '?') {
                    grid[i][j] = cur;
                    j++;
                }
            }
        }

        for (int i = 1; i <= N; i++) {
            for (int k = 1; k <= M; k++) {
                if (grid[i][k] == '?') continue;

                // go up
                for (int a = i - 1; a >= 0; a--) {
                    if (grid[a][k] != '?') break;
                    grid[a][k] = grid[i][k];
                }
                // go down
                for (int a = i +  1; a <= N; a++) {
                    if (grid[a][k] != '?') break;
                    grid[a][k] = grid[i][k];
                }
            }
        }
        cout << "Case #" << t << ":\n";
        for (int i = 1; i <= N; i++) {
            for (int k = 1; k <= M; k++) {
                cout << grid[i][k];
            } cout << "\n";
        }
    }

    return 0;
}
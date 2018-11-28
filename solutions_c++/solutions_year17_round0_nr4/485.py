#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair

#define MAX 101
int N, M, ans;
char grid[MAX][MAX];
char sol[MAX][MAX];


void print_() {
    for (int i = 0; i < N; i++) {
        for (int k = 0; k < N; k++)
            cout << sol[i][k];
        cout << "\n";
    }
}

int main() {

    ifstream cin ("input.txt");
    ofstream cout ("ans.txt");

    int T; cin >> T;
    for (int t = 1; t <= T; t++) {

        cin >> N >> M;
        for (int i = 0; i < N; i++) {
            for (int k = 0; k < N; k++)
                sol[i][k] = grid[i][k] = '.';
        }

        for (int i = 0; i < M; i++) {
            char cur; cin >> cur;
            int r, c; cin >> r >> c;
            r--, c--;
            grid[r][c] = cur;
        }

        int indx = -1;
        vector<pair<int, int> > change;
        vector<char> type;

        // find x or o
        for (int i = 0; i < N; i++) {
            if (grid[0][i] == 'o') {
                indx = i;
                break;
            } else if (grid[0][i] == 'x') {
                indx = i;
                break;
            }
        }

        for (int i = 0; i < N; i++) {
            sol[0][i] = '+';
        }

        if (indx == -1) indx = 0;

        sol[0][indx] = 'o';

        if (indx != N - 1) {
            int row = 1;
            for (int i = 0; i < N; i++, row++) {
                if (sol[0][i] == 'o') {
                    i++;
                }
                sol[row][i] = 'x';
            }
        } else {
            for (int i = N - 2, k = 1; i >= 0; i--, k++) {
                sol[k][i] = 'x';
            }
        }

        for (int i = 1; i < N - 1; i++) {
            sol[N - 1][i] = '+';
        }

        cout << "Case #" << t << ": ";
        // cout << "\n"; print_();

        int amnt = 0;
        for (int i = 0; i < N; i++) {
            for (int k = 0; k < N; k++) {
                if (sol[i][k] != '.' || grid[i][k] != '.') amnt++;
                if (grid[i][k] != sol[i][k]) {
                    type.pb(sol[i][k]);
                    change.pb(mp(i, k));
                }
            }
        }

        cout << amnt + 1 << " " << change.size() << "\n";
        for (int i = 0; i < change.size(); i++) {
            cout << type[i] << " " << change[i].first + 1 << " " << change[i].second + 1 << "\n";
        }
    }

    return 0;
}
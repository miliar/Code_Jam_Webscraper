#include <bits/stdc++.h>

using namespace std;

const int MAX_N = 110;
int T, N, M;
int grid[MAX_N][MAX_N];
int match[MAX_N << 2];
bool changes[MAX_N][MAX_N];
bool nu_r[MAX_N], nu_c[MAX_N], nu_s[MAX_N << 1], nu_d[MAX_N << 1];
bool visited[MAX_N << 1];
bool adj[MAX_N << 2][MAX_N << 2];

bool aug_path(int v) {
    if (visited[v]) return false;
    visited[v] = true;
    for (int i = 0; i < 4 * N; i++) {
        if (!adj[v][i]) continue;
        if (match[i] == -1 || aug_path(match[i])) {
            match[i] = v;
            return true;
        }
    }
    return false;
}

int main() {
    ifstream fin("D.in");
    ofstream fout("D.out");

    fin >> T;
    for (int t = 1; t <= T; t++) {
        fout << "Case #" << t << ": ";
        fin >> N >> M;

        memset(grid, 0, sizeof(grid));
        memset(changes, false, sizeof(changes));
        memset(adj, false, sizeof(adj));
        memset(nu_r, false, sizeof(nu_r));
        memset(nu_c, false, sizeof(nu_c));
        memset(nu_s, false, sizeof(nu_s));
        memset(nu_d, false, sizeof(nu_d));
        fill(match, match + (MAX_N << 2), -1);

        int ans = 0, added = 0;
        for (int i = 0; i < M; i++) {
            char type;
            int x, y;
            fin >> type >> x >> y;
            --x; --y;
            if (type == 'x' || type == 'o') {
                ++ans;
                ++grid[x][y];
                nu_r[x] = true;
                nu_c[y] = true;
            }
            if (type == '+' || type == 'o') {
                ++ans;
                grid[x][y] += 2;
                nu_s[x + y] = true;
                nu_d[x - y + N] = true;
            }
        }

        int a = 0, b = 0;
        while (a < N && b < N) {
            if (nu_r[a]) ++a;
            else if (nu_c[b]) ++b;
            else {
                ++ans;
                ++grid[a][b];
                if (!changes[a][b]) {
                    changes[a][b] = true;
                    ++added;
                }
                ++a; ++b;
            }
        }

        for (int i = 0; i < 2 * N - 1; i++) {
            if (nu_s[i]) continue;
            for (int j = max(-i, i - 2 * N + 1); j < min(i + 1, 2 * N - i); j++) {
                if ((i + j) % 2 != 0 || nu_d[j + N]) continue;
                adj[i][j + 3 * N] = adj[j + 3 * N][i] = true;
            }
        }

        for (int i = 0; i < 2 * N - 1; i++) {
            if (nu_s[i]) continue;
            memset(visited, false, sizeof(visited));
            ans += (int)aug_path(i);
        }

        for (int j = -N + 1; j < N; j++) {
            if (nu_d[j + N]) continue;
            int i = match[j + 3 * N];
            if (i == -1) continue;
            int x = (i + j) / 2, y = (i - j) / 2;
            grid[x][y] += 2;
            if (!changes[x][y]) {
                changes[x][y] = true;
                ++added;
            }
        }

        fout << ans << " " << added << "\n";
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (!changes[i][j]) continue;
                if (grid[i][j] == 3) fout << "o ";
                else if (grid[i][j] == 1) fout << "x ";
                else fout << "+ ";
                fout << i + 1 << " " << j + 1 << "\n";
            }
        }
    }

    fin.close();
    fout.close();

    return 0;
}

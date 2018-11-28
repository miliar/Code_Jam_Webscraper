#include <cstdio>
#include <cassert>
#include <algorithm>
#include <iterator>
#include <numeric>
#include <vector>
using namespace std;

bool adj[202][202];
bool vis[101], sel[101];

void either(int a, int b) {
    adj[a ^ 1][b] = adj[b ^ 1][a] = true;
}
void dfs(int i, int n) {
    vis[i / 2] = true;
    sel[i / 2] = i % 2;
    for(int j = 0; j < n; j++)
        if(!vis[j / 2] && adj[i][j])
            dfs(j, n);
}
bool solve_2sat(int n) {
    for(int k = 0; k < n; k++)
        for(int i = 0; i < n; i++)
            if(adj[i][k])
                for(int j = 0; j < n; j++)
                    if(adj[k][j])
                        adj[i][j] = true;
    if(adj[1][0])
        return false;
    for(int i = 2; i < n; i += 2)
        if(adj[i][i + 1] && adj[i + 1][i])
            return false;
    fill_n(vis, n / 2, false);
    fill_n(sel, n / 2, false);
    dfs(1, n);
    for(int i = 2; i < n; i += 2)
        if(!vis[i / 2])
            dfs(i + adj[i][i + 1], n);
    return true;
}

char s[50][51];
vector<int> v[50][50];

constexpr int dx[4] = {1, 0, -1, 0};
constexpr int dy[4] = {0, 1, 0, -1};

void solve(int r, int c) {
    for(int i = 0; i < 202; i++)
        fill_n(adj[i], 202, false);
    for(int i = 0; i < r; i++)
        for(int j = 0; j < c; j++)
            if(s[i][j] == '|')
                s[i][j] = '-';
    int n = 2;
    for(int i = 0; i < r; i++) {
        for(int j = 0; j < c; j++) {
            if(s[i][j] == '-') {
                for(int ii = i + 1, jj = j, d = 1; ii >= 0 && ii < r && jj >= 0 && jj < c && s[ii][jj] != '#'; ii += dy[d], jj += dx[d]) {
                    if(s[ii][jj] == '-') {
                        either(0, n);
                        break;
                    } else if(s[ii][jj] == '.') {
                        v[ii][jj].push_back(n + 1);
                    } else if(s[ii][jj] == '/') {
                        d = 3 - d;
                    } else if(s[ii][jj] == '\\') {
                        d ^= 1;
                    }
                }
                for(int ii = i - 1, jj = j, d = 3; ii >= 0 && ii < r && jj >= 0 && jj < c && s[ii][jj] != '#'; ii += dy[d], jj += dx[d]) {
                    if(s[ii][jj] == '-') {
                        either(0, n);
                        break;
                    } else if(s[ii][jj] == '.') {
                        v[ii][jj].push_back(n + 1);
                    } else if(s[ii][jj] == '/') {
                        d = 3 - d;
                    } else if(s[ii][jj] == '\\') {
                        d ^= 1;
                    }
                }
                for(int ii = i, jj = j + 1, d = 0; ii >= 0 && ii < r && jj >= 0 && jj < c && s[ii][jj] != '#'; ii += dy[d], jj += dx[d]) {
                    if(s[ii][jj] == '-') {
                        either(0, n + 1);
                        break;
                    } else if(s[ii][jj] == '.') {
                        v[ii][jj].push_back(n);
                    } else if(s[ii][jj] == '/') {
                        d = 3 - d;
                    } else if(s[ii][jj] == '\\') {
                        d ^= 1;
                    }
                }
                for(int ii = i, jj = j - 1, d = 2; ii >= 0 && ii < r && jj >= 0 && jj < c && s[ii][jj] != '#'; ii += dy[d], jj += dx[d]) {
                    if(s[ii][jj] == '-') {
                        either(0, n + 1);
                        break;
                    } else if(s[ii][jj] == '.') {
                        v[ii][jj].push_back(n);
                    } else if(s[ii][jj] == '/') {
                        d = 3 - d;
                    } else if(s[ii][jj] == '\\') {
                        d ^= 1;
                    }
                }
                n += 2;
            }
        }
    }
    for(int i = 0; i < r; i++)
        for(int j = 0; j < c; j++)
            if(s[i][j] == '.') {
                v[i][j].resize(2);
                either(v[i][j][0], v[i][j][1]);
                v[i][j].clear();
            }
    if(!solve_2sat(n)) {
        puts("IMPOSSIBLE");
        return;
    }
    puts("POSSIBLE");
    int m = 0;
    for(int i = 0; i < r; i++)
        for(int j = 0; j < c; j++)
            if(s[i][j] == '-' && sel[++m])
                s[i][j] = '|';
    for(int i = 0; i < r; i++)
        puts(s[i]);
}
int main() {
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++) {
        int r, c;
        scanf("%d %d", &r, &c);
        for(int j = 0; j < r; j++)
            scanf("%s", s[j]);
        printf("Case #%d: ", i);
        solve(r, c);
        // int y = gety(n, c, m);
        // int z = getz(n, c, m, y);
        // printf("Case #%d: %d %d\n", i, y, z);
    }
}

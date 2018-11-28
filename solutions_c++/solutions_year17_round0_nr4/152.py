#include <bits/stdc++.h>

using namespace std;

typedef long long LL;


const int N = 110;
int n, m;
char mat[N][N], mat2[N][N];
int match[2*N];
bool flag[2][2*N];
bool vis[2*N];
vector<int> E[2*N];

int dfs(int i) {
    for (auto j : E[i]) if (!vis[j]) {
        vis[j] = 1;
        if (match[j] < 0 || dfs(match[j])) {
            match[j] = i;
            return 1;
        }
    }
    return 0;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int _ = 1; _ <= T; _++) {
        scanf("%d%d", &n, &m);
        memset(mat, 0, sizeof(mat));
        memset(flag, 0, sizeof(flag));
        set<int> S;
        for (int i = 0; i < n; i++) S.insert(i);
        for (int k = 0; k < m; k++) {
            char c;
            int i, j;
            scanf(" %c%d%d", &c, &i, &j); 
            i--, j--;
            mat[i][j] = c;
            if (c == 'x' || c == 'o') S.erase(j);
            if (c == '+' || c == 'o') {
                flag[0][i + j] = 1;
                flag[1][j - i + n - 1] = 1;
            }
        }
        memcpy(mat2, mat, sizeof(mat));
        for (int i = 0; i < n; i++) {
            bool flag = 1;
            for (int j = 0; j < n; j++) if (mat[i][j] == 'x' || mat[i][j] == 'o') {
                flag = 0;
                break;
            }
            if (flag) {
                int j = *S.begin();
                mat[i][j] = mat[i][j] == '+' ? 'o' : 'x';
                S.erase(j);
            }
        }
        for (int i = 0; i <= 2*(n-1); i++) E[i].clear();
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) 
                if (!flag[0][i + j] && !flag[1][j - i + n - 1]) 
                    E[i + j].push_back(j - i + n - 1);
        memset(match, -1, sizeof(match));
        for (int i = 0; i <= 2*(n-1); i++) {
            memset(vis, 0, sizeof(vis));
            dfs(i);
        }
        for (int i = 0; i <= 2*(n-1); i++) if (match[i] != -1) {
            int x = (match[i] - i + n - 1) / 2;
            int y = (match[i] + i - n + 1) / 2;
            mat[x][y] = mat[x][y] == 'x' ? 'o' : '+';
        }
        int sum = 0, num = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == '+' || mat[i][j] == 'x') sum++;
                if (mat[i][j] == 'o') sum += 2;
                if (mat[i][j] != mat2[i][j]) num++;
            }
        printf("Case #%d: %d %d\n", _, sum, num);
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) 
                if (mat[i][j] != mat2[i][j]) printf("%c %d %d\n", mat[i][j], i + 1, j + 1);
    }
    return 0;
}

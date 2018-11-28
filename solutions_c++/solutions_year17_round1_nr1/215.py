#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

const int N = 5555;

int T, cas;

int n, m, x[2][50], y[2][50], v[50]; char ch[50][50];

bool Check(int id) {
    if (!x[0][id] || !y[0][id] || x[1][id] > n || y[1][id] > m)
        return false;
    for (int i = 0; i < 26; i ++)
        if (v[i] && i != id) {
            int rx = min(x[1][id], x[1][i]);
            int lx = max(x[0][id], x[0][i]);
            int ry = min(y[1][id], y[1][i]);
            int ly = max(y[0][id], y[0][i]);
            if (ry >= ly && rx >= lx) return false;
        }
    return true;
}

int main() {
    freopen("A-large (1).in", "r", stdin);
    freopen("A.out", "w", stdout);
    cin >> T;
    while (T --) {
        cin >> n >> m;
        memset(ch, 0, sizeof(ch));
        for (int i = 1; i <= n; i ++) {
            scanf(" %s", ch[i] + 1);
//            if (cas == 30) {
//                cout << "!!!" << ch[i]+1 << endl;
//            }
        }
        memset(x, 0, sizeof(x));
        memset(y, 0, sizeof(y));
        memset(v, 0, sizeof(v));
        for (int i = 1; i <= n; i ++)
            for (int j = 1; j <= m; j ++) {
                if (ch[i][j] == '?') continue;
                int t = ch[i][j] - 'A';
                x[0][t] = x[1][t] = i;
                y[0][t] = y[1][t] = j;
                v[t] = true;
            }
        for (int a = 1; a <= n; a ++)
        for (int b = 1; b <= m; b ++) {
            if (ch[a][b] != '?') {
                int i = ch[a][b] - 'A';
                while (Check(i)) x[0][i] --; x[0][i] ++;
                while (Check(i)) x[1][i] ++; x[1][i] --;
            }
        }
        for (int a = 1; a <= n; a ++)
        for (int b = 1; b <= m; b ++) {
            if (ch[a][b] != '?') {
                int i = ch[a][b] - 'A';
                while (Check(i)) y[0][i] --; y[0][i] ++;
                while (Check(i)) y[1][i] ++; y[1][i] --;
            }
        }
//        for (int i = 0; i < 26; i ++) {
//            if (v[i]) {
//            }
//        }

        for (int c = 0; c < 26; c ++) {
            for (int i = x[0][c]; i <= x[1][c]; i ++)
            for (int j = y[0][c]; j <= y[1][c]; j ++)
                ch[i][j] = c + 'A';
        }
        printf("Case #%d:\n", ++ cas);
        for (int i = 1; i <= n; i ++) {
            printf("%s\n", ch[i] + 1);
        }
    }
}

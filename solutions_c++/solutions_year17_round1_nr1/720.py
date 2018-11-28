#include <bits/stdc++.h>
using namespace std;

#define INF 0X3F3F3F3F
#define INFL 0x3F3F3F3F3F3F3F3FLL
#define MOD 1000000007
#define st first
#define nd second
#define pb push_back
#define mp make_pair
#define sz(X) int((X).size())
#define all(X) (X).begin(), (X).end()
#define rall(X) (X).rbegin(), (X).rend()
#define pow2(X) ((X)*(X))

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef long long ll;
typedef vector<ll> vll;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

const int N = 32;

int tt, n, m, expanded[N][N];
char mat[N][N], ans[N][N], init;

int ok(int row, int col, int l, int r, int u, int d) {
    char c = mat[row][col];
    for (int i = row-u; i <= row+d; i++) {
        for (int j = col-l; j <= col+r; j++) {
            if (expanded[i][j]) return 0;
            if (mat[i][j] != '?' and mat[i][j] != c) return 0;
        }
    }
    return 1;
}

void expand(int row, int col) {
    char c = mat[row][col];
    int L = -1, U = -1, R = -1, D = -1;
    for (int l = m; l >= 0; l--) {
        if (col - l < 1) continue;
        for (int u = n; u >= 0; u--) {
            if (row - u < 1) continue;
            for (int r = m; r >= 0; r--) {
                if (col + r > m) continue;
                for (int d = n; d >= 0; d--) {
                    if (row + d > n) continue;
                    if (!ok(row,col,l,r,u,d)) continue;
                    if (l > L) {
                        L = l, U = u, R = r, D = d;
                    } else if (l == L and u > U) {
                        L = l, U = u, R = r, D = d;
                    } else if (l == L and u == U and r > R) {
                        L = l, U = u, R = r, D = d;
                    } else if (l == L and u == U and r == R and d > D) {
                        L = l, U = u, R = r, D = d;
                    }
                }
            }
        }
    }
    for (int i = row-U; i <= row+D; i++) {
        for (int j = col-L; j <= col+R; j++) {
            expanded[i][j] = 1;
            ans[i][j] = c;
        }
    }
}

int main() {
    scanf("%d", &tt);
    for (int t = 1; t <= tt; t++) {
        printf("Case #%d:\n", t);
        init = '?';
        scanf("%d %d", &n, &m);
        memset(ans, '?', sizeof(ans));
        memset(expanded, 0, sizeof(expanded));
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                scanf(" %c", &mat[i][j]);
            }
            ans[i][m+1] = 0;
        }
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++)
                if (mat[i][j] != '?' and !expanded[i][j])
                    expand(i, j);
        for (int i = 1; i <= n; i++)
            puts(ans[i]+1);
    }
    return 0;
}
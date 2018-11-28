#include <bits/stdtr1c++.h>

#define clr(ar) memset(ar, 0, sizeof(ar))
#define read() freopen("lol.txt", "r", stdin)
#define write() freopen("out.txt", "w", stdout)
#define dbg(x) cout << #x << " = " << x << endl
#define ran(a, b) ((((rand() << 15) ^ rand()) % ((b) - (a) + 1)) + (a))

using namespace std;

int f, n;
bitset <1010> dp[3][1010][1010], visited[3][1010][1010];

inline bool F(int l, int r, int y, int b, int n){
    if (n == 0) return (l != f);
    if (visited[l][r][y][b]) return dp[l][r][y][b];

    bool res = false;
    if (l != 0 && r && !res) res = F(0, r - 1, y, b, n - 1);
    if (l != 1 && y && !res) res = F(1, r, y - 1, b, n - 1);
    if (l != 2 && b && !res) res = F(2, r, y, b - 1, n - 1);

    visited[l][r][y][b] = true;
    return (dp[l][r][y][b] = res);
}

void backtrack(int l, int r, int y, int b, int n){
    if (n == 0) return;

    if (l != 0 && r && F(0, r - 1, y, b, n - 1)){
        printf("R");
        return backtrack(0, r - 1, y, b, n - 1);
    }

    if (l != 1 && y && F(1, r, y - 1, b, n - 1)){
        printf("Y");
        return backtrack(1, r, y - 1, b, n - 1);
    }

    if (l != 2 && b && F(2, r, y, b - 1, n - 1)){
        printf("B");
        return backtrack(2, r, y, b - 1, n - 1);
    }
}

int main(){
    read();
    write();
    unsigned long long h = 0;
    int T = 0, t, i, j, k, l, r, o, y, g, b, v, res, found;

    scanf("%d", &t);
    while (t--){
        scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);

        found = 0;
        for (f = 0; f < 3; f++){
            for (i = 0; i < 3; i++){
                for (j = 0; j < 1010; j++){
                    for (k = 0; k < 1010; k++){
                        visited[i][j][k].reset();
                    }
                }
            }

            if (f == 0 && r > 0){
                res = F(f, r - 1, y, b, n - 1);
                if (res){
                    found = 1;
                    printf("Case #%d: ", ++T);
                    printf("R");
                    backtrack(f, r - 1, y, b, n - 1);
                    puts("");
                    break;
                }
            }
            if (f == 1 && y > 0){
                res = F(f, r, y - 1, b, n - 1);
                if (res){
                    found = 1;
                    printf("Case #%d: ", ++T);
                    printf("Y");
                    backtrack(f, r, y - 1, b, n - 1);
                    puts("");
                    break;
                }
            }
            if (f == 2 && b > 0){
                res = F(f, r, y, b - 1, n - 1);
                if (res){
                    found = 1;
                    printf("Case #%d: ", ++T);
                    printf("B");
                    backtrack(f, r, y, b - 1, n - 1);
                    puts("");
                    break;
                }
            }
        }
        if (found == 0) printf("Case #%d: IMPOSSIBLE\n", ++T);

        h = h * 666666667 + found + 13;
    }

    fprintf(stderr, "hash = %llu\n", h);
    return 0;
}

#include <bits/stdtr1c++.h>

#define clr(ar) memset(ar, 0, sizeof(ar))
#define read() freopen("lol.txt", "r", stdin)
#define write() freopen("out.txt", "w", stdout)
#define dbg(x) cout << #x << " = " << x << endl
#define ran(a, b) ((((rand() << 15) ^ rand()) % ((b) - (a) + 1)) + (a))

using namespace std;

bool cameron[1442], jamie[1442];
unsigned char f, dp[721][721][2][1442];

int F(int c, int j, int l, int i){
    if (c > 720 || j > 720) return 250;
    if (i >= 1440){
        if (c == 720 && j == 720) return (f != l);
        return 250;
    }
    if (dp[c][j][l][i] != 255) return dp[c][j][l][i];

    int x, y, res = 250;
    if (!cameron[i]){
        x = F(c + 1, j, 0, i + 1) + (l != 0);
        if (x < res) res = x;
    }

    if (!jamie[i]){
        x = F(c, j + 1, 1, i + 1) + (l != 1);
        if (x < res) res = x;
    }

    res = min(res, 250);
    return (dp[c][j][l][i] = res);
}

int main(){
    read();
    write();
    int T = 0, t, i, c, j, k, l, r, res;

    scanf("%d", &t);
    while (t--){
        scanf("%d %d", &c, &j);
        clr(cameron), clr(jamie);

        for (k = 0; k < c; k++){
            scanf("%d %d", &l, &r);
            for (i = l; i < r; i++) cameron[i] = true;
        }
        for (k = 0; k < j; k++){
            scanf("%d %d", &l, &r);
            for (i = l; i < r; i++) jamie[i] = true;
        }

        res = 250;
        f = 0, memset(dp, -1, sizeof(dp));
        if (!cameron[0]) res = min(res, (int)F(1, 0, 0, 1));
        f = 1, memset(dp, -1, sizeof(dp));
        if (!jamie[0]) res = min(res, (int)F(0, 1, 1, 1));

        assert(res <= (j + c + 4));
        printf("Case #%d: %d\n", ++T, res);
        fprintf(stderr, "Case #%d: %d\n", T, res);
    }
    return 0;
}

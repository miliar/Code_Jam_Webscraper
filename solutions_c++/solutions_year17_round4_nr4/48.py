#include <bits/stdc++.h>

#define foreach(i,v) for(auto&& i: v)
#define all(x) (x).begin(), (x).end()

typedef std::vector< std::string > VS;
typedef std::vector<int> VI;
typedef long long ll;

template <class C> C& mini(C& a, C b) { if (b < a) a = b; return a; }
template <class C> C& maxi(C& a, C b) { if (a < b) a = b; return a; }

using namespace std;

int C, R, M;
char F[32][32];
int mt[32][32];
int nt;
vector<pair<int, int>> S;

void flowt(int x, int y, int m) {
    int mm = 1 << m;
    for (int i = x-1; F[i][y] != '#'; i--)
        mt[i][y] |= mm;
    for (int i = x+1; F[i][y] != '#'; i++)
        mt[i][y] |= mm;
    for (int i = y-1; F[x][i] != '#'; i--)
        mt[x][i] |= mm;
    for (int i = y+1; F[x][i] != '#'; i++)
        mt[x][i] |= mm;
}

int vis[1024][32][32];
struct Pos {
    int x, y, mask, mov;
};

Pos Q[1024*32*32*10];
const int dx[] = { -1, 1, 0, 0};
const int dy[] = { 0, 0, -1, 1};
int can[10][10][1024];

void flowS(int x, int y, int ss) {
    memset(vis, -1, sizeof(vis));
    vis[0][x][y] = 1;
    int qs = 0, qf = 1;
    Q[0] = {x, y, 0, 0};
    while (qs < qf) {
        Pos& c = Q[qs++];
        int mask = c.mask | mt[c.x][c.y];
        {
            int tm = mask ^ c.mask;
            if (tm) {
                for (int i = 0; i < 10 && tm; i++) {
                    if (tm & (1 << i)) {
                        can[ss][i][c.mask] = 1;
                        tm ^= (1 << i);
                    }
                }
            }
        }
        int mov = c.mov + 1;
        if (mov > M)
            continue;
        for (int i = 0; i < 4; i++) {
            int x = c.x + dx[i];
            int y = c.y + dy[i];
            if (F[x][y] != '#' && vis[mask][x][y] < 0) {
                vis[mask][x][y] = mov;
                Q[qf++] = {x, y, mask, mov};
            }
        }
    }
}

void fcan() {
    for (int i = 0; i < 10; i++)
        for (int j = 0; j < 10; j++)
            for (int m = 0; m < 1024; m++)
                if (can[i][j][m])
                    for (int k = 0; k < 10; k++)
                        can[i][j][m | (1 << k)] = 1;
}

int dp[1024][1024];
int nnext[1024][1024];

int dfs(int ms, int mt) {
    int &ret = dp[ms][mt];
    if (ret >= 0)
        return ret;

    ret = 0;

    for (int i = 0; i < 10; i++)
        if (ms & (1 << i))
            for (int j = 0; j < 10; j++)
                if (mt & (1 << j))
                    if (can[i][j][((1 << nt) - 1) ^ mt]) {
                        int tt = 1 + dfs(ms ^ (1 << i), mt ^ (1 << j));
                        if (tt > ret) {
                            ret = tt;
                            nnext[ms][mt] = i * 1024 + j;
                        }
                    }

    return ret;
}

int main(int argc, const char* argv[]) {
    int T;
    scanf("%d\n", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d%d%d\n", &C, &R, &M);
        memset(F, '#', sizeof(F));
        for (int i = 1; i <= R; i++) {
            for (int j = 1; j <= C; j++)
                scanf("%c", &F[i][j]);
            scanf("\n");
        }
//        printf("%.*s\n", 32, F[2]);
        nt = 0;
        memset(mt, 0, sizeof(mt));
        S.clear();
        memset(can, 0, sizeof(can));
        for (int i = 1; i <= R; i++)
            for (int j = 1; j <= C; j++)
                if (F[i][j] == 'T')
                    flowt(i, j, nt++);
                else if (F[i][j] == 'S')
                    S.push_back({i, j});
        for (int i = 0; i < S.size(); i++)
            flowS(S[i].first, S[i].second, i);
        fcan();
        memset(dp, -1, sizeof(dp));
        memset(nnext, -1, sizeof(nnext));
        for (int i = 0; i < 1024; i++)
            dp[i][0] = dp[0][i] = 0;
        int ms1 = (1 << S.size()) - 1;
        int mt1 = (1 << nt) - 1;
        printf("Case #%d: %d\n", t, dfs(ms1, mt1));
        while (nnext[ms1][mt1] >= 0) {
            int i = nnext[ms1][mt1] / 1024;
            int j = nnext[ms1][mt1] % 1024;
            printf("%d %d\n", i + 1, j + 1);
            ms1 ^= (1 << i);
            mt1 ^= (1 << j);
        }
    }
    return 0;
}

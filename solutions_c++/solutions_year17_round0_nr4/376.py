#include <bits/stdc++.h>

const int N = 111, V = N * 6;
int cc = 0;
int pnum[2][N][N], snum[2][N][N];
char G0[N][N], G[N][N];
int nG[N][N];

const int MAXN=V;
int uN,vN;  //u,v数目
int g[MAXN][MAXN];//编号是0~n-1的 
int linker[MAXN];
bool used[MAXN], banu[MAXN], banv[MAXN];
bool dfs(int u)
{
    int v;
    for(v=0;v<vN;v++)
        if(g[u][v]&&!used[v] && !banv[v])
        {
            used[v]=true;
            if(linker[v]==-1||dfs(linker[v]))
            {
                linker[v]=u;
                return true;
            }    
        }  
    return false;  
}    
int hungary()
{
    int res=0;
    int u;
    for (int i = 0; i < vN; ++ i)
        if (!banv[i]) linker[i] = -1;
    for(u=0;u<uN;u++) if (!banu[u])
    {
        memset(used,0,sizeof(used));
        if(dfs(u))  res++;
    } 
    return res;   
}

__inline void link(int u, int v) {
    g[u][v] = true;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);

    int T; std::cin >> T;
    for (int t = 1; t <= T; ++ t) {
        int n; std::cin >> n;
        uN = vN = n + 2 * n - 1;
        memset(g, false, sizeof g);
        memset(banu, false, sizeof banu);
        memset(banv, false, sizeof banv);
        for (int i = 1; i <= n; ++ i) {
            for (int j = 1; j <= n; ++ j) {
                pnum[0][i][j] = i - 1;
                pnum[1][i][j] = j - 1;
                snum[0][i][j] = n + j - i + n - 1;
                snum[1][i][j] = n + i + j - 2;
                G0[i][j] = G[i][j] = '.';
                nG[i][j] = 0;
            }
        }
        //std::cout << uN << " " << vN << std::endl;

        int m; std::cin >> m;
        while (m --) {
            char buf[3]; std::cin >> buf;
            int x, y; std::cin >> x >> y;
            G0[x][y] = buf[0];
            //std::cout << "set " << x << " " << y << " " << buf[0] << std::endl;
        }

        int ans = 0;
        for (int i = 1; i <= n; ++ i) {
            for (int j = 1; j <= n; ++ j) {
                //std::cout << i << " " << j << " " << pnum[0][i][j] << " " << pnum[1][i][j] << " " << snum[0][i][j] << " " << snum[1][i][j] << std::endl;
                if (G0[i][j] == '.') {
                    link(pnum[0][i][j], pnum[1][i][j]);
                    link(snum[0][i][j], snum[1][i][j]);
                }
                else if (G0[i][j] == 'x') {
                    ++ ans;
                    link(snum[0][i][j], snum[1][i][j]);
                    linker[pnum[1][i][j]] = pnum[0][i][j];
                    banu[pnum[0][i][j]] = banv[pnum[1][i][j]] = true;
                }
                else if (G0[i][j] == '+') {
                    ++ ans;
                    link(pnum[0][i][j], pnum[1][i][j]);
                    linker[snum[1][i][j]] = snum[0][i][j];
                    banu[snum[0][i][j]] = banv[snum[1][i][j]] = true;
                }
                else {
                    ans += 2;
                    linker[pnum[1][i][j]] = pnum[0][i][j];
                    banu[pnum[0][i][j]] = banv[pnum[1][i][j]] = true;
                    linker[snum[1][i][j]] = snum[0][i][j];
                    banu[snum[0][i][j]] = banv[snum[1][i][j]] = true;
                }
            }
        }

        std::cout << "Case #" << t << ": ";
        ans += hungary();
        for (int i = 0; i < n; ++ i)
            if (~linker[i]) {
                nG[linker[i] + 1][i + 1] ^= 1;
            }
        for (int j = 0; j < 2 * n - 1; ++ j) {
            if (~linker[n + j]) {
                int i = linker[n + j] - n;
                int x = (j - i + n + 1) / 2;
                int y = (i + j - n + 3) / 2;
                nG[x][y] ^= 2;
            }
        }

        std::vector<std::tuple<char, int, int>> ans_list;
        for (int i = 1; i <= n; ++ i) {
            for (int j = 1; j <= n; ++ j) {
                //putchar(G0[i][j]);
                G[i][j] = ".x+o"[nG[i][j]];
                if (G[i][j] != G0[i][j])
                    ans_list.emplace_back(G[i][j], i, j);
            }
            //putchar('\n');
        }

        std::cout << ans << " " << ans_list.size() << std::endl;
        for (auto x : ans_list)
            std::cout << std::get<0>(x) << " " << std::get<1>(x) << " " << std::get<2>(x) << std::endl;
    }
}

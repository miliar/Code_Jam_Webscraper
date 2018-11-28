#include <bits/stdc++.h>
using namespace std;
template <class T> int size(const T &x) { return x.size(); }
#define rep(i,a,b) for (__typeof(a) i=(a); i<(b); ++i)
#define iter(it,c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
const int INF = 2147483647;

char arr[110][110];
vii sol, tur;
int can[110][1<<10];
int mem[1<<10][1<<10];
ii lnk[1<<10][1<<10];

int dp(int ts, int ss) {
    if (mem[ts][ss] != -1)
        return mem[ts][ss];
    lnk[ts][ss] = ii(-1,-1);
    int mx = 0;
    rep(i,0,size(sol)) {
        if (ss & (1<<i)) {
            rep(j,0,size(tur)) {
                if (can[i][ts] & (1<<j)) {
// cout << ts << " " << ss << ", " << i << " can " << j << endl;
// cout << ss << " " << can[i][ss] << endl;
                    int here = 1 + dp(ts ^ (1<<j), ss ^ (1 << i));
                    if (here > mx) {
                        lnk[ts][ss] = ii(i,j);
                        mx = here;
                    }
                }
            }
        }
    }
    return mem[ts][ss] = mx;
}

int main() {
    int ts;
    cin >> ts;
    rep(t,0,ts) {
        memset(mem,-1,sizeof(mem));
        int r, c, m;
        cin >> c >> r >> m;
        sol.clear();
        tur.clear();
        rep(i,0,r) {
            rep(j,0,c) {
                cin >> arr[i][j];
                if (arr[i][j] == 'S') {
                    sol.push_back(ii(i,j));
                }
                if (arr[i][j] == 'T') {
                    tur.push_back(ii(i,j));
                }
            }
        }
        // rep(i,0,r) {
        //     rep(j,0,c) {
        //         cout << arr[i][j];
        //     }
        //     cout << endl;
        // }

        memset(can,0,sizeof(can));
        rep(sub,0,1<<size(tur)) {
            int reach[31][31];
            rep(i,0,r) {
                rep(j,0,c) {
                    reach[i][j] = 0;
                }
            }
            rep(i,0,size(tur)) {
                if (sub & (1<<i)) {
                    rep(dx,-1,2) {
                        rep(dy,-1,2) {
                            if (abs(dx) + abs(dy) != 1) {
                                continue;
                            }
                            int x = tur[i].first,
                                y = tur[i].second;
                            while (0 <= x && x < r && 0 <= y && y < c && arr[x][y] != '#') {
                                reach[x][y] |= (1<<i);
                                x += dx;
                                y += dy;
                            }
                        }
                    }
                }
            }
            rep(i,0,size(sol)) {
                queue<ii> Q;
                int dist[31][31];
                memset(dist,-1,sizeof(dist));
                Q.push(sol[i]);
                dist[sol[i].first][sol[i].second] = 0;
                while (!Q.empty()) {
                    ii cur = Q.front();
                    Q.pop();
                    // cout << cur.first << " " << cur.second << endl;
                    if (reach[cur.first][cur.second] != 0) {
                        can[i][sub] |= reach[cur.first][cur.second];
                        continue;
                    }
                    if (dist[cur.first][cur.second] < m) {
                        rep(dx,-1,2) {
                            rep(dy,-1,2) {
                                if (abs(dx) + abs(dy) != 1)
                                    continue;
                                int nx = cur.first + dx,
                                    ny = cur.second + dy;
                                if (0 <= nx && nx < r && 0 <= ny && ny < c && arr[nx][ny] != '#' && dist[nx][ny] == -1) {
                                    Q.push(ii(nx,ny));
                                    // cout << nx << " " << ny << endl;
                                    dist[nx][ny] = 1 + dist[cur.first][cur.second];
                                }
                            }
                        }
                    }
                }

// cout << sub << " " << i << ": " << can[i][sub] << endl;
            }
        }
        // rep(sub,0,1<<size(tur)) {
        //     rep(i,0,size(sol)) {
        //         cout << sub << " " << i << " " << can[sub][i]
        //     }
        // }

        cout << "Case #" << (t+1) << ": " << dp((1<<size(tur))-1, (1<<size(sol))-1) << endl;
        int a = (1<<size(tur))-1,
            b = (1<<size(sol))-1;
        while (lnk[a][b].first != -1) {
            int x = lnk[a][b].first,
                y = lnk[a][b].second;
            cout << x+1 << " " << y+1 << endl;
            a ^= (1<<y);
            b ^= (1<<x);
        }
    }
    return 0;
}


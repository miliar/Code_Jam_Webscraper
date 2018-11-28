#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

const int dx[] = {1, 0, -1, 0};
const int dy[] = {0, 1, 0, -1};

int n, m, moves, can[1 << 11][12][35][35], fire[35][35];
int ids[36][36], idt[36][36], dp[1 << 11][1 << 11];
pair<int, int> p[1 << 11][1 << 11];
vector<pair<int, int>> kills[12];
vector<pair<int, int>> turrs, solds;
vector<pair<int, int>> revs;
string s[35];

void load() {
    cin >> n >> m >> moves;
    swap(n, m);
    for (int i = 0;i < n;i++) {
        cin >> s[i];
    }
}

void traverse(int x, int y, int sold, int mask) {
    vector<pair<int, int>> q;
    can[mask][sold][x][y] = 0;
    q.push_back(make_pair(x, y));
    int h = 0;

  //  cerr << mask << " " << sold << " " << x << " " << y << endl;
    while(h < (int)q.size()) {
        int x = q[h].first;
        int y = q[h].second;
        h++;

        int left = fire[x][y] ^ (mask & fire[x][y]);
//if (mask == 4) cerr << sold << " " << x << " " << y << " " << left << can[mask][sold][x][y] << "\n"; 
        if (left != 0) continue;

        for (int k = 0;k < 4;k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;

            if (s[nx][ny] == '#') continue;
            int cd = can[mask][sold][x][y];
            if (can[mask][sold][nx][ny] == -1 && cd + 1 <= moves) {
                can[mask][sold][nx][ny] = cd + 1;
                q.push_back(make_pair(nx, ny));
            }
        }
    }
}

int go(int msol, int mtur) {
    int &res = dp[msol][mtur];
    if (res != -1) return res;
    res = 0;

    for (int i = 0;i < (int)solds.size();i++) {
        if ((1 << i) & (msol)) continue;
        for (int j = 0;j < (int)turrs.size();j++) {
            if ((1 << j) & mtur) continue;

            for (int k = 0;k < (int)kills[j].size();k++) {
                if (can[mtur][i][kills[j][k].first][kills[j][k].second] == -1) continue;

                int t = go(msol | (1 << i), mtur | (1 << j)) + 1;
                if (t > res) {
                    res = t;
                    p[msol][mtur] = make_pair(i, j);
                }
                break;
            }
        }
    }
    return res;
}

void rev(int msol, int mtur) {
    if (dp[msol][mtur] == 0) return;
    revs.push_back(p[msol][mtur]);
    rev(msol | (1 << p[msol][mtur].first), mtur | (1 << p[msol][mtur].second));
}

void solve(int test) {
    printf("Case #%d: ", test);

    turrs.clear();
    solds.clear();
    for (int i = 0;i < n;i++) {
        for (int j = 0;j < m;j++) {
            if (s[i][j] == 'S') {
                solds.push_back(make_pair(i, j));
                ids[i][j] = solds.size();
            }
            if (s[i][j] == 'T') {
                turrs.push_back(make_pair(i, j));
                idt[i][j] = turrs.size();
            }
        }
    }

    memset(fire, 0, sizeof(fire));
    for (int i = 0;i < (int)turrs.size();i++) {
        kills[i].clear();
    }
    for (int i = 0;i < (int)turrs.size();i++) {
        int x = turrs[i].first;
        int y = turrs[i].second;
        for (int k = 0;k < 4;k++) {
            for (int steps = 0;;steps++) {
                int nx = x + dx[k] * steps;
                int ny = y + dy[k] * steps;
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) break;
                if (s[nx][ny] == '#') break;
                fire[nx][ny] |= (1 << i);
                kills[i].push_back(make_pair(nx, ny));
            }
        }
    }

    /*cerr << turrs.size() << "\n";
    for (int i = 0;i < (int)turrs.size();i++) {
        cerr << turrs[i].first << " " << turrs[i].second << endl;
    }

    for (int i = 0;i < n;i++) {
        for (int j = 0;j < m;j++) {
            cerr << fire[i][j] << " ";
        }
        cerr << endl;
    }*/

    memset(dp, -1, sizeof(dp));
    memset(can, -1, sizeof(can));
    for (int i = 0;i < (1 << (int)turrs.size());i++) {
        for (int j = 0;j < (int)solds.size();j++) {
            traverse(solds[j].first, solds[j].second, j, i);
        }
    }

    //cerr << can[4][0][1][0] << " " << can[4][1][1][0] << " " << can[4][2][1][0] << "\n";

    int ans = go(0, 0);
    revs.clear();
    rev(0, 0);
    printf("%d\n", ans);
    for (int i = 0;i < ans;i++) {
        printf("%d %d\n", revs[i].first + 1, revs[i].second + 1);
    }
}

int main() {
#ifdef VALERA
    freopen("a.in", "r", stdin);
#endif
    int t;
    cin >> t;

    for (int i = 0;i < t;i++) {
        load();
        solve(i + 1);
    }
    return 0;
}

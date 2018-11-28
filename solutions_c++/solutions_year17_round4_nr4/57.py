#include <bits/stdc++.h>
using namespace std;
#define fo(i,a,b) for (int i = (a); i < (b); i++)
#define pb push_back
typedef long long ll;
typedef pair<int,int> pii;
#define y first
#define x second

int T;

int dx[] = {0,1,0,-1};
int dy[] = {1,0,-1,0};

int c, r, mv;
int t, s;
pii tp[11], sp[11];

char gr[123][123];
int trgs[1<<10][11][11];

int sn[111][111], sut = 1;

int blk[123][123];

bool dp[1<<10][1<<10];
int ts[1<<10][1<<10], tt[1<<10][1<<10];
set<pii> los[11];

void reset() {
    fo(i,0,1<<t) fo(j,0,s) fo(k,0,t) trgs[i][j][k] = 0;
    fo(i,0,1<<s) fo(j,0,1<<t) dp[i][j] = 0;
    fo(i,0,t) los[i].clear();
    t = s = 0;
}

bool gp(int y, int x) {
    if (y < 0 || x < 0 || y >= r || x >= c) return 0;
    if (gr[y][x] == '#') return 0;
    return 1;
}

int main() {
    scanf("%d", &T);
    fo(_,1,T+1) {
        printf("Case #%d: ", _);

        scanf("%d %d %d", &c, &r, &mv);

        fo(i,0,r) scanf("%s", gr[i]);
        fo(i,0,r) fo(j,0,c) {
            if (gr[i][j] == 'T') {
                tp[t++] = {i,j};
            }
            if (gr[i][j] == 'S') {
                sp[s++] = {i,j};
            }
        }

        fo(i,0,t) fo(d,0,4) {
            int y = tp[i].y, x = tp[i].x;
        //    printf("%d %d\n", y, x);
            while (gp(y,x)) {
                los[i].insert({y,x});
          //      printf("los %d %d %d\n", i, y, x);
                y += dy[d]; x += dx[d];
            }

        }

        fo(i,0,1<<t) {
            fo(j,0,t) if(!(i & (1<<j))) for (auto x : los[j]) blk[x.y][x.x] = 1;

            fo(j,0,s) {
                typedef tuple<int,int,int> state;
                queue<state> q;
                q.push(state(sp[j].y, sp[j].x, 0));
                sn[sp[j].y][sp[j].x] = sut;   
                while (!q.empty()) {
                    int y, x, dst;
                    tie(y,x,dst) = q.front(); q.pop();
                    if (dst > mv) break;

         //           printf("%d %d at %d %d\n", i, j, y, x);

                    fo(k,0,t) if (los[k].count({y,x})) {
           //             printf("in los %d\n", k);
                        trgs[i][j][k] = 1;
                    }

                    if (blk[y][x]) continue;
                    fo(d,0,4) {
                        int ny = y + dy[d], nx = x + dx[d];
                        if (!gp(ny,nx) || sn[ny][nx] == sut) continue;
                        sn[ny][nx] = sut;
                        q.push(state(ny,nx,dst+1));
                    }
                }
                sut++;   
            }

            fo(j,0,r) fo(k,0,c) blk[j][k] = 0;
        }

        int bi = 0, bj = 0;
        dp[0][0] = 1;
        fo(i,0,1<<s) fo(j,0,1<<t) if (dp[i][j]) {
         //   printf("dp %d %d\n", i, j);
            if (__builtin_popcount(j) > __builtin_popcount(bj)) {
                bi = i; bj = j;
            }
            fo(as,0,s) if (!(i & (1<<as))) fo(at,0,t) if (!(j & (1<<at))) {
                if (trgs[j][as][at]) {
                    int ai = i | (1<<as), aj = j | (1<<at);
                    dp[ai][aj] = true;
                    ts[ai][aj] = as;
                    tt[ai][aj] = at;
                }
            }
        }
        vector<pii> ans;
        while (bi) {
            ans.pb({ts[bi][bj], tt[bi][bj]});
            int nxti = bi ^ (1<<ts[bi][bj]), nxtj = bj ^ (1<<tt[bi][bj]);
            bi = nxti; bj = nxtj;
        }
        reverse(ans.begin(), ans.end());
        printf("%d\n", ans.size());
        for (auto x : ans) printf("%d %d\n", x.first+1, x.second+1);

        reset();
    }

    return 0;
}

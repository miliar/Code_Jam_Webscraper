
/*********************************************************************\
   |--\        ---       /\        |-----------| -----   /-------|    |
   |   \        |       /  \       |               |    /             |
   |    \       |      /    \      |               |   |              |
   |     \      |     /      \     |               |   |----|         |
   |      \     |    / ------ \    |-------|       |        |-----|   |
   |       \    |   /          \   |               |              |   |
   |        \   |  /            \  |               |              /   |
  ---        -------            ------           ----- |---------/    |
                                                                      |
    codeforces = nfssdq  ||  topcoder = nafis007                      |
    mail = nafis_sadique@yahoo.com || nfssdq@gmail.com                |
    IIT,Jahangirnagar University(41)                                  |
                                                                      |
**********************************************************************/

#include <bits/stdc++.h>
using namespace std;

#define xx         first
#define yy         second
#define pb         push_back
#define mp         make_pair
#define LL         long long
#define inf        INT_MAX/3
#define mod        1000000007ll
#define PI         acos(-1.0)
#define linf       (1ll<<60)-1
#define FOR(I,A,B) for(int I = (A); I < (B); ++I)
#define REP(I,N)   FOR(I,0,N)
#define ALL(A)     ((A).begin(), (A).end())
#define set0(ar)   memset(ar,0,sizeof ar)
#define vsort(v)   sort(v.begin(),v.end())
#define setinf(ar) memset(ar,126,sizeof ar)

//cout << fixed << setprecision(20) << p << endl;

template <class T> inline T bigmod(T p,T e,T M){
    LL ret = 1;
    for(; e > 0; e >>= 1){
        if(e & 1) ret = (ret * p) % M;
        p = (p * p) % M;
    }
    return (T)ret;
}
template <class T> inline T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}

int nxt[4][2] = { {0, -1}, {-1, 0}, {0, 1}, {1, 0} };
char pp[55][55];
set < int > S;
int id[55][55];
int vis[55][55][4];

int R, C, fl;
void dfs(int x, int y, int d){
    if(x < 0 || x >= R || y < 0 || y >= C) return;
    if(vis[x][y][d]) return;
    if(pp[x][y] == '#') return;
    if(pp[x][y] == '-' || pp[x][y] == '|'){
        fl = 1;
        return;
    }
    vis[x][y][d] = 1;
    if(pp[x][y] == '.') S.insert(id[x][y]);
    if(pp[x][y] == '/'){
        if(d == 0) d = 3;
        else if(d == 1) d = 2;
        else if(d == 2) d = 1;
        else d = 0;
    } else if(pp[x][y] != '.'){
        if(d == 0) d = 1;
        else if(d == 1) d = 0;
        else if(d == 2) d = 3;
        else d = 2;
    }

    dfs(x + nxt[d][0], y + nxt[d][1], d);
}

set < int > SS[111][2];
int flags[111][2];
vector < int > V[2555];
int empties[2501], tmp[2555];

int state[111];
int dfs2(int n){
    int cur[2501];
    for(int i = 1; i <= n; i++){
        cur[i] = empties[i];
    }

    int mn = 100000, idd = -1;
    for(int i = 1; i <= n; i++){
        if(empties[i] == -1) continue;
        if(empties[i] < mn){
            mn = empties[i];
            idd = i;
        }
    }
    if(mn > 10000) {
        return 1;
    }

    REP(i, V[idd].size()){
        if(state[abs(V[idd][i])] != 0) continue;
        REP(j, n+1) empties[j] = cur[j];
        int dir = 0;
        if(V[idd][i] > 0) dir = 1;
        else dir = 2;
        state[abs(V[idd][i])] = dir;
        for(auto &v: SS[abs(V[idd][i])][dir-1]){
            empties[v] = -1;
        }
        if(dfs2(n)) return 1;
        state[abs(V[idd][i])] = 0;
        REP(j, n+1) empties[j] = cur[j];
    }
    return 0;
}

int main(){
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
    int T; cin >> T;
    FOR(ts, 1, T+1){
        cin >> R >> C;
        REP(i, R) cin >> pp[i];
        REP(i, 101){
            REP(j, 2){
                flags[i][j] = 0;
                SS[i][j].clear();
            }
        }

        int cnt_empty = 0, cnt_shot = 0;
        REP(i, R){
            REP(j, C){
                if(pp[i][j] == '.') {
                    cnt_empty++;
                    id[i][j] = cnt_empty;
                    V[cnt_empty].clear();
                } else if(pp[i][j] == '-' || pp[i][j] == '|'){
                    cnt_shot++;
                    id[i][j] = cnt_shot;
                }
            }
        }
        REP(i, R) REP(j, C){
            if(pp[i][j] == '-' || pp[i][j] == '|'){
                REP(k, 4){
                    fl = 0;
                    S.clear();
                    set0(vis);
                    dfs(i + nxt[k][0], j + nxt[k][1], k);
                    for(auto &v : S){
                        SS[id[i][j]][k%2].insert(v);
                    }
                    flags[id[i][j]][k%2] |= fl;
                }
            }
        }

        int fail = 0;
        cout << "Case #" << ts << ": ";
        set0(empties);
        set0(state);
        for(int i = 1; i <= cnt_shot; i++){
            if(flags[i][0] && flags[i][1]){
                fail = 1;
            }
            if(flags[i][0]) state[i] = 2;
            else if(flags[i][1]) state[i] = 1;
            set0(tmp);
            if(flags[i][0] == 0)for(auto &v: SS[i][0])tmp[v] |= 1;
            if(flags[i][1] == 0)for(auto &v: SS[i][1])tmp[v] |= 2;

            for(int j = 1; j <= cnt_empty; j++){
                if(empties[j] == -1) continue;
                if(tmp[j] == 3 || (flags[i][0] + flags[i][1] == 1 && tmp[j])){
                    empties[j] = -1;
                } else if(tmp[j]){
                    empties[j]++;
                    if(tmp[j] == 1)V[j].pb(i);
                    else V[j].pb(-i);
                }
            }
        }

        if(fail){
            cout << "IMPOSSIBLE" << endl;
            continue;
        }

        fl = dfs2(cnt_empty);
        if(fl == 0){
            cout << "IMPOSSIBLE" << endl;
            continue;
        }

        cout << "POSSIBLE" << endl;
        REP(i, R){
            REP(j, C){
                if(pp[i][j] == '-' || pp[i][j] == '|'){
                    if(state[id[i][j]] == 1) pp[i][j] = '-';
                    else if(state[id[i][j]] == 2) pp[i][j] = '|';
                }
            }
            cout << pp[i] << endl;
        }

    }
}


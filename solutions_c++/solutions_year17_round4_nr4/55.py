// Enjoy your stay. Code by evima on 2017/05/13

#include <bits/stdc++.h>
#include <dirent.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

#define LOOPVAR_TYPE long

#define all(x) (x).begin(), (x).end()
#define sz(x) ((LOOPVAR_TYPE)(x).size())
#define foreach(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); it++)
#define GET_MACRO(_1, _2, _3, NAME, ...) NAME
#define _rep(i, n) _rep2(i, 0, n)
#define _rep2(i, a, b) for(LOOPVAR_TYPE i = (LOOPVAR_TYPE)(a); i < (LOOPVAR_TYPE)(b); i++)
#define rep(...) GET_MACRO(__VA_ARGS__, _rep2, _rep)(__VA_ARGS__)

template<class T>
bool tomin(T &a, const T &b) { return (b < a) ? (a = b, true) : false; }

template<class T>
bool tomax(T &a, const T &b) { return (a < b) ? (a = b, true) : false; }

#define fir first
#define sec second
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back

const double EPS = 1e-9;
const double PI = 3.141592653589793238462;
const long INF = 1070000000LL;
const long MOD = 1000000007LL;

using namespace std;

////////////////////////////////////////////////////////////
int C, R, M;
char a[111][111];
int SY[111], SX[111];
int TY[111], TX[111];
int dp[1<<10][1<<10];
int nxS[1<<10][1<<10];
int nxT[1<<10][1<<10];
int numS, numT;
int canShoot[1<<10][10][10];

int dy[] = {0, 1, 0, -1};
int dx[] = {1, 0, -1, 0};

void read_input(istream &ist) {
    ist >> C >> R >> M;
    rep(i, R) ist >> a[i];
}

void prep(int mask2){
    int isSeen[111][111];
    memset(isSeen, 0, sizeof(isSeen));
    rep(i, numT){
        if(mask2 >> i & 1){
            rep(dir, 4){
                int y = TY[i];
                int x = TX[i];
                while(1) {
                    isSeen[y][x] = 1;
                    y += dy[dir];
                    x += dx[dir];
                    if(y < 0 || y >= R || x < 0 || x >= C) break;
                    if(a[y][x] == '#') break;
                }
            }
        }
    }
    if(mask2 == (1<<numT)-1){
        rep(i, R){
            //rep(j, C) cerr << isSeen[i][j];
            //cerr<<endl;
        }
    }
    rep(id_s, numS){
        int dist[111][111];
        rep(i, R) rep(j, C) dist[i][j] = INF;
        dist[SY[id_s]][SX[id_s]] = 0;
        queue<pair<int, int>> Q;
        Q.push(mp(SY[id_s], SX[id_s]));
        while(sz(Q)){
            auto t = Q.front(); Q.pop();
            int y = t.fir, x = t.sec;
            if(mask2 == (1<<numT)-1 && id_s == 0){
                cerr<<y<<" "<<x<<endl;
            }

            rep(dir, 4){
                int yy = y, xx = x;
                while(1){
                    rep(id_t, numT){
                        if(yy == TY[id_t] && xx == TX[id_t]){
                            canShoot[mask2][id_s][id_t] = 1;
                        }
                    }
                    yy += dy[dir];
                    xx += dx[dir];
                    if(yy < 0 || yy >= R || xx < 0 || xx >= C) break;
                    if(a[yy][xx] == '#') break;
                }
            }

            int d = dist[y][x];
            if(isSeen[y][x]) continue;
            if(d == M) continue;
            rep(dir, 4){
                int ny = y + dy[dir];
                int nx = x + dx[dir];
                int nd = d + 1;
                if(0 <= ny && ny < R && 0 <= nx && nx < C && dist[ny][nx] == INF && a[ny][nx] != '#'){
                    dist[ny][nx] = nd;
                    Q.push(mp(ny, nx));
                }
            }
        }
    }
}

int f(int mask1, int mask2){
    int& ret = dp[mask1][mask2];
    if(ret != -1) return ret;
    ret = 0;
    rep(i, numS){
        if(mask1 >> i & 1){
            rep(j, numT){
                if(mask2 >> j & 1){
                    if(canShoot[mask2][i][j]){
                        int ret2 = 1 + f(mask1 ^ (1<<i), mask2 ^ (1<<j));
                        if(ret2 > ret){
                            ret = ret2;
                            nxS[mask1][mask2] = i;
                            nxT[mask1][mask2] = j;
                        }
                    }
                }
            }
        }
    }
    return ret;
}

void solve(ostream &ost) {
    numS = 0, numT = 0;
    rep(i, R){
        rep(j, C){
            if(a[i][j] == 'S'){
                SY[numS] = i;
                SX[numS] = j;
                numS++;
            }
            if(a[i][j] == 'T'){
                TY[numT] = i;
                TX[numT] = j;
                numT++;
            }
        }
    }
    memset(canShoot, 0, sizeof(canShoot));
    rep(mask2, (1<<numT)){
        prep(mask2);
    }
    rep(i, numS) rep(j, numT) cerr << i << " " << j << " " << canShoot[(1<<numT)-1][i][j] << endl;
    memset(dp, -1, sizeof(dp));
    memset(nxS, -1, sizeof(nxS));
    memset(nxT, -1, sizeof(nxT));
    int ans = f((1<<numS)-1, (1<<numT)-1);
    ost << ans << endl;
    int curMask1 = (1<<numS)-1;
    int curMask2 = (1<<numT)-1;
    while(1){
        if(nxS[curMask1][curMask2] == -1) break;
        int s = nxS[curMask1][curMask2];
        int t = nxT[curMask1][curMask2];
        ost << s+1 << " " << t+1 << endl;
        curMask1 ^= 1<<s;
        curMask2 ^= 1<<t;
    }
}

////////////////////////////////////////////////////////////

const int MAX_PROCESS = 8;
const char FRAGMENTS_DIR[] = "fragments";

string int2str(int input, int upper) {
    int len = max(3, (int) ceil(log10(upper)));
    string ret((size_t) len, '\0');
    rep(i, len) {
        ret[len - 1 - i] = (char) ('0' + input % 10);
        input /= 10;
    }
    return ret;
}

int main(int argc, char *argv[]) {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    istream *isp;
    ostream *osp;

    string inf;
    string ouf = "stdout";

    if (argc >= 2) {
        char *inf_c = argv[1];
        inf = inf_c;
        isp = new ifstream(inf);
        if (!*isp) {
            cerr << "Error: cannot read " << inf << endl;
            perror("");
            exit(1);
        }
    } else {
        isp = &cin;
    }

    if (argc >= 3) {
        char *ouf_c = argv[2];
        ouf = ouf_c;
        osp = new ofstream(ouf);
        if (!*osp) {
            cerr << "Error: cannot write to " << ouf << endl;
            perror("");
            exit(2);
        }

        DIR *dir_f = opendir(FRAGMENTS_DIR);
        if (dir_f) {
            closedir(dir_f);
        } else if (errno == ENOENT) {
            mkdir(FRAGMENTS_DIR, 0755);
        } else {
            cerr << "Error: " << FRAGMENTS_DIR << " is not a directory" << endl;
            exit(3);
        }
    } else {
        osp = &cout;
    }

    int T;
    *isp >> T;

    if (inf.find('-') == string::npos) {
        cerr << "not an official input, no multiprocessing" << endl;

        rep(cid, 1, T + 1) {
            read_input(*isp);
            *osp << "Case #" << cid << ": ";
            solve(*osp);
        }
    } else {
        cerr << "official input, multiprocessing" << endl;

        int num_process = 0;
        vector<pid_t> pids((size_t) T);
        map<pid_t, int> pid2cid;

        int status;
        pid_t pid;

        for (int cid = 1; cid <= T; cid++) {
            read_input(*isp);

            if (num_process == MAX_PROCESS) {
                pid = wait(&status);
                if (status != 0) {
                    cerr << "Error: PID " << pid << " exited with status "
                         << status << " in Case #" << pid2cid[pid] << endl;
                }
                num_process--;
            }

            if ((pids[cid] = fork()) < 0) {
                perror("fork");
                exit(-1);
            } else if (pids[cid] == 0) {
                ofstream ofs(string(FRAGMENTS_DIR) + "/" + ouf + "." + int2str(cid, T));
                ofs << "Case #" << cid << ": ";
                solve(ofs);
                exit(0);
            } else {
                pid2cid[pids[cid]] = cid;
                num_process++;
            }
        }

        while (num_process > 0) {
            pid = wait(&status);
            if (status != 0) {
                cerr << "Error: PID " << pid << " exited with status "
                     << status << " in Case #" << pid2cid[pid] << endl;
            }
            num_process--;
        }
    }

    for (int cid = 1; cid <= T; cid++) {
        ifstream ifs(string(FRAGMENTS_DIR) + "/" + ouf + "." + int2str(cid, T));
        string str;
        while (getline(ifs, str)) {
            *osp << str << endl;
        }
    }
}
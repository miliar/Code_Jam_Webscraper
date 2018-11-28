// Enjoy your stay. Code by evima on 2017/04/23

#include <bits/stdc++.h>
#include <unistd.h>
#include <sys/wait.h>

#define LOOPVAR_TYPE long

#define all(x) (x).begin(), (x).end()
#define sz(x) ((LOOPVAR_TYPE)(x).size())
#define foreach(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); it++)
#define GET_MACRO(_1, _2, _3, NAME, ...) NAME
#define _rep(i, n) _rep2(i, 0, n)
#define _rep2(i, a, b) for(LOOPVAR_TYPE i = (LOOPVAR_TYPE)(a); i < (LOOPVAR_TYPE)(b); i++)
#define rep(...) GET_MACRO(__VA_ARGS__, _rep2, _rep)(__VA_ARGS__)

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

int N, R, O, Y, G, B, V;

void read_input() {
    cin >> N >> R >> O >> Y >> G >> B >> V;
}

void solve(ofstream& ofs) {

    int r = R, y = Y, b = B;
    if(G > 0){
        if(r == G && r + G == N){
            rep(i, r) ofs << "RG";
            ofs << endl;
            return;
        }
        if(r <= G){
            ofs << "IMPOSSIBLE" << endl;
            return;
        }
        r -= G;
    }
    if(V > 0){
        if(y == V && y + V == N){
            rep(i, y) ofs << "YV";
            ofs << endl;
            return;
        }
        if(y <= V){
            ofs << "IMPOSSIBLE" << endl;
            return;
        }
        y -= V;
    }
    if(O > 0){
        if(b == O && b + O == N){
            rep(i, b) ofs << "BO";
            ofs << endl;
            return;
        }
        if(b <= O){
            ofs << "IMPOSSIBLE" << endl;
            return;
        }
        b -= O;
    }

    int n = r + y + b;
    char mc = 'R';
    int mx = r;

    if(y > mx){
        mx = y;
        mc = 'Y';
    }
    if(b > mx){
        mx = b;
        mc = 'B';
    }

    if(mx > n / 2){
        ofs << "IMPOSSIBLE" << endl;
        return;
    }

    string remaining;
    while(r + y + b - mx > 0) {
        if (mc != 'R' && r > 0) {
            remaining += 'R';
            r--;
        }
        if (mc != 'Y' && y > 0) {
            remaining += 'Y';
            y--;
        }
        if (mc != 'B' && b > 0) {
            remaining += 'B';
            b--;
        }
    }

    string res(n, '?');
    rep(i, mx){
        res[2*i] = mc;
    }
    int pos = 0;
    for(int i = n-1; i >= 0; i--){
        if(res[i] == '?'){
            res[i] = remaining[pos++];
        }
    }
    cerr<<res<<" "<<mx<<endl;

    string ans;
    int flagG = G > 0, flagV = V > 0, flagO = O > 0;
    rep(i, n){
        if(res[i] == 'R' && flagG){
            rep(i, G){
                ans += "RG";
            }
            ans += "R";
            flagG = 0;
        }else if(res[i] == 'G' && flagV){
            rep(i, V){
                ans += "GV";
            }
            ans += "G";
            flagV = 0;
        }else if(res[i] == 'B' && flagO){
            rep(i, O){
                ans += "BO";
            }
            ans += "B";
            flagO = 0;
        }else{
            ans += res[i];
        }
    }
    ofs << ans << endl;
}

int main(int argc, char *argv[]) {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    if(argc != 2){
        cerr << "Error: argc is not 2" << endl;
        exit(1);
    }

    char *ouf_c = argv[1];
    string ouf = ouf_c;
    if(access(ouf_c, F_OK) != -1){
        cerr << "Error: " + ouf + " already exists" << endl;
        exit(2);
    }

    int numP = 0;
    const int maxP = 4;
    pid_t pids[1000];
    map<pid_t, int> pid2cid;

    int status;
    pid_t pid;

    int T;
    cin >> T;
    rep(cid, 1, T + 1) {
        read_input();

        if (numP == maxP){
            pid = wait(&status);
            if(status != 0){
                cerr << "Error: PID " << pid << " exited with status "
                     << status << " in Case #" << pid2cid[pid] << endl;
            }
            numP--;
        }

        if ((pids[cid] = fork()) < 0) {
            perror("fork");
            exit(-1);
        } else if (pids[cid] == 0) {
            ofstream ofs("work/" + ouf + "." + to_string(cid));
            ofs << "Case #" << cid << ": ";
            solve(ofs);
            exit(0);
        } else {
            pid2cid[pids[cid]] = cid;
            numP++;
        }

    }

    while (numP > 0) {
        pid = wait(&status);
        if(status != 0){
            cerr << "Error: PID " << pid << " exited with status "
                 << status << " in Case #" << pid2cid[pid] << endl;
        }
        numP--;
    }

    ofstream ofs(ouf);
    rep(cid, 1, T + 1) {
        ifstream ifs("work/" + ouf + "." + to_string(cid));
        string str;
        while(getline(ifs, str)){
            ofs << str << endl;
        }
    }
}
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

int N, Q;
int E[111];
double S[111];
long D[111][111];
int U[111], V[111];
double edges[111][111];

void read_input() {
    cin >> N >> Q;
    rep(i, N) cin >> E[i] >> S[i];
    rep(i, N){
        rep(j, N){
            cin >> D[i][j];
            if(D[i][j] == -1) D[i][j] = 1e15;
        }
    }
    rep(i, Q){
        cin >> U[i] >> V[i];
        U[i]--; V[i]--;
    }
}

void solve(ofstream& ofs) {
    rep(k, N){
        rep(i, N){
            rep(j, N){
                D[i][j] = min(D[i][j], D[i][k] + D[k][j]);
            }
        }
    }
    rep(i, N){
        rep(j, N){
            if(D[i][j] <= E[i]){
                edges[i][j] = D[i][j] / S[i];
            }else{
                edges[i][j] = 1e15;
            }
        }
    }
    rep(k, N){
        rep(i, N){
            rep(j, N){
                edges[i][j] = min(edges[i][j], edges[i][k] + edges[k][j]);
            }
        }
    }
    rep(i, Q){
        ofs << setprecision(17) << edges[U[i]][V[i]] << " ";
    }
    ofs << endl;
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
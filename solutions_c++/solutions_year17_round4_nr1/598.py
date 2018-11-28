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
int N, G[111], P;
int total;

void read_input(istream &ist) {
    ist >> N >> P;
    rep(i, N) ist >> G[i];
}

map<vector<char>, int> M;
int f(vector<char> v){
    if(M.find(v) != M.end()){
        return M[v];
    }
    int& res = M[v];
    int t = 0;
    int sum = 0;
    rep(i, P){
        t += v[i] * i;
        sum += v[i];
    }
    if(sum == 0){
        return res = 0;
    }
    rep(i, P){
        if(v[i] > 0){
            v[i]--;
            tomax(res, f(v));
            v[i]++;
        }
    }
    return res += (total - t) % P == 0;
}

void solve(ostream &ost) {
    vector<char> v(P, 0);
    total = 0;
    rep(i, N){
        v[G[i] % P]++;
        total += G[i];
    }
    M.clear();
    ost << f(v) << endl;
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
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef vector<double> ret_t;

struct Pos {
public:
    Pos(int _v, int _dist):v(_v), dist(_dist) {
    }
    int v;
    int dist;
};

class compare { // for queue
public:
    bool operator()(const Pos & a, const Pos & b) const {
        return a.dist > b.dist; // here > means lower costs go first
    }
};

class Solver {
public:
    vector<vector<double> > traveltime;
    //vector<bool> vis;
    ret_t solve(int n, int q, vector<int> maxdist, vector<double> speed,
                vector<vector<int> > dist, vector<int> from, vector<int> to) {
        //cerr<<"In solver"<<endl;
        ret_t ret(q, -1);
        traveltime = vector<vector<double> >(n, vector<double>(n, -1));
        for (int i = 0; i < n; ++i) {
            vector<int> traveldist(n, -1);
            priority_queue<Pos, vector<Pos>, compare> q;
            //traveldist[i] = 0;
            Pos p(i, 0);
            q.push(p);
            while (!q.empty()) {
                p = q.top();
                q.pop();
                int j = p.v;
                int d = p.dist;
                if (traveldist[j] != -1)
                    continue;
                traveldist[j] = d;
                for (int k = 0; k < n; ++k) {
                    if (dist[j][k] == -1)
                        continue;
                    int d2 = d + dist[j][k];
                    if (d2 > maxdist[i])
                        continue;
                    q.push(Pos(k, d2));
                }
            }
            for (int k = 0; k < n; ++k) {
                if (traveldist[k] == -1)
                    traveltime[i][k] = 1e12;
                else
                    traveltime[i][k] = traveldist[k] / speed[i];
            //traveltime[i][i] = 0.0;
            }
        }
        //cerr<<"starting all-pair"<<endl;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                for (int k = 0; k < n; ++k) {
                    traveltime[j][k] = min(traveltime[j][k],
                                           traveltime[j][i] + traveltime[i][k]);
                }
            }
        }
        for (int i = 0; i < q; ++i) {
            //cerr<<i<<endl;
            //cerr<<from[i]-1<<'\t'<<to[i]-1<<endl;
            ret[i] = traveltime[from[i]-1][to[i]-1];
        }
        return ret;
    }
};

int main(int argc, char ** argv) {
    string s;
    int N;
    getline(cin, s);
    {
        stringstream A(s);
        A >> N;
    }
    for (int no = 1; no <= N; ++no) {
        cerr //<< "Case "
            << no << " / " << N << endl;
        Solver solver;
        // *** get input ***
        getline(cin, s);
        int n, q;
        {
            stringstream A(s);
            A >> n >> q;
        }
        vector<int> maxdist(n);
        vector<double> speed(n);
        {
            for (int i = 0; i < n; ++i) {
                getline(cin, s);
                stringstream A(s);
                A >> maxdist[i] >> speed[i];
            }
        }
        vector<vector<int> > dist(n, vector<int>(n));
        {
            for (int i = 0; i < n; ++i) {
                getline(cin, s);
                stringstream A(s);
                for (int j = 0; j < n; ++j)
                    A >> dist[i][j];
            }
        }
        vector<int> from(q);
        vector<int> to(q);
        {
            for (int i = 0; i < q; ++i) {
                getline(cin, s);
                stringstream A(s);
                A >> from[i] >> to[i];
            }
        }

        // special testcase
        /*
        if (n == 1) {
            n = 100;
            maxdist = vector<int>(n, 1000000000);
            speed = vector<double>(n, 1);
            dist = vector<vector<int> >(n, vector<int>(n, 1));
            for (int i = 0; i < n; ++i)
                dist[i][i] = -1;
        }
        */

        ret_t ret = solver.solve(n, q, maxdist, speed, dist, from, to);
        //cerr<<"case done"<<endl;

        // *** give output ***
        //cout << "Case #" << no << ": " << ret << endl; // one line
        cout << "Case #" << no << ":"; for (int i = 0; i < ret.size(); ++i) cout << " " << setprecision(7) << ret[i]; cout << endl; // vector
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}

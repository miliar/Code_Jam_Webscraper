#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef int ret_t;

class Solver {
public:
    ret_t solve(int n, int p, vector<int> g) {
        ret_t ret = 0;

        vector<int> par(p, 0);
        for (int i = 0; i < n; ++i) {
            ++par[g[i] % p];
        }
        for (int i = 0; i < p; ++i) cerr << ' ' << par[i]; cerr << endl;

        if (p == 2) {
            ret = par[0] + (par[1] + 1) / 2;
        }
        else if (p == 3) {
            ret = par[0]; // 3
            //cerr << ret << endl;

            int m = min(par[1], par[2]);
            ret += m; // 1+2
            //cerr << ret << endl;
            par[1] -= m;
            par[2] -= m;

            ret += (par[1] + par[2] + 2) / 3;
            //cerr << ret << endl;
        }
        else {
            ret = par[0]; // 4

            int m = min(par[1], par[3]);
            ret += m;
            par[1] -= m;
            par[3] -= m;

            int best = 0;
            for (int k = 0; k <= par[2]; k += 2) {
                int cur = k / 2;
                vector<int> tmp(par);
                tmp[0] = 0;
                tmp[2] -= k;
                while (tmp[1] > 0 || tmp[2] > 0 || tmp[3] > 0) {
                    if (tmp[2] > 0 && (tmp[1] >= 2 || tmp[3] >= 2)) {
                        tmp[2] -= 1;
                        tmp[1] -= 2;
                        tmp[3] -= 2;
                        cur += 1;
                    }
                    else if (tmp[1] >= 4 || tmp[3] >= 4) {
                        tmp[1] -= 4;
                        tmp[3] -= 4;
                        cur += 1;
                    }
                    else {
                        cur += 1;
                        tmp[1] = tmp[2] = tmp[3] = 0;
                    }
                }
                if (cur > best)
                    best = cur;
            }
            ret += best;
            // TODO
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
        int ng, p;
        {
            stringstream A(s);
            A >> ng >> p;
        }
        vector<int> g(ng, -1);
        getline(cin, s);
        {
            stringstream A(s);
            for (int i = 0; i < ng; ++i)
                A >> g[i];
        }
        ret_t ret = solver.solve(ng, p, g);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
        //cout << "Case #" << no << ":"; for (int i = 0; i < ret.size(); ++i) cout << " " << ret[i]; cout << endl; // vector
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}

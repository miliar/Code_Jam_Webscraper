#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef double ret_t;

class Solver {
public:
    ret_t solve(double d, int n, vector<double> init, vector<double> speed) {
        ret_t ret;
        double time = 0.0;
        for (int i = 0; i < n; ++i) {
            //cerr<<d<<'\t'<<init[i]<<'\t'<<speed[i]<<endl;
            time = max(time, (d - init[i]) / speed[i]);
        }
        return d / time;
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
        int d, n;
        {
            stringstream A(s);
            A >> d >> n;
        }
        vector<double> init(n);
        vector<double> speed(n);
        for (int i = 0; i < n; ++i) {
            getline(cin, s);
            stringstream A(s);
            A >> init[i] >> speed[i];
        }
        ret_t ret = solver.solve(d, n, init, speed);

        // *** give output ***
        cout << "Case #" << no << ": " << setprecision(7) << ret << endl; // one line
        //cout << "Case #" << no << ":"; for (int i = 0; i < ret.size(); ++i) cout << " " << ret[i]; cout << endl; // vector
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}

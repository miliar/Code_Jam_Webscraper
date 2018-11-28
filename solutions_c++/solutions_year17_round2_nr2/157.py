#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef string ret_t;

class Solver {
public:
    ret_t solve(int n, vector<int> c) {
        vector<int> a(n);
        ret_t fail("IMPOSSIBLE");
        int wp = 0;
        int k = 0;
        if (c[k] == 0) k += 2;
        if (c[k] == 0) k += 2;
        if (c[k] == 0) return fail;
        a[wp++] = k;
        c[k]--;
        while (wp < n) {
            int prev = a[wp-1];
            if (prev % 2 == 1) {
                k = (prev + 3) % 6;
                if (c[k] == 0) return fail;
                a[wp++] = k;
                c[k]--;
                cerr << k;
            }
            else if (c[(prev + 3) % 6] > 0) {
                k = (prev + 3) % 6;
                a[wp++] = k;
                c[k]--;
                cerr << k;
            }
            else {
                int diff = c[(prev + 2) % 6] - c[(prev + 5) % 6]
                    - (c[(prev + 4) % 6] - c[(prev + 1) % 6]);
                if (diff > 0 || (diff == 0 && a[0] != (prev + 4) % 6))
                    k = (prev + 2) % 6;
                else
                    k = (prev + 4) % 6;
                if (c[k] == 0) return fail;
                a[wp++] = k;
                c[k]--;
                cerr << k;
            }
        }
        if (a[0] == a[n-1]) return fail;
        if (a[n-1] % 2 == 1 && a[0] != (a[n-1] + 3) % 6)
            return fail;
        ret_t rainbow("ROYGBV");
        ret_t ret(n, '?');
        for (int i = 0; i < n; ++i)
            ret[i] = rainbow[a[i]];
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
        int n;
        vector<int> c(6);
        {
            stringstream A(s);
            A >> n;
            for (int i = 0; i < 6; ++i)
                A >> c[i];
        }
        ret_t ret = solver.solve(n, c);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
        //cout << "Case #" << no << ":"; for (int i = 0; i < ret.size(); ++i) cout << " " << ret[i]; cout << endl; // vector
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}

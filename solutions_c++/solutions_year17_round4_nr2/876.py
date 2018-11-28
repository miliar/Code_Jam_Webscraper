#include <cassert>
#include <complex>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iostream>
#include <iterator>
#include <limits>
#include <numeric>
#include <sstream>
#include <utility>
#include <cmath>

#include <algorithm>
#include <bitset>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

#include <memory.h>
using namespace std;

#define Pi 3.141592653589793
#define all(c) (c).begin(), (c).end()
typedef long long ll;

template <typename T>
int numbits(T n) {
    return n ? 1 + numbits(n & (n - 1)) : 0;
}

class timer {
public:
    timer() : t_(clock()) {}
    void restart() { t_ = clock(); }
    float elapsed() { return float(clock() - t_) / CLOCKS_PER_SEC; }
private:
    clock_t t_;
};

void run();

int main() {
    // freopen("in.txt", "r", stdin);

#ifdef LOCAL_HOST
    freopen("out.txt", "w", stdout);
    timer t;
#endif
    run();
#ifdef LOCAL_HOST
    // printf("\nElapsed time: %.9f\n", t.elapsed());
#endif
    return 0;
}

struct Cmp {
    bool operator()(const vector<int>& a, const vector<int>& b) const {
        return a.size() > b.size();
    }
};

int solve(int rides, const vector< vector<int> > custs) {
    int cnts[1024];
    for (int i = 0; i < 1024; ++i) {
        cnts[i] = rides;
    }
    int res = 0;
    for (int i = 0; i < custs.size(); ++i) {
        for (int j = 0; j < custs[i].size(); ++j) {
            int val = custs[i][j];
            // cout << "here " << val << " " << cnts[val] << endl;
            if (cnts[val]) {
                cnts[val]--;
            } else {
                while (val && !cnts[val]) {
                    val--;
                }
                if (val) {
                    cnts[val]--;
                    res++;
                } else {
                    return -1;
                }
            }
        }
    }
    return res;
}

void run() {
    int T; cin >> T;
    for (int cs = 0; cs < T; ++cs) {
        int n, c, m;
        cin >> n >> c >> m;
        vector< vector<int> > cust(c + 1);
        for (int i = 0; i < m; ++i) {
            int a, b; cin >> a >> b;
            cust[b].push_back(a);
        }
        int mn = 1;
        for (int i = 0; i < cust.size(); ++i) {
            sort(all(cust[i]));
            mn = max(mn, int(cust[i].size()));
        }
        sort(all(cust), Cmp());
        int mx = 1000;
        for (int i = 0; i < 30; ++i) {
            int md = (mn + mx) / 2;
            // cout << md << " " << solve(md, cust) << endl;
            if (solve(md, cust) != -1) {
                mx = md;
            } else {
                mn = md + 1;
            }
        }
        cout << "Case #" << cs + 1 << ": " << mn << " " << solve(mn, cust) << endl;
    }
}


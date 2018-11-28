#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cmath>
#include <cctype>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <utility>
#include <algorithm>
#include <bitset>
#include <iomanip>

using namespace std;

typedef long long int LLI;

#define _ ios_base::sync_with_stdio(0);

const int inf = 0x3f3f3f3f;
const double eps = 1e-8; 

int n, p;
double r[55];
double q[55][1005];
int idx[55];

int main() { _
    int t;
    cin >> t;
    for (int kase = 1; kase <= t; ++kase) {
        cout << "Case #" << kase << ": ";
        cin >> n >> p;
        for (int i = 0; i < n; ++i) {
            cin >> r[i];
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < p; ++j) {
                cin >> q[i][j];
            }
            sort(q[i], q[i]+p);
        }
        memset(idx, 0, sizeof(idx));
        int serve = 1;
        int cnt = 0;
        int done = 0;
        bool good, under;
        while (!done) {
            good = 1;
            under = 0;
            for (int i = 0; i < n; ++i) {
                if (q[i][idx[i]] < 0.9*serve*r[i]) {
                    idx[i]++;
                    if (idx[i] == p) ++done;
                    good = 0;
                    under = 1;
                }
            }
            if (!done && good) {
                for (int i = 0; i < n; ++i) {
                    if (q[i][idx[i]] > 1.1*serve*r[i]) {
                        good = 0;
                    }
                }
            }
            if (!done && good) {
                ++cnt;
                for (int i = 0; i < n; ++i) {
                    idx[i]++;
                    if (idx[i] == p) ++done;
                }
            }
            if (!good && !under) ++serve;
            // cout << serve << " " << cnt << "\n";
        }
        cout << cnt << "\n";
    }

    return 0;
}

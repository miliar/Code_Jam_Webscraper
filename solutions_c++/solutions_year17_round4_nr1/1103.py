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
#include <cassert>

using namespace std;

typedef long long int LLI;

#define _ ios_base::sync_with_stdio(0);
#define debug

const int inf = 0x3f3f3f3f;
const double eps = 1e-8; 

int g[105];
int cnt[5];

int main() { _
    int t, n, p;
    int res, tmp;
    cin >> t;
    for (int kase = 1; kase <= t; ++kase) {
        memset(cnt, 0, sizeof(cnt));
        cin >> n >> p;
        for (int i = 0; i < n; ++i) {
            cin >> g[i];
            cnt[g[i]%p]++;
        }

        res = cnt[0];
        if (p == 2) {
            res += ceil((double)cnt[1]/2);
        } else if (p == 3) {
            tmp = min(cnt[1], cnt[2]);
            res += tmp;
            cnt[1] -= tmp, cnt[2] -= tmp;
            res += ceil((double)cnt[1]/3);
            res += ceil((double)cnt[2]/3);
        } else {
            tmp = min(cnt[1], cnt[3]);
            res += tmp;
            cnt[1] -= tmp, cnt[3] -= tmp;
            tmp = cnt[2]/2;
            res += tmp;
            cnt[2] -= 2*tmp;
            if (cnt[2]) {
                ++res;
                cnt[1] -= 2;
                if (cnt[1] > 0) {
                    res += ceil((double)(cnt[1])/4);
                }
                cnt[3] -= 2;
                if (cnt[3] > 0) {
                    res += ceil((double)cnt[3]/4);
                }
            } else {
                res += ceil((double)cnt[1]/4);
                res += ceil((double)cnt[3]/4);
            }
        }
        cout << "Case #" << kase << ": " << res << "\n";
    }

    return 0;
}

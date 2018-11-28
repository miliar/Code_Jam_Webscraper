#include <iostream>
#include <string>
#include <algorithm>
#include <unordered_set>
#include <algorithm>
#include <functional>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <bitset>
#include <unordered_map>
#include <iomanip>
#include <queue>

#define mp make_pair
#define pb push_back
#define FI first
#define SI second


#ifdef _MSC_VER
#define ALIGN(x) __declspec(align(x))
#else
#define ALIGN(x) __attribute__((aligned(x)))
#endif

using namespace std;

typedef long long ll;

const int maxn = 1000007;

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    freopen("B-small-attempt2.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;
        string ans = "";
        vector<pair<int, char> > z = {mp(R, 'R'), mp(Y, 'Y'), mp(B, 'B')};
        sort(z.begin(), z.end(), greater<pair<int, char> > ());
        if (z[0].FI > z[1].FI + z[2].FI) {
            ans = "IMPOSSIBLE";
        } else {
            ans = "#";
            for (int i = 0; i < N; ++i) {
                sort(z.begin(), z.end(), greater<pair<int, char> >());
                if (ans.back() != z[0].SI) {
                    ans += z[0].SI;
                    z[0].FI -= 1;
                } else {
                    ans += z[1].SI;
                    z[1].FI -= 1;
                }
            }
            ans = ans.substr(1);
            int nn = ans.size();
            if (ans.front() == ans.back()) swap(ans[nn - 1], ans[nn - 2]);
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}

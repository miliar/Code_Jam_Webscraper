#include <cstdio>
#include <algorithm>
#include <set>
using namespace std;
const double EPS = 1e-8;
int r[110], q[110][110], low[110][110], high[110][110], vst[110][110];
int main() {
    int T = 0;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int n, p;
        scanf("%d%d", &n, &p);
        for (int i = 0; i < n; i++) scanf("%d", &r[i]);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < p; j++) scanf("%d", &q[i][j]);
            sort(q[i], q[i] + p);
        }
        set<int> s;
        for (int j = 0; j < p; j++) {
            for (int i = 0; i < n; i++) {
                low[i][j] = int(ceil(q[i][j] / (1.1 * r[i])) +EPS);
                high[i][j] = int(floor(q[i][j] / (0.9 * r[i])) +EPS);
                vst[i][j] = false;
                s.insert(low[i][j]);
                s.insert(high[i][j]);
            }
        }
        int ans = 0;
        for (auto &val : s) {
            while (true) {
                int cnt = 0;
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < p; j++)
                    if (!vst[i][j] && low[i][j] <= val && val <= high[i][j]) {
                        cnt++;
                        break;
                    }
                }
                if (cnt < n) break;
                ans++;
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < p; j++)
                    if (!vst[i][j] && low[i][j] <= val && val <= high[i][j]) {
                        vst[i][j] = true;
                        break;
                    }
                }
            }
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}

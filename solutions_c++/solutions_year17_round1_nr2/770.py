#include <cstdio>
#include <vector>
#include <cstring>
using namespace std;

int minK(int r, int q) {
    // ceil(q / (1.1 * r))
    return (10 * q + 11 * r - 1) / (11 * r);
}

int maxK(int r, int q) {
    // floor(q / (0.9 * r))
    return (10 * q) / (9 * r);
}

const int N = 50, P = 50, K = 1100000;
int n, p;
int r[N], q[N][P];

bool valid(int k, int idx[N]) {
    for (int i = 0; i < n; ++i) {
        if (idx[i] >= p) return false;
        if (k < minK(r[i], q[i][idx[i]])) return false;
        if (k > maxK(r[i], q[i][idx[i]])) return false;
    }
    return true;
}

int gao_large() {
    int idx[N] = {}, k = 1, ans = 0;
    for (bool done = false; !done;) {
        // raise idx[] for current k
        for (int i = 0; i < n; ++i) {
            while (idx[i] < p && k > maxK(r[i], q[i][idx[i]])) ++idx[i];
            if (idx[i] >= p) {
                done = true;
                break;
            }
        }
        if (valid(k, idx)) {
            // if valid, raise ans and idx[] (used)
            ++ans;
            for (int i = 0; i < n; ++i) ++idx[i];
        } else {
            // if invalid, raise k at least 1
            ++k;
            for (int i = 0; i < n; ++i) {
                k = max(k, minK(r[i], q[i][idx[i]]));
            }
        }
    }
    return ans;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        scanf("%d%d", &n, &p);
        for (int i = 0; i < n; ++i) {
            scanf("%d", &r[i]);
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < p; ++j) {
                scanf("%d", &q[i][j]);
            }
            sort(q[i], q[i] + p);
        }
        int ans = gao_large();
        printf("Case #%d: %d\n", cas, ans);
    }
}

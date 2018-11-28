#include <cstdio>
#include <algorithm>

constexpr int MAX_N = 55;
constexpr double EPS = 1e-9;

using namespace std;

int t, n, p;
int req[MAX_N];
double have[MAX_N][MAX_N];
int rem[MAX_N][MAX_N];
int idx[MAX_N];

int main() {
    scanf(" %d", &t);
    for (int q = 1; q <= t; q++) {
        scanf(" %d %d", &n, &p);
        for (int i = 0; i < n; i++) {
            scanf(" %d", &req[i]);
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < p; j++) {
                int cur;
                scanf(" %d", &cur);
                have[i][j] = 1.0 * cur / req[i];
                rem[i][j] = cur % req[i];
            }
            sort(have[i], have[i] + p);
            idx[i] = 0;
        }

        int ans = 0;

        while (true) {
            bool done = false;
            for (int i = 0; i < n; i++) {
                if (idx[i] == p) {
                    done = true;
                }
            }
            
            if (done) break;

            int best = 0;
            for (int i = 0; i < n; i++) {
                if (have[i][idx[i]] < have[best][idx[best]]) {
                    best = i;
                }
            }

            bool poss = true;
            int x = (int) (have[best][idx[best]] / 0.9 + EPS);
            double most = 1.1 * x;

            for (int i = 0; i < n; i++) {
                if (have[i][idx[i]] > most + EPS) {
                    poss = false;
                    break;
                }
            }
            
            if (!poss) {
                idx[best]++;
            } else {
                ans++;
                for (int i = 0; i < n; i++) {
                    idx[i]++;
                }
            }
        }

        printf("Case #%d: %d\n", q, ans);
    }
    
    return 0;
}

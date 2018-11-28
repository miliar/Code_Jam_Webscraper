#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
using namespace std;

typedef long long LL;
typedef long double LD;

int T, cas = 1;
int N, C, M, B[1002][1002];

int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    scanf("%d", &T);
    while (cas <= T) {
        scanf("%d %d %d", &N, &C, &M);
        memset(B, 0, sizeof(B));
        for (int i = 0; i < M; i++) {
            int Pi, Bi;
            scanf("%d %d", &Pi, &Bi);
            B[Bi][Pi]++;
        }
        int y = 0, z = 0;
        if (C == 2) {
            for (;;) {
                int max_p = 0;
                for (int i = 1; i <= N; i++) {
                    if (B[2][i] + B[1][i] > B[2][max_p] + B[1][max_p]) {
                        max_p = i;
                    }
                    else if (B[2][i] + B[1][i] == B[2][max_p] + B[1][max_p]) {
                        if (max(B[2][i], B[1][i]) > max(B[2][max_p], B[1][max_p]))
                            max_p = i;
                    }
                }
                if (B[2][max_p] + B[1][max_p] <= 0) break;
                int p1 = 2;
                if (B[1][max_p] > B[2][max_p]) p1 = 1;
                int max_p2 = 0;
                for (int i = 1; i <= N; i++) {
                    if (i == max_p) continue;
                    if (B[2][i] + B[1][i] > B[2][max_p2] + B[1][max_p2]) {
                        max_p2 = i;
                    }
                    else if (B[2][i] + B[1][i] == B[2][max_p2] + B[1][max_p2]) {
                        if (B[3 - p1][i]> B[3 - p1][max_p2])
                            max_p2 = i;
                    }
                }
                if (B[2][max_p2] + B[1][max_p2] <= 0) {
                    if (max_p > 1) {
                        y += max(B[2][max_p], B[1][max_p]);
                        z = min(B[2][max_p], B[1][max_p]);
                    }
                    else {
                        y += (B[1][max_p] + B[2][max_p]);
                    }
                    break;
                }
                if (B[3 - p1][max_p2] <= 0) {
                    y++;
                    B[p1][max_p]--;
                }
                else {
                    y++;
                    B[p1][max_p]--;
                    B[3 - p1][max_p2]--;
                }
            }
        }
        printf("Case #%d: %d %d\n", cas, y, z);
        cas++;
    }
    return 0;
}
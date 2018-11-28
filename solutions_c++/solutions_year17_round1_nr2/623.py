#include <vector>

#include <stdio.h>
#include <limits.h>

using namespace std;

int main()
{
    int t;
    scanf("%d", &t);
    for (int cases = 1; cases <= t; cases++) {
        int n, p;
        scanf("%d%d", &n, &p);
        int r[n];
        for (int i = 0; i < n; i++) {
            scanf("%d", &r[i]);
        }
        int q[n][p];
        bool mark[n][p];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < p; j++) {
                scanf("%d", &q[i][j]);
                mark[i][j] = false;
            }
        }
        for (int k = 0; k < p; k++) {
            int v = q[0][k];
            int x = v / r[0];
            int left = x;
            int right = x;
            while (left > 0 && v < left * r[0] * 1.1) {
                left--;
            }
            while (v > right * r[0] * 0.9) {
                right++;
            }
            for (int now = left; now <= right; now++) {
                double lb = now * r[0] * 0.9;
                double rb = now * r[0] * 1.1;
                if (v < lb || v > rb) {
                    continue;
                }
                vector<vector<int> > tmp(n);
                tmp[0].push_back(k);
                bool find = true;
                for (int i = 1; i < n && find; i++) {
                    find = false;
                    lb = now * r[i] * 0.9;
                    rb = now * r[i] * 1.1;
                    for (int j = 0; j < p; j++) {
                        if (q[i][j] >= lb && q[i][j] <= rb) {
                            find = true;
                            tmp[i].push_back(j);
                        }
                    }
                }
                if (find) {
                    for (int i = 0; i < n; i++) {
                        for (int j = 0; j < tmp[i].size(); j++) {
                            mark[i][tmp[i][j]] = true;
                        }
                    }
                }
            }
        }
        int ans = p;
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j < p; j++) {
                count += mark[i][j];
            }
            ans = min(ans, count);
        }
        printf("Case #%d: %d\n", cases, ans);
    }
    return 0;
}

#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <set>
#include <unordered_set>
#include <map>
#include <string>
#include <unordered_map>
#include <string>
#include <vector>
#include <queue>
#include <string.h>
#include <algorithm>


using namespace std;

typedef pair<int ,int> pp;

double dp[2][1001][2];
int main() {
    int t;
    scanf("%d", &t);
    const static double PI = atan(1)*4;
    for (int i = 0; i < t; ++i) {
        int n, k;
        scanf("%d%d", &n, &k);
        vector<pp> p;
        for (int j = 0; j < n; ++j) {
            int r, h;
            scanf("%d%d", &r, &h);
            p.push_back(make_pair(r, h));
        }
        sort(p.begin(), p.end(), [&](const pp&a, const pp&b) {
            long long va = a.first;
            va *= a.second;
            long long vb = b.first;
            vb *= b.second;
            return va > vb;
        });
        double ans = 0;
        for (int j = 0; j < n; ++j) {
            double tmp = p[j].first + 2 * p[j].second;
            tmp *= p[j].first;
            for (int l = 0, cnt = 1; cnt < k; ++l) {
                if (l == j) {
                    continue;
                }
                ++cnt;
                tmp += p[l].first * (double)p[l].second * 2.0;
            }
            if (tmp > ans) {
                ans = tmp;
            }
        }
        ans *= PI;
        printf("Case #%d: %.7lf", (i + 1), ans);
        if (i + 1 < t) {
            printf("\n");
        }
    }
    return 0;
}

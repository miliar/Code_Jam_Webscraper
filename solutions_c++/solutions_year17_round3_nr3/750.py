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

int main() {
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n, k;
        scanf("%d%d", &n, &k);
        double u;
        scanf("%lf", &u);
        vector<double> p;
        for (int j = 0; j < n; ++j) {
            double v;
            scanf("%lf", &v);
            p.push_back(v);
        }
        sort(p.begin(), p.end());
        double s = u;
        double ans = 1.0;
        for (int j = 0; ; ++j) {
            if (j == n) {
                for (int k = 0; k < j; ++k) {
                    ans *= s / j;
                }
                break;
            }
            if (s + p[j] < p[j] * (j + 1)) {
                for (int k = 0; k < j; ++k) {
                    ans *= (s / (j));
                }
                for (; j < n; ++j) {
                    ans *= p[j];
                }
                break;
            }
            s += p[j];
            //cout << j << ' ' << s << ' ' << (s / (j + 1)) << endl;;
        }
        
        printf("Case #%d: ", (i + 1));
        if (ans < 0.1) {
            printf("0.");
            for (int j = 0; j < 400 && ans < 1; ++j) {
                ans *= 10;
                if (ans >= 1) {
                    break;
                }
                printf("0");
            }
            for (int j = 0; j < 10; ++j) {
                int t = ans;
                printf("%d", t);
                ans -= t;
                ans *= 10;
            }
        } else {
            printf("%.7lf", ans);
        }
        if (i + 1 < t) {
            printf("\n");
        }
    }
    return 0;
}

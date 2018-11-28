#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>

#define LL long long
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define PII pair<int, int>
#define PID pair<int, double>

using namespace std;

int n, p, a, T;
int r[4];

int main(){
    cin >> T;
    for (int id = 1; id <= T; id++) {
        printf("Case #%d: ", id);

        cin >> n >> p;
        r[0] = r[1] = r[2] = r[3] = 0;
        for (int i = 0; i < n; ++i) {
            cin >> a;
            r[a % p] ++;
        }

        if (p == 2) {
            printf("%d\n", r[0] + (1 + r[1]) / 2);
        } else if (p == 3) {
            int ans = r[0];
            int x = min(r[1], r[2]);
            ans += x;
            x = max(r[1], r[2]) - x;
            ans += (x + 2) / 3;
            printf("%d\n", ans);
        } else {
            int ans = r[0];
            ans += r[2] / 2;
            r[2] = r[2] % 2;
            int x = min(r[1], r[3]);
            ans += x;
            x = max(r[1], r[3]) - x + r[2];
            ans += (x + 2) / 3;
            printf("%d\n", ans);
        }
    }
}

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <list>


using namespace std;

int p[3];

int main() {
    int test, n, m;
    scanf("%d", &test);
    for (int cas = 1; cas <= test; cas++) {
        scanf("%d%d", &n, &m);
        memset(p, 0, sizeof(p));
        for (int i = 0; i < n; i++) {
            int a;
            scanf("%d", &a);
            p[a % m]++;
        }
        int res;
        if (m == 2) {
            res = p[0] + (p[1] + 1) / 2;
        }
        else {
            res = p[0] + min(p[1], p[2]);
            int tmp = max(p[1], p[2]) - min(p[1], p[2]);
            res = (res + (tmp + 2) / 3);
        }
        printf("Case #%d: %d\n", cas, res);
    }
    return 0;
}

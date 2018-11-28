#include <cmath>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <vector>
#include <set>
using namespace std;

const int maxn = 1000 + 10;

int p[maxn], b[maxn];

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int T, kase = 0; scanf("%d",&T);
    while (T--) {
        printf("Case #%d: ",++kase);
        int n, c, m; scanf("%d%d%d",&n,&c,&m);
        for (int i = 0; i < m; i ++) {
            scanf("%d%d",&p[i],&b[i]);
        }
        vector<int> v1, v2;
        for (int i = 0; i < m; i ++) {
            if (b[i] == 1) v1.push_back(p[i]);
            else v2.push_back(p[i]);
        }
        int g1 = 0, g2 = 0;
        for (int i = 0; i < v1.size(); i ++) {
            if (v1[i] == 1) g1 ++;
        }
        for (int i = 0; i < v2.size(); i ++) {
            if (v2[i] == 1) g2 ++;
        }
        int y = max((int)max(v1.size(), v2.size()), g1 + g2);
        int z = 0;
        for (int i = 2; i <= n; i ++) {
            int g = 0;
            for (int j = 0; j < m; j ++) {
                if (p[j] == i) g ++;
            }
            z += max(0, g - y);
        }
        printf("%d %d\n",y,z);
    }
    return 0;
}

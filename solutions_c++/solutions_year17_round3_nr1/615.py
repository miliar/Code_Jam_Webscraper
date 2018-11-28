#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstring>
#include <cmath>
#include <stack>
using namespace std;
//#define LOCAL

const double PI = acos(-1);

struct Node {
    double r, h;
};

bool cmp1(Node & x, Node & y) {
    return x.r > y.r;
}

bool cmp2(Node & x, Node & y) {
    return x.r * x.h > y.r * y.h;
}

const int maxn = 1000 + 100;

Node a[maxn];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, kase = 0; scanf("%d",&T);
    while (T--) {
        int n, k; scanf("%d%d",&n,&k);
        for (int i = 0; i < n; i ++) {
            scanf("%lf%lf",&a[i].r,&a[i].h);
        }
        sort(a, a + n, cmp1);
        vector<Node> v;
        double sum = 0, res = 0;
        for (int i = 0; i < n; i ++) {
            v.clear();
            for (int j = i+1; j < n; j ++) {
                v.push_back(a[j]);
            }
            if (v.size() + 1 < k) break;
            sort(v.begin(), v.end(), cmp2);
            sum += a[i].r * a[i].r * PI;
            sum += 2 * PI * a[i].r * a[i].h;
            
            for (int j = 0; j < k-1; j ++) {
                sum += 2 * PI * v[j].r * v[j].h;
            }
            
            res = max(res, sum);
            sum = 0;
        }
        printf("Case #%d: %.12f\n",++kase,res);
    }
    return 0;
}

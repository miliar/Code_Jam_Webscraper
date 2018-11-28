#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <stack>
using namespace std;
typedef int64_t ll;
const int inf = 0x3f3f3f3f;
const int mod = 1000003;
const double pi = 3.141592653589793238462643383279;

struct pz{
    ll r;
    ll h;
};

bool operator <(const pz &a, const pz &b) {
    return a.h * a.r < b.h * b.r;
}

int t, n, k;
ll res, mx;
int ptr;

int main() {
    freopen("in", "r", stdin);
    freopen("out0", "w", stdout);
    scanf("%d", &t);
    for (int ncase = 1; ncase <= t; ncase++) {
        pz p[1005];
        mx = 0;
        scanf("%d%d", &n, &k);
        for (int i = 0; i < n; i++) {
            scanf("%lld%lld", &p[i].r, &p[i].h);
        }
        mx = 0;
        for (ptr = 0; ptr < n; ptr++) {
            priority_queue<pz> v;
            for (int i = 0; i < ptr; i++)
                v.push(p[i]);
            for (int i = ptr + 1; i < n; i++)
                v.push(p[i]);
            res = p[ptr].r * p[ptr].r + p[ptr].r * p[ptr].h + p[ptr].r * p[ptr].h;
            for (int i = 0; i < k - 1; i++) {
                res += (v.top().r * v.top().h + v.top().r * v.top().h);
                v.pop();
            }
            if (res > mx)
                mx = res;
        }
        double newres = mx * pi;
        printf("Case #%d: %.9lf\n", ncase, newres);
    }
    return 0;
}
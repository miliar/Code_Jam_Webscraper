#include <cstdio>
#include <algorithm>
#include <cmath>
#include <iostream>
#define PI acos(-1.0)
#define EPS 1e-6

using namespace std;

class Pie{
public:
    double top, side;
    Pie(double _t = 0, double _s = 0): top(_t), side(_s) {}
};

Pie pie[1005];

int dcmp(double x) { return x < -EPS ? -x : x > EPS; }

bool cmp1(Pie p1, Pie p2) {
    if (dcmp(p1.side-p2.side) == 0)
        return p1.top > p2.top;
    return p1.side > p2.side;
}

void solve() {
    double tmp = 0, ans = 0, maxtop = 0;
    int N, K;
    scanf("%d%d",&N,&K);
    for (int i = 0; i < N; ++i) {
        int r, h;
        scanf("%d%d",&r,&h);
        pie[i] = Pie((double)r*r*PI,(double)2*r*PI*h);
    }

    sort(pie,pie+N,cmp1);

    int cur = 0;
    for (; cur < K-1; ++cur) {
        tmp += pie[cur].side;
        maxtop = max(maxtop,pie[cur].top);
    }

    if(pie[cur].top > maxtop) {
        ans = tmp + pie[cur].top + pie[cur].side;
    }
    else {
        ans = tmp + maxtop + pie[cur].side;
    }

    for (cur = cur+1; cur < N; ++cur) {
        if(pie[cur].top > maxtop) {
            ans = max(ans,tmp + pie[cur].top + pie[cur].side);
        }
        else {
            ans = max(ans,tmp + maxtop + pie[cur].side);
        }
    }
    printf("%.9lf\n",ans);
}


int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int test;
    scanf("%d",&test);
    for (int t = 1; t <= test; ++t) {
        printf("Case #%d: ",t);
        solve();
    }
    return 0;
}

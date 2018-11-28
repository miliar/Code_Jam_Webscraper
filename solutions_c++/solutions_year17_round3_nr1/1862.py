#include <cstdio>
#include <utility>
#include <cmath>
#include <algorithm>
#define PI acos(-1.0)

using namespace std;

int T, cas;
int K, N, index, R, H;
pair<double, double> pancake[1005], cand[1005];
double ans, area, max_r, cur, max_0;


bool cmp(pair<double, double> a, pair<double, double> b) {

    return a.second == b.second ? a.first > b.first : a.second > b.second;
}

void solve() {
    ans = area = 0.0;
    max_r = -1;
    index = 0;

    sort(pancake, pancake+N, cmp);

    int cur = 0;

    for(; cur < K-1; ++cur) {
        area += pancake[cur].second;
        max_r = max(max_r, pancake[cur].first);
    }

    if(max_r < pancake[cur].first) {
        ans = area + pancake[cur].first + pancake[cur].second;
    }
    else {
        ans = area + max_r + pancake[cur].second;
    }

    for(cur = cur+1; cur < N; ++cur) {
        if(max_r < pancake[cur].first) {
            ans = max(ans, area + pancake[cur].first + pancake[cur].second);
        }
        else {
            ans = max(ans, area + max_r + pancake[cur].second);
        }
    }
}


int main(void) {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    scanf("%d", &T);
    for(cas = 1; cas <= T; ++cas) {
        scanf("%d %d", &N, &K);
        for(int i = 0; i < N; ++i) {
            scanf("%d %d", &R, &H);
            pancake[i].first = (double)R*R*PI;
            pancake[i].second = (double)2.0*R*PI*H;
        }
        solve();
        printf("Case #%d: %.9lf\n", cas, ans);
    }


    return 0;
}

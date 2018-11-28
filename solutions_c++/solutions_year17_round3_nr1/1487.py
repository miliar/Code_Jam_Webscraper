#include <bits/stdc++.h>

using namespace std;

int main(int argc, const char * argv[]) {
    freopen("/Inputs/GC2017/in.txt", "r", stdin);
    freopen("/Inputs/GC2017/out.txt", "w", stdout);
    
    int t;
    scanf("%d", &t);
    for (int c = 1; c <= t; c++) {
        vector<pair<long long, long long>> ps;
        priority_queue<long long> sides;
        int n, k;
        scanf("%d%d", &n, &k);
        long long r, h;
        for (int i = 0; i < n; i++) {
            scanf("%lld%lld", &r, &h);
            ps.push_back({r, h});
        }
        
        long long mx = -1;
        for (int i = 0; i < n; i++) {
            r = ps[i].first;
            h = ps[i].second;
            long long res = 2 * r * h + r * r;
            
            for (int j = 0; j < n; j++) {
                if (i != j && ps[j].first <= ps[i].first) {
                    r = ps[j].first;
                    h = ps[j].second;
                    sides.push(2 * r * h);
                }
            }
            
            for (int j = 0; j < k-1; j++) {
                if (sides.empty()) {
                    res = 0;
                    break;
                }
                res += sides.top();
                sides.pop();
            }
            
            mx = max(res, mx);
        }
        
        printf("Case #%d: %.8lf\n", c, mx * M_PI);
    }
    return 0;
}

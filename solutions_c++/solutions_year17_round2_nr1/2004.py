#include <bits/stdc++.h>

using namespace std;

const int N = 1e6 + 5;

int main() {
    int t;
    scanf("%d", &t);
    int te = 1;
    while(te <= t) {
        int d, n;
        vector<pair<int, int> > v;
        scanf("%d %d", &d, &n);
        for(int i=0;i<n;i++) {
            int a, b;
            scanf("%d %d", &a, &b);
            v.push_back(make_pair(-a, b));
        }
        sort(v.begin(), v.end());
        double mx = 0.0;
        for(int i=0;i<n;i++) {
            mx = max(mx, ((double)(d+v[i].first))/((double)(v[i].second)));
        }
        printf("Case #%d: %lf\n", te++, ((double)d)/mx);
    }
    return 0;
}


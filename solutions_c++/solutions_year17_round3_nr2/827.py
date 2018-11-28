#include <bits/stdc++.h>

using namespace std;

int ac, aj;
typedef pair<int, int> ii;

int get(vector<ii> x) {
    if (x[1].second - x[0].first <= 720)
        return 2;
    if (x[1].first - x[0].second >= 720)
        return 2;
    return 4;
}

void solve() {
    scanf("%d%d", &ac, &aj);
    vector<ii> vc, vj;
    for(int i = 0; i < ac; ++i) {
        int c, d;
        scanf("%d%d", &c, &d);
        vc.push_back(ii(c, d));
    }
    for(int i = 0; i < aj; ++i) {
        int c, d;
        scanf("%d%d", &c, &d);
        vj.push_back(ii(c, d));
    }
    if (ac <= 1 && aj <= 1) {
        printf("2\n");
        return;
    }
    sort(vc.begin(), vc.end());
    sort(vj.begin(), vj.end());
    if (ac == 2) {
        printf("%d\n", get(vc));
    } else {
        printf("%d\n", get(vj));
    }
}

int main() {
    int ntests;
    scanf("%d", &ntests);
    for(int t = 1; t <= ntests; ++t) {
        printf("Case #%d: ", t);
        solve();
    }
    return 0;
}
#include <bits/stdc++.h>
#define fr(a, b, c) for(int a = b; a < c; ++a)
#define pb push_back

using namespace std;

typedef pair<int, int> ii;

int mark[1002], cost[1002], ls[1002], rs[1002];

bool cmp(ii a, ii b) {
    return (min(a.first, a.second) != min(b.first, b.second)) ? min(a.first, a.second) > min(b.first, b.second) :
                max(a.first, a.second) > max(b.first, b.second);
}

int main() {
    int n, cas = 0;
    cin >> n;
    while (n--) {
        int p, k;
        cin >> p >> k;
        p += 2;

        memset(mark, 0, sizeof mark);
        mark[0] = mark[p-1] = 1;

        int last;
        while (k--) {
            memset(ls, 0, sizeof ls);
            memset(rs, 0, sizeof rs);

            int cur = 0;
            fr(i, 0, p) {
                ls[i] = cur;
                if (mark[i]) cur = 0;
                else ++cur;
            }

            cur = 0;
            for(int i = p-1; i >= 0; i--) {
                rs[i] = cur;
                if (mark[i]) cur = 0;
                else ++cur;
            }

            vector<ii> v;
            fr(i, 0, p) if (!mark[i]) v.pb(ii(ls[i], rs[i]));
            sort(v.begin(), v.end(), cmp);

            fr(i, 0, p) {
                if (!mark[i] && ls[i] == v[0].first && rs[i] == v[0].second) {
                    mark[i] = 1;
                    if (!k) printf("Case #%d: %d %d\n", ++cas, max(v[0].first, v[0].second), min(v[0].first, v[0].second));
                    break;
                }
            }
        }
    }
    return 0;
}
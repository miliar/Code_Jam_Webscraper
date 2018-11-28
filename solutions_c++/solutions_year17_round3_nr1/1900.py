#include <bits/stdc++.h>
using namespace std;

#define fi first
#define sc second
typedef pair<long long, long long> ii;

long double pi = 3.14159265358979323846264338327950288419716939937510;

int main() {
    //freopen("A-large.in", "r", stdin);
    //freopen("A-small-attempt3.in", "r", stdin);
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int tc; cin >> tc;
    for (int tci = 1; tci <= tc; ++tci) {
        int n, k; scanf("%d%d", &n, &k);
        ii p[n];
        for (int i = 0, r, h; i < n; ++i) {
            scanf("%d%d", &r, &h);
            p[i] = ii((long long)r*r, (long long)2*r*h);
        }
        sort(p, p+n, greater<ii>());
        //for (int i = 0; i < n; ++i) printf("%lld %lld\n", p[i].fi, p[i].sc);
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            long long cur = (long long)p[i].fi + p[i].sc;
            vector<long long> r;
            for (int j = i+1; j < n; ++j) r.push_back(p[j].sc);
            sort(r.begin(), r.end(), greater<long long>());
            for (int j = 0; j < min(k-1, (int)r.size()); ++j) cur += r[j];
            //printf("\t %lld :: %lld\n", cur, ans);
            ans = max(ans, cur);
        }
        printf("Case #%d: ", tci);
        cout << setprecision(30) << ans * pi << endl;
        //cout << setprecision(30) << ans << endl;
    }
}

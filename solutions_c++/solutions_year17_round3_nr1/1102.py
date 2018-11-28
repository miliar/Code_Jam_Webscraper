#include <bits/stdc++.h>

using namespace std;

typedef long long lint;

const long double PI=atan(1)*4;
#define pb push_back 
#define mp make_pair 
inline long double calc(pair<int, int> x) {
    return 2 * PI * (long double)x.first * x.second;
}

int main() {
    int t;
    lint n, k;
    scanf("%d", &t);
    map<pair<int,int>, long double> mapa;
    for(int CASE = 1; CASE <= t; CASE++) {
        cerr<< CASE <<endl; 
        scanf("%lld %lld", &n, &k);
        vector<pair<int, int>> pr;
        vector<int> radii;
        int a, b;
        for(int i = 0; i < n; i++) {
            scanf("%d %d", &a, &b);
            pr.push_back(make_pair(a, b));
            radii.push_back(a);
        }
        sort(pr.rbegin(), pr.rend());
        sort(radii.begin(), radii.end());
        radii.resize(unique(radii.begin(),radii.end())-radii.begin());
        mapa.clear();
        mapa[make_pair(0, -1)] = 0;
        for(int i = 0; i < n; i++) {
            vector<pair<pair<int,int>, long double>> o;
            for(auto x: mapa) {
                if(x.first.first + n - i < k) continue;
                if(x.first == make_pair(0, -1)) {
                    o.push_back(mp(mp(1, pr[i].first), PI * pr[i].first * 
                    pr[i].first + calc(pr[i])));
                }
                else if(x.first.first < k && x.first.second >= pr[i].first) {
                    o.pb(mp(mp(x.first.first+1, pr[i].first), x.second + calc(pr[i])));
                }
            }
            for(auto x: o) {
                mapa[x.first] = max(mapa[x.first], x.second);
            }
        }
        long double maxio = 0;
        for(auto x: mapa) {
            if(x.first.first == k) maxio = max(x.second, maxio);
        }
        printf("Case #%d: %.9Lf\n", CASE, maxio);
    }
    return 0;
}
#include <bits/stdc++.h>

using namespace std;

int n, t, w = 1, k;

pair<long double, long double> g[1000];

long double ans;

const long double PI = 3.14159265358979323846;

bool comp(pair<long double, long double> a, pair<long double, long double> b){
    if(a.first * a.second <= b.first * b.second) return true;
    return  false;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    while(w <= t){
        ans = 0;
        cout << "Case #" << w << ": ";
        ++w;
       cin >> n >> k;
       for(int i = 0; i < n; ++i){
           cin >> g[i].second >> g[i].first;
       }
        for(int i = 0; i < n; ++i){
            for(int j = i + 1; j < n; ++j){
                if(!comp(g[i], g[j])) swap(g[i], g[j]);
            }
        }
        reverse(g, g + n);
        for(int i = 0; i < n; ++i){
            int cnt = 1;
            long double a = g[i].second * g[i].second * PI + 2 * g[i].second * PI * g[i].first;
            for(int j = 0; j < n; ++j){
                if(cnt == k) {
                    break;
                }
                if(j != i && g[i].second >= g[j].second){
                    cnt += 1;
                    a += 2 * g[j].second * PI * g[j].first;
                }
            }
            ans = max(ans, a);
            //cout << g[i].first << " " << g[i].second << " " << ans <<  "\n";
        }
        cout << fixed;
        cout << setprecision(12) << ans << "\n";
    }
    return 0;
}
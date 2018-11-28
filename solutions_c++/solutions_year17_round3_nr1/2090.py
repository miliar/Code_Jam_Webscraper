#include "bits/stdc++.h"
using namespace std;
const int N = 1e6 + 5;
const int LGN = 21;
int n , k;
int r[N];
int h[N];
const double pi = 3.1415926535897932384626433832;
double get(int r , int h) {
    double rekt = 1.0 * pi * r * r + 2.0 * pi * r * h;
    return rekt;
}

double solve(vector < pair < int , int > > v) {
    double cur = 0.0;
    sort(v.begin() , v.end());
    for(int i = v.size() - 1; i >= 0; --i) {
        cur += 2.0 * pi * v[i].first * v[i].second;
        cur += 1.0 * pi * v[i].first * v[i].first;
        if(i > 0) {
            cur -= 1.0 * pi * v[i - 1].first * v[i - 1].first;
        }
    }
    return cur;
}

int main() {
    int tt;
    freopen("Round1CA.txt" , "r" , stdin);
    freopen("Round1CAO.txt" , "w" , stdout);
    cin >> tt;
    for(int TT = 1; TT <= tt; ++TT) {
        cout << "Case #" << TT << ": ";
        cin >> n >> k;
        for(int i = 1; i <= n; ++i) {
            cin >> r[i] >> h[i];
        }
        double ans = 0.0;
        for(int i = 0; i < (1 << n); ++i) {
            int cnt = __builtin_popcount(i);
            if(cnt == k) {
            double cur = 0.0;
            vector < pair < int , int > > v;
            for(int j = 0; j < n; ++j) {
                if(i & (1 << j) ) {
                    v.push_back(make_pair(r[j + 1] , h[j + 1]));
                }
            }
            ans = max(ans , solve(v));
        }
    }
    cout << setprecision(10) << fixed << ans << endl;
}
return 0;
}

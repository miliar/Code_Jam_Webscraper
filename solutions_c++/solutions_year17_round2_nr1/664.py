#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <unordered_set>
#include <cmath>
#include <set>
#include <unordered_map>
#include <map>
#include <functional>
#include <iomanip>
#include <vector>
#include <utility>

using namespace std;

typedef long long ll;
typedef long double ld;

const bool debug = false;


ld solve (){
    int d, n;
    cin >> d >> n;
    vector<pair<int, int>> val(n);
    int i;
    for(i = 0; i < n; i++) {
        cin >> val[i].first >> val[i].second;
    }
    sort(val.begin(), val.end());
    ld t = (d - val[n - 1].first) / ((ld)val[n - 1].second);
    for(i = n - 2; i >= 0; i--) {
        ld ct = (d - val[i].first) / ((ld)val[i].second);
        t = max(t, ct);
    }
    ld sp = d / t;
    return sp;

}

int main() {
   ios_base::sync_with_stdio(false);
   if(!debug) {
        freopen("large.in", "r", stdin);
        freopen("large.out", "w", stdout);
    }
    int t;
    cin >> t;
    int i;
    for(i = 1; i <= t; i++) {
        cout << "Case #" << i << ": " <<  fixed << setprecision(7) << solve() << '\n';


        cerr << "Case " << i << '\n';
    }
    return 0;
}

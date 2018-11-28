#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cassert>
#include <map>
#include <unordered_map>
#include <utility>
#include <iomanip>
#include <cmath>
#include <cstdio>

#define FOR(i,n) for(ull i=0;i<ull(n);++i)

using namespace std;

using ull = unsigned long long;

void test() {
    ull n, k; cin >> n >> k;
    vector<pair<ull, ull>>p(n);
    for (auto&& pp:p) cin >> pp.first >> pp.second;
    
    double mx = 0.0;
    FOR (j, n) {
        
        vector<pair<ull, ull>> q(p.begin(), p.end());
        swap(q[0], q[j]);
        
        sort(q.begin()+1, q.end(), [](auto&& a, auto&& b){
            return a.second*a.first > b.first*b.second;
        });
        
        double res = double(q[0].first) * double(q[0].first);
        ull selected = 0;
        FOR(i, n) {
            if (q[i].first > q[0].first) continue;
//            cout << q[i].second << "  " << q[i].first <<endl;
            res = res+ double(q[i].second)*double(q[i].first)*2.0;
            selected++;
            if (selected >= k) break;
        }
        if (selected < k) continue;
        res = res * M_PI;
        mx = max(mx,res);
    }
    printf("%.12f\n", mx);
}

int main() {
    
    ull tn; cin >> tn;
    FOR (t, tn) {
        cerr << t << endl;
        cout << "Case #" << t+1 << ": ";
        test();
    }
    
    return 0;
}

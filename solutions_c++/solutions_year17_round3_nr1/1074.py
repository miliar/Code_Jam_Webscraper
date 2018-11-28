#include<iostream>
#include<cstdio>
#include<utility>
#include<tuple>
#include<vector>
#include<algorithm>
#include<cstdint>
#include<cmath>

using namespace std;
typedef int64_t var;
var t, n, k;

int main(){
    cin >> t;
    for(var _t = 0; _t < t; ++_t){
        cin >> n >> k;
        vector<pair<var,var>> o;
        for(var i = 0; i < n; ++i){
            var b1, b2; 
            cin >> b1 >> b2;
            o.emplace_back(b1,b2);
        }

        sort(o.begin(),o.end());
        var best=0;

        for(var j = k-1; j < n; ++j){
            vector<var> v;
            var maxr = o[j].first;
            var sum = maxr * maxr + 2*o[j].first*o[j].second;
            for(var i = 0; i < j; ++i){
                var b1 = o[i].first;
                var b2 = o[i].second;
                v.emplace_back(2*var(b1)*var(b2));
            }
            sort(v.begin(),v.end(),std::greater<var>());
            for(int i = 0; i < k-1; ++i){
                sum += v[i];
            }
            best = max(best,sum);
        }
        printf("Case #%d: %.06lf\n", _t+1, M_PI*double(best));
    }
    return 0;
}

#include<iostream>
#include<cstdio>
#include<utility>
#include<tuple>
#include<vector>
#include<algorithm>
#include<cstdint>

using namespace std;
typedef int64_t var;
var t, n, k;

int main(){
    cin >> t;
    for(var _t = 0; _t < t; ++_t){
        cin >> n >> k;
        double u;
        vector<double> v;
        cin >> u;
        for(var i = 0; i < n; ++i){
            double buf;
            cin >> buf;
            v.push_back(buf);
        }
        v.push_back(1.0f);
        sort(v.begin(),v.end());
        var i;
        for(i = 0; i < n && u>0.0000001; ++i){
            double to_fill = double(i+1)*(v[i+1]-v[i]);
            v[i]=v[i]+min(to_fill,u/(i+1));
            for(var j = i - 1; j >= 0; --j){
                v[j] = v[i];
            }
            u=max(0.0,u-to_fill);
        }
        double ans = 1.0f;
        for(auto it: v){
            ans*=it;
        }
        printf("Case #%d: %.6lf\n", _t+1, ans);
    }
    return 0;
}

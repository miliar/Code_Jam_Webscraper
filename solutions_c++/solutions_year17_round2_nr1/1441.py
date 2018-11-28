#include<iostream>
#include<cstdio>
#include<utility>
#include<tuple>
#include<vector>
#include<algorithm>
#include<cstdint>

using namespace std;
typedef int64_t var;
var t, n, d;

int main(){
    cin >> t;
    for(var _t = 0; _t < t; ++_t){
        cin >> d >> n;
        double time_taken = 0;
        for(var i = 0; i < n; ++i){
            var k, s;
            cin >> k >> s;
            var dist = d-k;
            double ttaken = ((double)dist)/s;
            time_taken=max(time_taken,ttaken);
        }
        //cout << "Case #" << (_t+1) << ": " << (double)d/time_taken << endl;
        printf("Case #%d: %lf\n", _t+1, d/time_taken);
    }
    return 0;
}

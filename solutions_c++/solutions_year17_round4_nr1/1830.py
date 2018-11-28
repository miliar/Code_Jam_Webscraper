#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll t, cnt, rem[5], p, diff, n, i, a[1005];
int main() {
    cin>>t;
    for(ll _t = 1; _t <= t; _t++) {
        cin>>n>>p;
        memset(rem, 0, sizeof rem);
        for(i = 0; i < n; i++) {
            cin>>a[i];
            rem[a[i]%p]++;
        }
        if(p == 2) {
            cnt = rem[0] + (rem[1]+1)/2;
        }
        else if(p == 3) {
            cnt = rem[0] + min(rem[1], rem[2]) + (abs(rem[1]-rem[2])+2)/3;
        }
        else if(p == 4) {
            diff = abs(rem[1] - rem[2]);
            cnt = rem[0] + min(rem[1], rem[3]) + (rem[2]+1)/2 + diff/4;
            if(rem[2]&1) {
                if(diff%4 > 2) cnt++;
            }
            else {
                if(diff%4) cnt++;
            }
        }
        printf("Case #%lld: %lld\n", _t, cnt);
    }

    return 0;
}

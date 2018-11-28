#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll t, f[100], r[100], mnVal, mxVal, mult, cnt, mxf, p, n, flag, i, j, x, curVal;
vector<ll> q[100];
int main() {
    cin>>t;
    for(ll _t = 1; _t <= t; _t++) {
        cin>>n>>p;
        for(i = 0; i < n; i++) {
            cin>>r[i];
        }
        for(i = 0; i < n; i++) {
            q[i].clear();
            for(j = 0; j < p; j++) {
                cin>>x;
                q[i].push_back(x);
            }
            sort(q[i].begin(), q[i].end());
            f[i] = 0;
        }
        mxf = 0;
        mult = 1;
        cnt = 0;
        while(mxf < p && mult < 1e6+6) {
            flag = 1;
            for(i = 0; i < n; i++) {
                curVal = r[i]*mult;
                mxVal = (curVal*110)/100;
                mnVal = ceil(((double)(curVal*90))/100.0);
                //cout<<mult<<" "<<mnVal<<endl;
                while(q[i][f[i]] < mnVal && f[i] < p) f[i]++;
                if(f[i] < p && q[i][f[i]] >= mnVal && q[i][f[i]] <= mxVal) {

                }
                else {
                    flag = 0;
                }
                mxf = max(mxf, f[i]);
            }
            if(flag) {
                for(i = 0; i < n; i++) {
                    f[i]++;
                    mxf = max(mxf, f[i]);
                }
                cnt++;
                //cout<<" "<<mxf<<" "<<mult<<endl;
            }
            else mult++;
        }
        //cout<<mxf<<" "<<mult<<endl;
        printf("Case #%lld: %lld\n", _t, cnt);

    }

    return 0;
}

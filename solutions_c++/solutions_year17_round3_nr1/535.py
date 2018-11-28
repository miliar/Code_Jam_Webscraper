#include<bits/stdc++.h>

#define pi 3.14159265359

using namespace std;

int n,m,k,l,kk;

long double r[1111],h[1111],mx,q,ans,rr,curr;

main(){
    freopen("22.in","r",stdin);
    freopen("1.txt","w",stdout);

    int t;

    cin >> t;

    for(int T = 1; T <= t; ++T){
        cin >> n >> k;

        vector<pair<long double,int> > v;

        mx = 0.0;
        m = 1;

        for(int i = 1; i <= n; ++i){
            cin >> r[i] >> h[i];
            v.push_back({2.0 * r[i] * h[i] * pi,i});
        }


        sort(v.begin(),v.end());
        reverse(v.begin(),v.end());

        ans = 0.0;
        for(int i = 1; i <= n; ++i){
            curr = r[i] * r[i] * pi + r[i] * pi * h[i] * 2.0;

            kk = k - 1;
            for(int j = 0; j < n; ++j){
                if(!kk) break;
                if(v[j].second != i){
                    curr += v[j].first;
                    kk--;
                }
                if(!kk) break;
            }
            ans = max(ans,curr);
        }

        cout << fixed << setprecision(6)  << "Case #" << T << ": " << ans << "\n";
    }
}

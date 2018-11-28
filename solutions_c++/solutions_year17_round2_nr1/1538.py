// ༼∩ຈل͜ຈ༽つ━☆ﾟ.*･｡ﾟ .·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º> - code by: kdkdk
//#define ONLINE_JUDGE //in case i forget to uncomment this, uncomment this.
#ifdef ONLINE_JUDGE
#include <bits/stdc++.h>
#else
#include "stdc++.h"
#endif

#define int long long
using namespace std;

signed main() {
#ifndef ONLINE_JUDGE
    freopen("/Users/kdkdk/Desktop/input.txt", "r", stdin);
    //freopen("/Users/kdkdk/Desktop/output.txt", "w", stdout);
#endif
    int t; cin >> t;
    for(int c = 1; c <= t; ++c) {
        int d, n; cin >> d >> n;
        vector<pair<int,double> > horses(n); vector<double> arrivalTime(n);
        for(int i = 0; i < n; ++i) cin >> horses[i].first >> horses[i].second;
        //for(int i = 0; i < n; ++i) horses[i].second = 1./horses[i].second;
        sort(horses.begin(), horses.end());
        reverse(horses.begin(), horses.end());
        
        
        for(int i = n-1; i >= 0; --i) {
            arrivalTime[i] = (d - horses[i].first) / horses[i].second;
            if(i < n-1 && arrivalTime[i+1] > arrivalTime[i]) arrivalTime[i] = arrivalTime[i+1];
            //cout << "ARR:" << arrivalTime[i] << endl;
        }
        double resSpeed = (double)d / (double)arrivalTime[0];
        std::cout << std::fixed;
        std::cout << std::setprecision(6);
        cout << "Case #" << c << ": " << resSpeed << endl;
    }
}

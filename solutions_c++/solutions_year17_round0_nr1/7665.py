// ༼∩ຈل͜ຈ༽つ━☆ﾟ.*･｡ﾟ .·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º> - code by: kdkdk
#define ONLINE_JUDGE //in case i forget to uncomment this, uncomment this.
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
    
    ios_base::sync_with_stdio(false); cin.tie(0);
    int t; cin >> t;
    for(int c = 1; c <= t; ++c) {
        int k, flips = 0, possible = 1; string str; cin >> str >> k; vector<int> vec(str.size());
        for(int i = 0; i < str.size() ; ++i) vec[i] = ( str[i] == '+' ? 1 : 0);
        for(int i = 0; i + k <= str.size(); ++i) if(vec[i] == 0 && ++flips) for(int j = 0; j < k; ++j) vec[i+j] = !vec[i+j];
        for(int i = 0; i < str.size(); ++i) if(vec[i] == 0) possible = false;
        cout << "Case #" << c << ": " << (possible ? to_string(flips) : "Impossible") << endl;
    }
    return 0;
}

#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

int main() {
    int t;
    long long int n, k;
    cin >> t;
    for(int z = 1; z <= t; z++) {
        cin >> n >> k;
        vector <ll> v {0, n+1};
        int insert = 0;
        ll m = v[0] + v[1]/2, l = 0, r = 0;
        
        while(insert < k) {
            l = -1, r = -1;
            for(int j = 1; j < v.size(); j++) {
                // cout << "Current Interval: " << v[j-1] << " " << v[j] << endl;
                if(v[j] - v[j-1] == 1)
                    continue;
                ll m1 = v[j-1] + (v[j] - v[j-1])/2;
                ll l1 = m1 - v[j-1] - 1;
                ll r1 = v[j] - m1 - 1;
                if(l1 == -1 && r1 == -1)
                    m = m1, l = l1, r = r1;
                else if(l1 + r1 > l+r)
                    m = m1, l = l1, r = r1;
            }
            v.push_back(m);
            sort(v.begin(), v.end());
            ++insert;
        }
        cout << "Case #" << z << ": " << max(l, r) << ' ' << min(l, r) << endl;
        // for(const auto& item: v)
            // cout << item << ' ';
        // cout << endl;
    }
}
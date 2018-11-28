#include <bits/stdc++.h>
#define ll long long
using namespace std;

int test;

ll n, nums3;

pair<ll, ll> result;
map<ll, ll> maps1;

int main() {
    
    cin >> test;
    for(int tt=0;tt < test ;tt++) {
        cout<<"Case #"<<tt+1<< ": ";
        
        cin >> n >> nums3;
        
        nums3--;
        maps1.clear();
        maps1[-n] = 1;
        result = {-1, -1};
        
        while (true) {
            pair<ll, ll> currents = *maps1.begin();
            
            ll val = -currents.first;
            ll cnt = currents.second;
            
            maps1.erase(currents.first);
            
            ll nums1 = (val - 1) / 2;
            ll nums2 = val / 2;
            
            nums3 -= cnt;
            
            if (nums3 < 0) {
                result = {nums1, nums2};
                break;
            }
            
            if (nums1 > 0) {
                maps1[-nums1] += cnt;
            }
            if (nums2 > 0) {
                maps1[-nums2] += cnt;
            }
        }		        
        
        
        if (result.first < result.second) {
            swap(result.first, result.second);
        }
        
        cout << result.first << " "  << result.second << endl;        
    }
    
    return 0;
}

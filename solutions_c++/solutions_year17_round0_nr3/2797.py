#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <tuple>
typedef long long ll;

using namespace std;
ll t,n,k;



void ress(ll l){
    if(l%2==0){
        cout << l/2 << " " << (l-2)/2 << "\n";
    }else{
        cout << (l-1)/2 << " " << (l-1)/2 << "\n";
    }
    return;
}

void solve(int cas){
    cin >> n >> k;
    vector<pair<ll,ll> > nums, nums2;
    cout << "Case #" << cas << ": ";
    nums.push_back(make_pair(n,1));
    while(true){
        map<ll, int> findpos;
//        cout << "new: " << k << "\n";
//        for(auto u: nums){
//            cout << u.first << " " << u.second << "\n";
//        }
        for(auto u: nums){
            if(u.second<k){
                k-=u.second;
                if(u.first%2==1){
                    if(u.first>1){
                        ll nn = (u.first-1)/2;
                        if(findpos.count(nn) <= 0){
                            findpos[nn] = nums2.size();
                            nums2.push_back(make_pair( nn, u.second*2));
                        }else{
                            nums2[findpos[nn]].second += u.second*2;
                        }
                    }
                }else{
                    ll n1 = (u.first-2)/2, n2 = (u.first)/2;
                    if(findpos.count(n2) <= 0){
                        findpos[n2] = nums2.size();
                        nums2.push_back(make_pair( n2, u.second));
                    }else{
                        nums2[findpos[n2]].second += u.second;
                    }
                    if(u.first>2){
                        if(findpos.count(n1) <= 0){
                            findpos[n1] = nums2.size();
                            nums2.push_back(make_pair(n1, u.second));
                        }else{
                            nums2[findpos[n1]].second += u.second;
                        }
                    }
                }
            }else{
                ress(u.first);
                return;
            }
        }
        nums.clear();
        swap(nums,nums2);
    }

}

int main()
{
    ios::sync_with_stdio(false);
    cin >> t;
    for(int i=0; i<t; i++){
        solve(i+1);
    }
    return 0;
}

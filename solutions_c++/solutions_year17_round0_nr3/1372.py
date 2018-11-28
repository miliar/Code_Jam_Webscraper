//chiragjn
#include <iostream>
#include <vector>
#include <sstream>
#include <limits>
#include <map>
#include <functional>
#define ll long long
#define ff first
#define ss second
#define pb push_back
#define mpr make_pair
#define gibe_de_fast_io_b0ss ios::sync_with_stdio(0);cin.tie(0);cout.tie(0)
using namespace std;
const ll mod = 1e9 + 7;
const ll INF = 0x7FFFFFFFFFFFFFFF/2;
vector<int> arr,arr2;
int main(){
    gibe_de_fast_io_b0ss;
    int t,k;
    cin>>t;
    for(int T=1;T<=t;T++){
    	map<ll, ll, std::greater<ll>> mp;
        ll curr = 0;
        pair<ll,ll> ans = mpr(0,0);
        ll n,k;
        cin>>n>>k;
        mp[n]++;
        while(curr < k){
            auto it = mp.begin();
            ll a = it -> first,b = it -> second;
            if(a==0){
                break;
            }
            if(a%2==0){
                mp[a/2] += mp[a];
                mp[a/2 - 1] += mp[a];
                ans.ff = a/2;
                ans.ss = a/2 - 1;
                curr += mp[a];
            }
            else{
                mp[a/2] += mp[a];
                mp[a/2] += mp[a];
                ans.ff = a/2;
                ans.ss = a/2;
                curr += mp[a];
            }
            mp.erase(it);
        }

		cout<<"Case #"<<T<<": "<<ans.ff<<" "<<ans.ss<<"\n";
    }
    return 0;
}
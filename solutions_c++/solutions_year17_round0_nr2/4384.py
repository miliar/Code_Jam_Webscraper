#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

vector<ll> ans;

int main(){
    freopen("in2.txt","r",stdin);
    freopen("out.txt","w",stdout);
    ll t;
    cin >> t;
    for(ll k = 1;k <= t;k++){
        ll n;
        cin >> n;
        while(n){
            ans.push_back(n%10);
            n /= 10;
        }
        reverse(ans.begin(),ans.end());
        for(ll i = ans.size() - 1;i >= 1;i--){
            if(ans[i] < ans[i - 1]){
                for(ll j = i;j< ans.size();j++)
                    ans[j] = 9;
                ans[i - 1]--;
            }
        }
        ll i = 0;
        cout << "Case #" << k << ": ";
        while(i < ans.size() && ans[i] == 0)
            i++;
        for(;i < ans.size();i++)
            cout << ans[i];
        cout << "\n";
        ans.clear();
    }
}

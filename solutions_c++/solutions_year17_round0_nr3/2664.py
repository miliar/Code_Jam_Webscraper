#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main()
{
    int t;
    ll k, n;
    cin >> t;
    for(int cn=1;cn<=t;cn++){
        map<ll,ll,greater<ll>> mp;
        cin >> n >> k;
        mp[n] += 1;
        for(auto x : mp){
            if(x.second >= k){
                cout << "Case #" << cn << ": ";
                if(x.first%2 == 0){
                    cout << x.first/2 << ' '<< x.first/2 - 1 << '\n';
                }
                else{
                    cout << x.first/2 << ' ' << x.first/2 << '\n';
                }
                break;
            }
            else{
                k -= x.second;
                if(x.first %2 == 0){
                    if(x.first == 2){
                        mp[1]+= x.second;
                    }
                    else{
                        mp[x.first/2] += x.second;
                        mp[x.first/2-1] += x.second;
                    }
                }
                else{
                    mp[x.first/2] += (2LL*x.second);
                }
            }
        }
    }
    return 0;
}

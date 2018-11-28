#include<bits/stdc++.h>

using namespace std;
typedef long long ll;
int main(){
    int t,T;
    ll n,k,x,y,fr;
    cin>>T;
    for(t=1;t<=T;t++){
        cin>>n>>k;
        map<ll,ll>mp;
        mp[n]=1;
        while(1){
            n = mp.rbegin()->first;
            fr = mp.rbegin()->second;
            mp.erase(n);
            if(k>fr)k -= fr;
            else{
                if(n%2 == 1){
                    x=y=n/2;
                }else{
                    x = n/2;
                    y = max(0LL,x-1);
                }
                break;
            }
            if(n%2 == 1){
                mp[n/2] += 2*fr;
            }else{
                mp[n/2] += fr;
                mp[n/2 - 1] += fr;
            }
        }
        printf("Case #%d: %lld %lld\n",t,x,y);
    }
    return 0;
}

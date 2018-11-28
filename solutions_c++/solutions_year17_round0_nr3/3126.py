#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
map<ll,ll> mp;
void pjam(int tt){
    printf("Case #%d: ",tt);
}
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,itt;
    cin>>t;
    for(itt=1;itt<=t;itt++){
        mp.clear();
        ll n,k;
        cin>>n>>k;
        mp[n]=1;
        while(1){
            auto it =mp.end();
            it--;
           // cout<<it->first<<" ff "<<it->second<<endl;
            if(k<=it->second){
                pjam(itt);
                cout<<it->first/2<<" "<<it->first-(it->first/2)-1<<"\n";
                break;
            }
            else{
                k-=it->second;
                if(it->first&1){
                    mp[it->first/2]+=it->second*2;
                }
                else{
                    mp[it->first/2]+=it->second;
                    mp[it->first/2-1]+=it->second;
                }
            }
            mp.erase(it);
        }
    }
}

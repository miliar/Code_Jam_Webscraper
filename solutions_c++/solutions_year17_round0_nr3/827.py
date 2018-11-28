#include <bits/stdc++.h>

using namespace std;
#define pb push_back
#define mp make_pair
typedef long long int ll;


pair<ll,ll> getS(ll sa){
    ll ma = sa/2;
    ll mi;
    if(sa%2==0){
        mi = ma-1;
    }else{
        mi = ma;
    }
    mi = max((ll)0,mi);
    return mp(ma,mi);
}



int main(){
	int t;
    cin>>t;
    ll n,k;
    for(int i = 1;i<=t;i++){
        cout<<"Case #"<<i<<": ";
        cin>>n>>k;
        
        ll t = 0;
        map<ll,ll> ma1;
        map<ll,ll> ma2;
        pair<ll,ll> temp = getS(n);
        ma1[temp.first]++;
        ma1[temp.second]++;
        t++;
        if(t>=k){
            cout<<temp.first<<" "<<temp.second<<endl;
            continue;
        }
        bool fl = 1;            
        while(t<k){
            if(fl){
                fl = 0;
                ma2.clear();
                for(auto it = ma1.rbegin();it!=ma1.rend();it++){
                    
                    temp = getS(it->first);
                    //cout<<endl<<it->first<<" "<<it->second<<" "<<temp.first<<" "<<temp.second<<" "<<t<<endl;
                    t+=it->second;
                    if(t>=k){
                        cout<<temp.first<<" "<<temp.second<<endl;
                        break;
                    }
                    ma2[temp.first]+=it->second;
                    ma2[temp.second]+=it->second;
                }
            }else{
                fl = 1;
                ma1.clear();
                for(auto it = ma2.rbegin();it!=ma2.rend();it++){
                    temp = getS(it->first);
                    //cout<<endl<<it->first<<" "<<it->second<<" "<<temp.first<<" "<<temp.second<<" "<<t<<endl;
                    t+=it->second;
                    if(t>=k){
                        cout<<temp.first<<" "<<temp.second<<endl;
                        break;
                    }
                    ma1[temp.first]+=it->second;
                    ma1[temp.second]+=it->second;
                }
            }
        }
        
    }
    return 0;
}




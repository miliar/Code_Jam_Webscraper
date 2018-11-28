#include <bits/stdc++.h>
using namespace std ;
/*
An_Tea_Love.
Never_Give_Up.
*/
#define ft first
#define sd second
#define pb push_back
#define ll long long int
#define mp make_pair
#define loop(i, a, b) for(i=a; i<b; i++)
#define run	ios_base::sync_with_stdio(0)
const int mod = 1e9 + 7;
const ll INF = 1e17;
int main(){
    run;
    ll t,i,j,k,l,n,p=0;
    cin>>t;
    while(t--){
        p++;
        cin>>n;
        vector<ll>v;
        k=n;
        while(k>0){
            v.pb(k%10);
            k/=10;
        }
        reverse(v.begin(),v.end());
        k=1;
        while(1){
            ll flag=0;
            for(i=0;i<v.size()-1;i++){
                if(v[i]>v[i+1]){
                    flag=1;
                    break;
                }
            }
            if(flag==0){
                break;
            }
            for(i=v.size()-k;i>=1;i--){
                if(v[i]<v[i-1]){
                    l=i-1;
                    break;
                }
            }
            if(v[l]==0){
                v[l]=9;
                for(i=l-1;i>=0;i--){
                    if(v[i]==0){
                        v[i]=9;
                    }
                    else{
                        v[i]--;
                        break;
                    }
                }
                for(i=l+1;i<v.size();i++){
                    v[i]=9;
                }
            }
            else{
                v[l]--;
                for(i=l+1;i<v.size();i++){
                    v[i]=9;
                }
            }
        }
        l=-1;
        for(i=0;i<v.size();i++){
            if(v[i]>0){
                l=i;
                break;
            }
        }
        cout<<"Case #"<<p<<": ";
        for(i=l;i<v.size();i++){
            cout<<v[i];
        }
        cout<<endl;
    }
return 0;

}



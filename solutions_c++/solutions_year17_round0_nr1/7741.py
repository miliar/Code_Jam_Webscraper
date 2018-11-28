#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
    ios::sync_with_stdio(false);
    ll t,p=1;
    cin>>t;
    while(t--){
        string s;
        ll k,n;
        cin>>s>>k;
        n=s.length();
        ll q=0;
        for(ll i=0;i<n-k+1;i++){
            if(s[i]=='-'){
                q++;
                for(ll j=0;j<k;j++){
                    if(s[i+j]=='+')
                        s[i+j]='-';
                    else s[i+j]='+';
                }
            }
        }
        ll flag=0;
        for(ll i=0;i<n;i++){
            if(s[i]=='-'){
                flag=1;
                break;
            }
        }
        if(flag==1){
            cout<<"Case #"<<p<<": "<<"IMPOSSIBLE\n";
            p++;
        }else{
            cout<<"Case #"<<p<<": "<<q<<"\n";
            p++;
        }
    }
}

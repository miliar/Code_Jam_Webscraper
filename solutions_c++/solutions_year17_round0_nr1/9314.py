
#include <bits/stdc++.h>
# define ll long long int 
using namespace std;


int main() {
    ll t;
    cin>>t;
    ll  p;
    p=0;
    while(t--){
        string s;
        p++;
        cin>>s;
        ll k;
        cin>>k;
        ll sum;
        sum=0;
        ll i;
        for(i=0;i<(s.length()+1)-k;i++){
             
              if(s[i]=='-'){
                 
                   ll c=0;
                  sum++;
             while(c<k){
                
                 
                 if(s[c+i]=='+'){
                     s[c+i]='-';
                 }
                 else if(s[c+i]=='-'){
                     s[c+i]='+';
                 }
                      c++;
             }
        }
        }
            ll flag=0;
         for(i=0;i<s.length();i++){
             if(s[i]=='-'){
                 flag=1;
                
             }
         }
            if(flag){
             cout<<"Case #"<<p<<": impossible\n"  ;
            }
            else{
                cout<<"Case #"<<p<<": "<<sum<<"\n";
            }
        
        
    }
    return 0;
}

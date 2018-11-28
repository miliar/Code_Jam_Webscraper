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
    ll t,i,j,k,l,p=0;
    cin>>t;
    while(t--){
        p++;
        string s;
        cin>>s>>k;
        ll flag=0;
        ll ans=0;
        for(i=0;i<=s.length()-k;i++){
            if(s[i]=='-'){
                ans++;
                for(j=i;j<=i+k-1;j++){
                    if(s[j]=='-'){
                        s[j]='+';
                    }
                    else{
                        s[j]='-';
                    }
                }
            }
        }
        loop(i,0,s.length()){
            if(s[i]=='-'){
                flag=1;
                break;
            }
        }
        if(flag==1){
            cout<<"Case #"<<p<<": ";
            cout<<"IMPOSSIBLE"<<endl;
        }
        else{
            cout<<"Case #"<<p<<": ";
            cout<<ans<<endl;
        }
    }
return 0;

}




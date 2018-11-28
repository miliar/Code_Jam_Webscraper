#include <bits/stdc++.h>
using namespace std;

int main(){

      #ifndef ONLINE_JUDGE
     freopen("input.txt","r",stdin);
     freopen("output.txt","w",stdout);
   #endif

    int t,p=1;
    cin>>t;

    while(t--){
        string s; int k,ans = 0;
        cin>>s>>k;

        for(int i=0; i<=s.size()-k; i++){
            
            if(s[i] == '-'){
                for(int j=0; j<k; j++){
                    if(s[i+j] == '+')
                        s[i+j] = '-';
                    else
                        s[i+j] = '+';
                
                }
                //cout<<s<<endl;

                ans++;
            }

        }

        int fg = 0;

        cout<<"Case #"<<p++<<": ";

        for(int i=0; i<s.size(); i++)
            if(s[i] == '-')
                fg = 1;

        if(fg)
           cout<<"IMPOSSIBLE"<<endl;
        else
           cout<<ans<<endl;
    }

}
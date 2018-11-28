#include<bits/stdc++.h>
using namespace std;

int main(){
    freopen("Alarge.txt", "r", stdin);
    freopen("Alarge_out.txt", "w", stdout);
    int T;
    cin>>T;
    for(int t=1 ; t<=T ; ++t){
        string s;
        int k, ans=0;
        cin>>s>>k;
        for(int i=0 ; i<=s.size()-k ; ++i){
            if(s[i] == '-'){
                ans++;
                for(int j=0 ; j<k ; ++j){
                    if(s[i+j] == '-')
                        s[i+j] = '+';
                    else
                        s[i+j] = '-';
                }
            }
        }
        bool done = true;
        for(int i=0 ; i<s.size() ; ++i)
            if(s[i] == '-')
                done = false;
        cout<<"Case #"<<t<<": ";
        if(done)
            cout<<ans<<endl;
        else
            cout<<"IMPOSSIBLE"<<endl;
    }
}

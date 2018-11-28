#include <bits/stdc++.h>
using namespace std;
int main(){
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int k,t,x;
    bool mini;
    cin>>t;
    for(int i=1;i<=t;++i){
        x=0;mini=false;
        string s;
        cin>>s>>k;
        for(int i=0;i<=s.size()-k;++i){
            if(s[i]=='-'){
                x++;
                for(int j=i;j<i+k;++j){
                    if(s[j]=='+'){s[j]='-';}
                    else{s[j]='+';}
                }
            }
        }
        for(int i=0;i<s.size();++i){
            if(s[i]=='-'){
                mini=true;
                break;
            }
        }
        if(mini) cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
        else cout<<"Case #"<<i<<": "<<x<<endl;
    }
    return 0;
}

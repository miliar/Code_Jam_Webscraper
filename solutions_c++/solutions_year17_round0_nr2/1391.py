#include<bits/stdc++.h>
using namespace std;
string order(string  s){
    int n = s.size(),ok=0;
    while(!ok){
            ok=1;
        for(int i=1;i<n;i++){
            if(s[n-i]<s[n-i-1]){
                    ok=0;
                s[n-i-1]--;
                for(int k=n-i;k<n;k++)
                s[k]='9';

            }
        }
    }
    for(int i  = 0;i<s.size()&&s[i]=='0';i++)s.erase(s.begin());
    return s;


}
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int tc;cin>>tc;
    for(int t=1;t<=tc;t++){
        string in;cin>>in;
        cout<<"Case #"<<t<<": "<<order(in)<<endl;
    }
}

#include<bits/stdc++.h>
using namespace std;
int tc,k,f;
string s;
bool checa() {
    bool flag=true;
    for(int i=0;i<s.size();i++)
        if(s[i]=='-')
            return false;
    return true;

}
int main(){
    freopen("in.in","r",stdin);
    freopen("o.out","w",stdout);
    cin>>tc;
    int ans=0;
    int t=1;
    while(tc--) {
        ans=0;
        cin>>s>>k;
        for(int i=0,j=s.size()-1;i<s.size()-1;i++,j--){
            if(checa())
                break;
            if(s[i]=='-') {
                if(i+k<=s.size()){
                    for(int u=i;u<i+k;u++){
                        if(s[u]=='-')
                            s[u]='+';
                        else
                            s[u]='-';
                    }
                    ans++;
                }
            }
             if(checa())
                break;
            if(s[j]=='-'){
                if(j-k>=0){
                    for(int u=j;u>j-k;u--){
                        if(s[u]=='-')
                            s[u]='+';
                        else
                            s[u]='-';
                    }
                    ans++;
                }
            }
        }
        if(checa())
           cout<<"Case #"<<t<<": "<<ans<<endl;
        else
            cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
        t++;
    }
}

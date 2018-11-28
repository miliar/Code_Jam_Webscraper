#include<bits/stdc++.h>
using namespace std;
string s;
int main(){
    ios_base::sync_with_stdio(0);
    int ans,i,j,k,l,tc,cc=0;
    cin>>tc;
    while(cc<tc){
        cin>>s>>k;
        ans=0;
        l=s.length();
        for(i=0;i<l;++i)if(s[i]=='-'){
            //cout<<s<<'\n';
            if(i+k>l){
                ans=-1;
                break;
            }
            for(j=0;j<k;++j){
                if(s[i+j]=='+')s[i+j]='-';
                else s[i+j]='+';
            }
            ++ans;
        }
        cout<<"Case #"<<++cc<<": ";
        if(ans!=-1)cout<<ans<<'\n';
        else cout<<"IMPOSSIBLE\n";
    }
    return 0;
}

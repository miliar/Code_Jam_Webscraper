#include<bits/stdc++.h>

using namespace std;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("output4.out","w",stdout);
    int t;
    cin>>t;

    for(int i=1; i<=t; ++i){
        int flag=0;
        string s;
        int k;
        int ans=0;
        cin>>s;
        //cout<<s<<endl;

        cin>>k;
        cout<<"Case #"<<i<<": ";

        for(int j=0; j<s.length()-k; j++){
            if (s[j]=='-'){
                ans++;
                for(int p=j; p<j+k; p++ ){
                    if(s[p]=='-')
                        s[p]='+';
                    else
                        s[p]='-';
                }
            }
        }
       // cout<<s<<endl;

        for(int l=s.length()-k; l<s.length()-1; l++){
            if(s[l]!=s[l+1]){
                flag=1;
                cout<<"IMPOSSIBLE"<<'\n';
                break;
            }
        }
        if((!flag) && s[s.length()-k]=='-')
            ans++;

        if(!flag)
            cout<<ans<<'\n';
    }
return 0;
}

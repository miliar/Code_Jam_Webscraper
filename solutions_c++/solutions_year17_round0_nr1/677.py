#include<bits/stdc++.h>
using namespace std;
int main(){
    int a,b,c,d,e,f,g,h,k,t;
    ios::sync_with_stdio(0);
    //freopen("A-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    cin>>t;
    for(int ii=1;ii<=t;ii++){
        string s;
        cin>>s>>k;
        int g=0;
        for(int i=0;i+k<=s.size();i++){
            if(s[i]=='-'){
                g++;
                for(int j=0;j<k;j++){
                    if(s[i+j]=='-')s[i+j]='+';
                    else s[i+j]='-';
                }
            }
        }
        h=1;
        for(int i=1;i<=k;i++){
            if(s[s.size()-i]!='+'){
                h=0;break;
            }
        }
        cout<<"Case #"<<ii<<": ";
        if(h)cout<<g<<endl;
        else cout<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}

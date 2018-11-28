#include <bits/stdc++.h>
using namespace std;
const int MAXN=3000;
int main(){
    int t,c,st,ans,k,v[MAXN],md[MAXN];
    string s;
    cin>>t;
    for(int T=1;T<=t;T++){
        ans=0;
        cin>>s>>k;
        for(int i=0;i<MAXN;i++)md[i]=0;
        st=0;
        for(int i=0;i<s.size();i++){
            c=(s[i]=='+'?0:1);
            c=(c+st)%2;
            if(c==1){
                ans++;
                st++;
                c=0;
                md[i+k-1]--;
            }
            st=st+md[i];
        }
        cout<<"Case #"<<T<<": ";
        if(st==0)cout<<ans<<endl;
        else cout<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}

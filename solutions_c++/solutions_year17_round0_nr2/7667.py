// ༼∩ຈل͜ຈ༽つ━☆ﾟ.*･｡ﾟ .·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º> - code by: kdkdk
#include <bits/stdc++.h>
#define q reverse(n.begin(),n.end());
using namespace std;int main(){
    int t,c=1;cin>>t;for(;c<=t;++c){string n;cin>>n;q
        for(int i=1;i<n.size();++i)for(int j=i;j-->0&&n[j]<n[j+1]&&(n[j]='9');)n[i]=(j+1==i?'0'+(n[i]+11)%10:n[i]);for(;n.size()>1&&n.back()=='0';)n.pop_back();q
cout<<"Case #"<<c<<": "<<n<<'\n';}}

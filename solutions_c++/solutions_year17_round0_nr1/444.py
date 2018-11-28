#include<bits/stdc++.h>
using namespace std;
void solve(int iii)
{
    int ans=0,k;
    string s;
    cout<<"CASE #"<<iii<<": ";
    cin>>s>>k;
    for(int i=0;i+k-1<s.size();i++){
        if(s[i]=='-'){
            for(int j=i;j<=i+k-1;j++) s[j]=(s[j]=='-')?'+':'-';
            ans++;
        }
    }
    for(int i=0;i<s.size();i++) if(s[i]=='-') {cout<<"IMPOSSIBLE\n"; return;}
    cout<<ans<<'\n';
}
int main()
{
    int t;
    freopen("test.inp","r",stdin);
    freopen("test.out","w",stdout);
    cin>>t;
    for(int i=1;i<=t;i++) solve(i);
}

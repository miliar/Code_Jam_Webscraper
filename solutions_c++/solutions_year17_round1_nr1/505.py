#include<bits/stdc++.h>
using namespace std;
string s[200];
void solve()
{
    int n,m;
    cin>>n>>m;
    for(int i=0;i<n;i++) cin>>s[i];
    for(int i=0;i<n;i++){
        for(int j=1;j<s[i].size();j++){
            if(s[i][j]=='?') s[i][j]=s[i][j-1];
        }
        reverse(s[i].begin(),s[i].end());
        for(int j=1;j<s[i].size();j++){
            if(s[i][j]=='?') s[i][j]=s[i][j-1];
        }
        reverse(s[i].begin(),s[i].end());
        if(i>0)
        for(int j=0;j<s[i].size();j++){
            if(s[i][j]=='?') s[i][j]=s[i-1][j];
        }
    }
    for(int i=n-1;i>=0;i--){
        for(int j=0;j<s[i].size();j++){
            if(s[i][j]=='?') s[i][j]=s[i+1][j];
        }
    }
    for(int i=0;i<n;i++){
        cout<<s[i]<<'\n';
    }
}
int main()
{
    int t;
    ios_base::sync_with_stdio(false);
    freopen("test.inp","r",stdin);
    freopen("test.out","w",stdout);
    cin>>t;
    for(int i=1;i<=t;i++){
        cout<<"CASE #"<<i<<":"<<'\n';
        solve();
    }
}

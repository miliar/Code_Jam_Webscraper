#include<bits/stdc++.h>
using namespace std;
void solve(int iii)
{
    string s;
    long long int ans=0;
    cin>>s;
    for(int i=(int)s.size()-1;i>=0;i--){
        if(s[i]=='0') continue;
        long long int first=s[i]-'1',cur=(s[i]-'0');
        for(int j=(int)s.size()-1;j>i;j--) first=first*10+9,cur=cur*10;
        if(cur>10*ans && i+1!=s.size()) ans=first;
        else ans=cur+ans;
        //cout<<ans<<" "<<cur<<'\n';
    }
    cout<<"CASE #"<<iii<<": "<<ans<<'\n';
}
int main()
{
    int t;
    freopen("test.inp","r",stdin);
    freopen("test.out","w",stdout);
    cin>>t;
    for(int i=1;i<=t;i++) solve(i);
}

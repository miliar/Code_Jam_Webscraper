#include<iostream>
using namespace std;
void solve()
{
    string s;
    cin>>s;
    int n=s.size(),i;
    for(i=1;i<n;i++)
        if(s[i]<s[i-1])break;
    if(i==n)
    {
        cout<<s<<'\n';
        return;
    }
    for(i=i-1;i>0;i--)
        if(s[i]-1>=s[i-1])break;
    if(i==0 && s[0]=='1')
    {
        for(;i<n-1;i++)
            cout<<9;
        cout<<'\n';
        return;
    }
    s[i]--;
    for(i=i+1;i<n;i++)
        s[i]='9';
    cout<<s<<'\n';
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t,i;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        solve();
    }
}

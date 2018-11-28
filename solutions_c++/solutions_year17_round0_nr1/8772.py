#include<iostream>
using namespace std;
void solve()
{
    string s;
    int k,n,i,j,o=0;
    cin>>s>>k;
    n=s.size();
    for(i=0;i<=n-k;i++)
    {
        if(s[i]=='-')
        {
            o++;
            for(j=i;j<i+k;j++)
            {
                if(s[j]=='-')s[j]='+';
                else if(s[j]=='+')s[j]='-';
            }
        }
    }
    for(;i<n;i++)
        if(s[i]=='-')
        {
            cout<<"IMPOSSIBLE\n";
            return;
        }
    cout<<o<<'\n';
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

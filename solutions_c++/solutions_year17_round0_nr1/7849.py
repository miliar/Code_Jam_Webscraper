#include<bits/stdc++.h>
using namespace std;
bool done(string s,int n)
{
    //for(int i=0;i<n;i++)cout<<s[i];
    //cout<<endl;
    for(int i=0;i<n;i++)
        if(s[i]=='-')return false;
    return true;
}
int res(string s,int n,int k,int i,int c)
{
    if(done(s,n))return c;
    if(i+k>n)return INT_MAX;
    if(s[i]=='-')
    {
        int j=i+k;
        for(int k=i;k<j;k++)
        if(s[k]=='+')s[k]='-';
        else s[k]='+';

        c++;
    }
    return res(s,n,k,i+1,c);
}
int main()
{
    int t;cin>>t;
    for(int i=1;i<=t;i++)
    {
        string s;
        cin>>s;
        int n,k;
        cin>>k;
        n=s.size();
        int ans=res(s,n,k,0,0);
        cout<<"Case #"<<i<<": ";
        ans==INT_MAX ?cout<<"IMPOSSIBLE":cout<<ans;
        cout<<endl;
    }
}

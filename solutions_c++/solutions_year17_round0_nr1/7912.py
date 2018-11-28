#include <iostream>
#include <vector>
using namespace std;
int Sol(string s,int t)
{
    int ans=0;
    string s2="";
    for(int i=0;i<s.size(); i++) s2=s2+"+";

    for(int i=0; i<=s.size()-t; i++)
    {
        if(s[i]!=s2[i])
        {
            for(int j=i; j<i+t; j++) 
                s2[j]=s2[j]=='+'?'-':'+';
            ans++;
        }
    }
    return s==s2?ans:-1;
}   
int main()
{
    int n,t,ans;
    string s;
    cin>>n;
    for(int i=1; i<=n; i++)
    {
        cin>>s>>t;
        ans=Sol(s,t);
        if(ans!=-1)
            cout<<"Case #"<<i<<": "<<ans<<endl;        
        else
            cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;        

    }
    return 0;
}
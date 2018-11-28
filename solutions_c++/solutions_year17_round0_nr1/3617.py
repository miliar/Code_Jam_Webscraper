#include<bits/stdc++.h>
using namespace std;
int k,t;
long long ans;
string s;
void flip(int loc)
{
    for(int i=loc;i<loc+k;i++)
        s[i]=(s[i]=='-')?'+':'-';
}
bool check()
{
    for(int i=0;i<s.size();i++)
        if(s[i]=='-') return false;
    return true;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    for(int tc=1;tc<=t;tc++)
    {
        cin>>s>>k;
        ans=0;
        for(int i=0;i<=s.size()-k;i++)
        {
            if(s[i]=='-')
            {
                ans++;
                flip(i);
            }
        }
        cout<<"Case #"<<tc<<": ";
        if(check())
            cout<<ans<<endl;
        else
            cout<<"IMPOSSIBLE"<<endl;
    }
}
#include <iostream>
#include <string>
using namespace std;

int main()
{

int t,n,i,j,ans,l,k;
string s;
cin>>t;
for(i=1;i<=t;i++)
{
    cin>>s>>k;
    ans=0;
     l=s.length();
    for(j=0;j<l-k+1;j++)
    {
        if(s[j]=='-')
        {
            for(n=0;n<k;n++)
            {
                if(s[j+n]=='-')s[j+n]='+';
                else s[j+n]='-';
            }
            ans++;
        }
    }
    for(n=j;n<l;n++)
        if(s[n]=='-')ans=-1;
    if(ans>-1)cout<<"Case #"<<i<<": "<<ans<<endl;
    else cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
}
return 0;
}

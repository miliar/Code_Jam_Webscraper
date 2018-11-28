#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("largens.txt","w",stdout);
int t;
string s;
int k,ans;

cin>>t;
for(int tc=1;tc<=t;++tc)
{
    ans=0;
    cin>>s>>k;
    for(int i=0;i+k-1<s.length();++i)
    {
        if(s[i]=='-')
        {for(int j=i;j<=i+k-1;++j)
        {
          if(s[j]=='-')s[j]='+';
          else s[j]='-';
        }
        ++ans;
        }
    }
    int f=1;
    cout<<"Case #"<<tc<<": ";
    for(int i=0;i<s.length();++i)if(s[i]=='-')f=0;
    if(!f)cout<<"IMPOSSIBLE\n";
    else cout<<ans<<endl;
}
return 0;
}

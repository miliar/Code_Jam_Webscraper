#include <bits/stdc++.h>
using namespace std;
int main()
{
  int p,t,l,g=0,k,i=0,j,f=0,ans=0;
  string s;
  cin>>t;
  for(p=1;p<=t;p++)
  {
    f=i=ans=0;
    cin>>s>>k;
    while(i<s.size()-k+1)
    {
      if(s[i]=='-')
      {
        for(j=0;j<k;j++)
          if(s[i+j]=='+')
            s[i+j]='-';
          else
            s[i+j]='+';
          ans++;
          i++;
      }
      else
        i++;
      //cout<<s<<endl<<i<<endl;;
    }
    f=0;
    for(l=0;l<s.size();l++)
      if(s[l]=='-')
        {
          f=1;
          break;
        }
    if(f)
      cout<<"Case #"<<p<<": "<<"IMPOSSIBLE\n";
    else
      cout<<"Case #"<<p<<": "<<ans<<endl;
  }
  return 0;
}

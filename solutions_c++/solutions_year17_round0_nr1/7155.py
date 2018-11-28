#include<bits/stdc++.h>
using namespace std;
int main()
{
  int t,n,k,flag,c;string s;ofstream fp;
  fp.open("out.txt",ios::app);
  cin>>t;
  for(int p=1;p<=t;p++)
  {
     cin>>s>>k;
     n=s.size();
     c=0;
     for(int i=0;i<=n-k;i++)
      {
         if(s[i]=='+')
          continue;
          else
          {
             c++;
             for(int j=i;j<i+k;j++)
              {
                 if(s[j]=='+')
                  s[j]='-';
                  else
                   s[j]='+';
              }
          }
      }flag=0;
      for(int i=n-k+1;i<n;i++)
      {
        if(s[i]=='-')
        {flag=1;break;}
      }
      if(flag==1)
      fp<<"Case #"<<p<<": IMPOSSIBLE"<<endl;
      else
       fp<<"Case #"<<p<<": "<<c<<endl;
  }
}

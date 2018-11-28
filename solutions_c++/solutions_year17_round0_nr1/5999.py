#include <bits/stdc++.h>

#define Saiyan

using namespace std;

int main()
{
    #ifdef Saiyan
  freopen("inp.txt","r",stdin) ;
  freopen("out.txt","w",stdout) ;
  #endif

int t,k,c,n,i,j,ans=0,z;
string s;
  cin>>t;

  for(z=1;z<=t;z++)
  {ans=0;
      cin>>s;
      cin>>k;
      n=s.length();
      for(i=0;i<n-k+1;i++)
      {
          if(s[i]=='-')
          {ans++;
              for(j=i;j<k+i;j++)
              {
                  if(s[j]=='+')
                  {
                      s[j]='-';
                  }
                  else
                  {
                      s[j]='+';
                  }
              }
          }
      }
      c=0;
      for(i=0;i<n;i++)
      {
          if(s[i]=='+')
          {
              c++;
          }
      }
      //cout<<c;

      if(c==n)
      {
          cout<<"Case #"<<z<<": "<<ans<<endl;
      }
      else
      {
          cout<<"Case #"<<z<<": "<<"IMPOSSIBLE"<<endl;
      }

//cout<<s<<endl;
  }

	return 0;
}

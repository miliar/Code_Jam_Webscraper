#include<bits/stdc++.h>
using namespace std;
int main()
{ios::sync_with_stdio(0);
freopen("1.txt","r",stdin);
freopen("2.txt","w",stdout);
int t,i,j,k,l,len,cnt,ii;
bool flag;

string s;
cin>>t;
  for(ii=1;ii<=t;ii++)
  {cnt=0;
      cin>>s>>k;
       len=s.length();
       for(i=0;i<=len-k;i++)
          {
              if(s[i]=='-')
              {cnt++;
                  for(j=0;j<k;j++)
                  {
                      if(s[i+j]=='-')
                      {
                          s[i+j]='+';
                      }
                      else
                        s[i+j]='-';
                  }
              }

          }
          flag=0;

          for(i=len-k+1;i<len;i++)
          {
              if(s[i]=='-')
                 flag=1;
          }
          if(flag==1)
          {
              cout<<"Case #"<<ii<<": IMPOSSIBLE"<<endl;
          }
          else
          cout<<"Case #"<<ii<<": "<<cnt<<endl;

  }

return 0;
}

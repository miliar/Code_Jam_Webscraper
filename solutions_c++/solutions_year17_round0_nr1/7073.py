#include "bits/stdc++.h"
using namespace std;
int main()
{
  int T;
  cin>>T;
  string s;
  int k;
  for(int t=1;t<=T;t++)
  {
    cin>>s>>k;
    int op=0;
    for(int i=0;i<s.size();i++)
    {
      if(s[i]=='-')
      {
        op++;
        if(i+k-1>=s.size())
        {
          op=-1;
          break;
        }
        else
        {
          for(int j=i;j<i+k;j++)
          {
            if(s[j]=='-')s[j]='+';
            else s[j]='-';
          }
        }
      }
    }
    cout<<"Case #"<<t<<": ";
    if(op==-1)
      cout<<"IMPOSSIBLE\n";
    else
      cout<<op<<endl;
  }
}

#include<bits/stdc++.h>
using namespace std ;

 string s;
  int t,x;
int main()
{
//   freopen("B-large.in","r",stdin);
//   freopen("B-large-output.txt","w",stdout);

    cin>>t;

        for(int o=1;o<=t;o++)
    {
        cin>>s;
        x=s.size();
         int h=1;
    while(h)
    {
        h=0;
        for(int i=1;i<x;i++)
        {
            if(s[i]<s[i-1])
            {
                h=1;
                for(int j=i;j<x;j++)
      {
          s[j]='9';
      }
      i--;
      while((s[i]=='0' || s[i]=='1') && i!=0)
      {
          s[i]='9';
          i--;
      }
      s[i]--;
      break;
            }
        }
    }
        if(x>1 && s[0]=='0')s.erase(s.begin());
        cout<<"Case #"<<o<<": ";
        cout<<s<<endl;
    }
}

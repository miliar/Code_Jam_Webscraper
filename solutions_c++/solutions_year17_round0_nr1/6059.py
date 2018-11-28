#include<bits/stdc++.h>
using namespace std;

int main()
{
   freopen("A-large.in","r",stdin);
   freopen("al_out.in","w",stdout);
   int tst,k,ans;
   string str;
   cin >> tst;
   for(int tstno=1;tstno<=tst;tstno++)
   {
      cin >> str >>k;
      ans=0;
      for(int i=0;i<str.length();i++)
      {
         if(str[i]=='-')
         {
             if(i+k>str.length())
                ans=-1;
             else{
             ans++;
             for(int j=i;j<i+k;j++)
             {
                 if(str[j]=='+')
                    str[j]='-';
                 else
                    str[j]='+';

             }}
         }
      }
      if(ans==-1)
         cout<<"Case #"<<tstno<<": IMPOSSIBLE\n";
      else
         cout<<"Case #"<<tstno<<": "<<ans<<"\n";
   }
}

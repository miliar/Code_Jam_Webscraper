#include<bits/stdc++.h>
using namespace std;

int main()
{

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int t;

    cin >> t;

    int j=1;

    while(j<=t)
    {
      string s;
      int k,ans=0,flag=1;

      cin >> s >> k;

      for(int i = 0 ; i <= s.size()-k ; i++)
      {

         if(s[i]=='-')
         {
             for(int it=i ; it<k+i;it++)
             {
                 if(s[it]=='-')
                 {
                     s[it]='+';
                 }
                 else
                    s[it]='-';
             }
             ans++;
         }
      }
      for(int i = 0 ; i < s.size() ; i++)
      {

          if(s[i]=='-')
          {
              flag=0;
               break;
          }
      }
      if(flag)
      cout<<"Case #"<<j<<": "<<ans<<"\n";
    else
        cout<<"Case #"<<j<<": "<<"IMPOSSIBLE\n";
        j++;

    }
    return 0;
}

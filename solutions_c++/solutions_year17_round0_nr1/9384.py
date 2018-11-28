#include<bits/stdc++.h>
using namespace std;
#include<algorithm>
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.in","w",stdout);
    std::ios_base::sync_with_stdio(false);
   int t,k,count,flag=0,i,l,j,m;
   string s;
   cin>>t;
   for(i=1;i<=t;i++)
   {
       count=0;
       flag=0;
      cin>>s>>k;
      l=s.length();
      for(j=0;j<=l-k;j++)
      {
          if(s[j]=='+')
            continue;
          else
            {
                for(m=j;m<j+k;m++)
                {
              if(s[m]=='-')
                s[m]='+';
                else
                    s[m]='-';
                }
                count++;
            }
      }
      for(j=l-k;j<l;j++)
      {
          if(s[j]=='-')
            flag=1;
      }
      if(flag==1)
        cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
      else
        cout<<"Case #"<<i<<": "<<count<<endl;
   }

 return 0;
}

#include<bits/stdc++.h>
#define ll long long int
using namespace std;
int main()
{ios::sync_with_stdio(0);
freopen("1.txt","r",stdin);
freopen("2.txt","w",stdout);
 ll t,i,j,k,len,temp;
 string s,ans,aans;
 cin>>t;
  for(i=1;i<=t;i++)
      {ans="";
      aans="";
      cin>>s;
      ans=s;
   //   cout<<ans<<endl;
      len=s.length();
         for(j=0;j<len-1;j++)
         {//cout<<"1 "<<endl;
              temp=s[j];
             if(s[j]>s[j+1])
             {
                 while(j>=0 &&temp==s[j])
                 {
                     j--;
                 }
                 j++;
                 ans[j]=ans[j]-1;
                 j++;
                 while(j<len)
                 {
                     ans[j]='9';
                     j++;
                 }
     //            cout<<ans<<endl;
       //          cout<<" hugh "<<endl;
             }
         }if(ans[0]=='0')
            {//cout<<ans<<endl;
             aans="";
                for(k=1;k<len;k++)
                {
                    aans=aans+ans[k];
                }
                ans=aans;

               // cout<<ans<<endl;
            }
         cout<<"Case #"<<i<<": ";
         cout<<ans<<endl;
      }

return 0;
}

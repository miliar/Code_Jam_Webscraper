// Ashwani NSIT
//codejam 2017 qualification round - A
#include <bits/stdc++.h>

using namespace std;

#define ll long int
#define mod 1000000007


int main()
{
freopen("A-large.in","r",stdin);
freopen("ansa.out","w",stdout);
string str;
ll t,flag,ans,i,j,k,t1=0,len;
cin>>t;
while(t--)
{t1++;
cin>>str>>k;
len=str.length();
ans=flag=0;
for(i=len-1;i>=k-1;i--)
 {
  if(str[i]=='-')
   {
    for(j=i;j>(i-k);j--)
     {
      if(str[j]=='+')
       {
        str[j]='-';
       }
       else
        {
        str[j]='+';
        }
     }
     ans++;
   }
 }
 for(i=0;i<len;i++)
  {
     if(str[i]=='-')
      {
        flag=1;
        break;
      }
  }
  cout<<"Case #"<<t1<<": ";
 if(flag==0)
  {
   cout<<ans<<endl;
  }
  else
   {
   cout<<"IMPOSSIBLE"<<endl;
   }
}
    return 0;
}

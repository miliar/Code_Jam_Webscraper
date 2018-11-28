#include<bits/stdc++.h>
#include<iostream>
using namespace std;
int main()
{

  int y,t;
  cin>>t;
  for(y=0;y<t;y++)
  {
    string s;
    int k,l,ans=0,i,j,flag=0;
    cin>>s;
    cin>>k;
    l=s.size();
    for(i=0;i<=l-k;i++)
    {
       if(s[i]=='-')
       {
           ans++;
          for(j=i;j<i+k;j++)
          {
            if(s[j]=='-')
                s[j]='+';
            else
                s[j]='-';
          }
          //cout<<s<<endl;
       }
    }
    for(i=l-k+1;i<l;i++)
    {
       if(s[i]=='-')
       {
           cout<<"CASE #"<<y+1<<": IMPOSSIBLE"<<endl;
           flag=1;
           break;
       }
    }
    if(flag!=1)
    {
      cout<<"CASE #"<<y+1<<": "<<ans<<endl;
    }

   }
   return 0;
}

#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
freopen("o.out","w",stdout);
int foo,i,j;
string str;
int f,ctr=0,t,l=1;
cin>>t;
while(t--)
{f=0,ctr=0;
cin>>str>>foo;
for(i=str.length()-1;i>=foo-1;i--)
 {
  if(str[i]=='-')
   {
    for(j=i;j>(i-foo);j--)
     {
      if(str[j]=='-')
       {
        str[j]='+';
       }
       else
        {
        str[j]='-';
        }
     }
     ctr++;
   }
 }
 for(i=0;i<str.length();i++)
  {
     if(str[i]=='-')
      {
        f=1;
        break;
      }
  }
  cout<<"Case #"<<l<<": ";
 if(f==1)
  {
  cout<<"IMPOSSIBLE";
  }
  else
   {
   cout<<ctr;
   }
   cout<<endl;
   l++;
}
    return 0;
}

//Ashwani NSIT
//codejam 2017 qualification round - B
#include <bits/stdc++.h>

using namespace std;

#define ll long int
#define mod 1000000007

int main()
{
 freopen("B-large.in","r",stdin);
 freopen("ansb.out","w",stdout);
string str;
ll t,t1=0,i,j,a,b,flag,check,index,len;
cin>>t;
while(t--)
{t1++;
 cout<<"Case #"<<t1<<": ";
flag=check=index=0;
cin>>str;
len=str.length();
for(i=0;i<len-1;i++)
 {
  if(str[i+1]<str[i])
   {
     check=1;
     break;
   }
 }
 if(check==1)
 {
for(i=0;i<len-1&&flag!=1;i++)
 {
  if(str[i]>str[i+1])
   {flag=1;
    for(j=i;j>0;j--)
     {
     if(str[j]!=str[j-1])
      {index=j;
        break;
      }
     }
   }
   if(flag==1)
    {
    a=str[index]-'0';
    a--;
    str[index]=a+'0';
    }
 }
for(i=index+1;i<len;i++)
 {
 str[i]='9';
 }
 for(i=0;i<len;i++)
  {
     if(str[i]!='0')
      {
         cout<<str[i];
      }
  }
  cout<<endl;
 }
 else
  {

    cout<<str<<endl;
  }
}
    return 0;
}

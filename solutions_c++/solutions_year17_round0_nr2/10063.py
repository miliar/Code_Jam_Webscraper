#include <bits/stdc++.h>

using namespace std;


int main()
{
 freopen("B-small-attempt1.in","r",stdin);
freopen("out.out","w",stdout);
string str;
int t,g=1;
cin>>t;
while(t--)
{
cin>>str;
char ch;
int l=str.length(),pos=0,num1,num2,i,j,f=0,f1=0;
for(i=0;i<l-1;i++)
 {
  num1=str[i]-'0';
  num2=str[i+1]-'0';
  if(num2<num1)
   {
     f1=1;
     break;
   }
 }
 if(f1==1)
 {
for(i=0;i<l-1;i++)
 {
  num1=str[i]-'0';
  num2=str[i+1]-'0';
  if(num1>num2)
   {f=1;
    for(j=i;j>0;j--)
     {
     num1=str[j]-'0';
     num2=str[j-1]-'0';
     if(num1!=num2)
      {
        pos=j;
        break;
      }
     }
   }
   if(f==1)
    {
    num1=str[pos]-'0';
    num1--;
    ch=(char)(num1+'0');
    str[pos]=ch;
    break;
    }
 }
for(i=pos+1;i<l;i++)
 {
 str[i]='9';
 }
cout<<"Case #"<<g<<": ";
 for(i=0;i<l;i++)
  {
     if(str[i]!='0')
      {
         cout<<str[i];
      }
  }
 }
 else
  {
    cout<<"Case #"<<g<<": ";
    cout<<str;
  }
  cout<<endl;
  g++;
}
    return 0;
}

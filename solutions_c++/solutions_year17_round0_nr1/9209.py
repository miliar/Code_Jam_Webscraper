#include<iostream>
#include<cstring>
#include<map>
#include<utility>
#include<vector>
#include<set>
using namespace std;
int main()
{
int t,i,j,k,n,a,b,c=0;
cin>>t;
while(t--)
{
  c++;
 long long int ans=0;
 char str[1009];
 cin>>str;
 n=strlen(str);
 cin>>k;
 i=0;
 while(str[i]!='\0')
 {
    if(str[i]=='+')
    i++;
    else
    {
      if(i+k<=n)
      {
      for(j=i;j<(i+k);j++)
      {
        if(str[j]=='+')
          str[j]='-';
        else
          str[j]='+';
      }
      ans++;
    }
      i++;
    } 
 }
 bool temp=false;
 for(i=0;i<n;i++)
 {
  if(str[i]=='-')
    {temp=true;
      break;}
 }

 if(temp)
  cout<<"Case #"<<c<<": "<<"IMPOSSIBLE\n";
else
 cout<<"Case #"<<c<<": "<<ans<<endl;
}
 
 
  return 0;
} 
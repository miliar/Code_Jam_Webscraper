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
 long long int answer=0;
 char arr[1009];
 cin>>arr;
 n=strlen(arr);
 cin>>k;
 i=0;
 while(arr[i]!='\0')
 {
    if(arr[i]=='+')
    i++;
    else
    {
      if(i+k<=n)
      {
      for(j=i;j<(i+k);j++)
      {
        if(arr[j]=='+')
          arr[j]='-';
        else
          arr[j]='+';
      }
      answer++;
    }
      i++;
    } 
 }
 bool flag=false;
 for(i=0;i<n;i++)
 {
  if(arr[i]=='-')
    {flag=true;
      break;}
 }

 if(flag)
  cout<<"Case #"<<c<<": "<<"IMPOSSIBLE\n";
else
 cout<<"Case #"<<c<<": "<<answer<<endl;
}
 
 
  return 0;
} 
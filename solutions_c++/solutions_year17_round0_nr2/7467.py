#include<iostream>
#include<algorithm>
#include<cstring>
#include<stdio.h>
using namespace std;
int tidy(int n)
{
  char s[18];
  sprintf(s,"%d",n);
  int d=strlen(s);
  if(d==1)
      return n;
  char s1[18];
  strcpy(s1,s);
  sort(s1,s1+d);
  if(strcmp(s,s1)==0)
    return n;
  else 
    return tidy(n-1);
}
int main()
{
  int t,n,i,j;
  cin>>t;
  for(i=0;i<t;i++)
  {
    cin>>n;
    cout<<"Case #"<<i+1<<": "<<tidy(n)<<endl;
  }
}
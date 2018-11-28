#include<iostream>
#include<string.h>
#include<stdlib.h>
using namespace std;

struct testcases{
unsigned long long int n,y;
}test[100];
int main()
{
 int t,i,j=0,a[19];
 unsigned long long int x,l;
 cout<<"";
 cin>>t;
 for(i=0;i<t;i++)
 cin>>test[i].n;
 if(t>=1 && t<=100)
 {
  for(i=0;i<t;i++)
  {
  if(test[i].n>=1 && test[i].n<=1000)
  {
    x=test[i].n;
    l=x;
    jump:j=0;
    if(x<10)
    {test[i].y=x;continue;}
    a[j]=x%10;
    x=x/10;
    j++;
    while(x!=0)
    {
     a[j]=x%10;
     x=x/10;
     if(a[j-1]<a[j])
     {
      x=--l;
      goto jump;
     }
     j++;
    }
    test[i].y=l;
   }
  }
  for(j=0;j<t;j++)
  cout<<"Case #"<<j+1<<": "<<test[j].y<<endl;
 }
 return 0;
}


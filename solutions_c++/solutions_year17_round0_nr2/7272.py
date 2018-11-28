#include<iostream>
#include<math.h>
using namespace std;
int main()
{
 unsigned long long n,i,m,a,b;
 int c,d,t,j,k;
 cin>>t;
 
 for(k=0;k<t;k++)
 {
  cin>>n;
  cout<<endl;
  a=0;
  b=1;
  for(i=n;i>=1;i--)
  {
   c=0;
   b=1;
   m=i;
   //cout<<i<<endl;
   a=(((i)%10));
   //cout<<i<<endl;
   if(a==n)
    break;
   for(j=2;m!=0;j++)
   {
    m=m/10;
    //d=pow(10,j);
    b=((m)%10);
   // cout<<b<<endl;
    if(b<=a)
     {
      a=b;
      //cout<<a<<endl;
      continue;
     }
    else
     {
      c=1;
      break;
     }
   }
   if(c==0)
    break;
  }
  cout<<"Case #"<<k+1<<": "<<i;
 }
 return 0;
}

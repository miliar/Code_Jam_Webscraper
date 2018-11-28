#include<iostream>
using namespace std;
int main()
{
long long t,n,i,x,r,c,k,j;
 cin>>t;
 while(t>0)
 {
 cin>>n;
 for(i=n;i>=1;i--)
 {
  x=i;
  long long a[20];
  k=0;
  c=0;
  while(x>0)
  {
   r=x%10;
   a[k++]=r;
   x=x/10;
  }
  for(j=0;j<k-1;j++)
  {
   if(a[j]>=a[j+1])
    c++;
   else
    break;
  }
  if(c==k-1)
  {
   cout<<i;
   break;
  }
 }
 t--;
 }
 return 0;
}
#include<iostream>
#include<bits/stdc++.h>
using namespace std;
long long int check(long long int a[],long long int c)
{
    long long int m,b[20],x;
   for(m=0;m<c;m++)
    b[m]=a[m];
  sort(b,b+c,greater<long long int>());
   x=0;
   for(m=0;m<c;m++)
   {
       //cout<<b[m]<<a[m]<<endl;
       if(b[m]==a[m])
        x++;
   }
   //cout<<x<<c<<endl;
   if(x==c)
    return 0;
   else
    return 1;
}
int main()
{
 ios::sync_with_stdio(false);
 long long int t,n,c,i,k,j,d,a[20],z;
 cin>>t;
 z=1;
 while(t)
 {
 cin>>n;
 for(i=n;i>0;i--)
 {
     j=i;
     c=0;
     while(j>0)
     {
       k=j%10;
       a[c]=k;
       c++;
       j=j/10;
     }
     d=check(a,c);
     if(d==0)
        break;
 }
 printf("Case #%lld: %lld\n",(t-(t-z)),i);
 z++;
 t--;
 }
 return 0;
}














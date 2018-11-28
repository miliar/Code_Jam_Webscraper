#include <iostream>
#include <cstdio>
using namespace std;

int main() {
   long long t;
   scanf("%lld",&t);
   for(long long i=1;i<=t;i++)
   {
      long long n,temp1,temp2,c=1;
      scanf("%lld",&n);
      long long temp=n;
     while(temp/10 !=0)
     {
        temp1=temp%10;
         temp2=temp/10;
         temp2=temp2%10;
         if(temp1==0)
           { 
            n=n-1;
            temp=n;
           }
         else if (temp2>temp1 || temp2==0)
         {
            n=n-temp1*c-1*c;
            temp=n;
         }
         else{}
         temp=temp/10;
      }
      printf("Case #%lld: %lld \n",i,n);
   }
	return 0;
}

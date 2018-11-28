#include <stdio.h>
#include<iostream.h>
//#include<vector>



//long double T,N;
  //unsigned long long int N,i,last,sum=0,rev,j,l1,r,n;
long int N,i,last,sum=0,rev,j,l1,r,n;
  int T, t;
  
  void main()
	 {
    freopen("B-small-attempt2.in","r",stdin);

    freopen("output.out","w",stdout);

    scanf("%d",&T);
   
 for(int t=1;t<=T;++t) 
{
        printf("Case #%d: ",t);
 
    
   scanf("%ld/n",&N);



for(i=0;i<100;i++)
{
  
 
 n=N;
static int count=0;
   while(n!=0)
    

   {
	   last= n % 10;
	   //count++;
	 //  sum=sum*10+last;
	   n=n/10;

	   r=n;

	  if(r==n)
	  {
		  l1= n%10;
		  if(last<l1)
		  {
			  N=N-1;

		  }
	  }
	  
}}
/*a=N;
last=a%10;
a=a/10;

r=a;
if(r==a)
{
	l1=n%10;
	if(last<l1)
}*/
  
   printf("%ld\n",N);
 }
}
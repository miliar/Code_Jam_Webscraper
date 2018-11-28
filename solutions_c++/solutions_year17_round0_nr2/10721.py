#include <stdio.h>
#include<iostream>
int main()
{
  unsigned long int t,n,a,c,w=0;
  scanf("%d",&t);
  
	w=0;
	while(t!=0)
	{--t;
		++w;
	int flag=1;
	int b[100]={0};
 
scanf("%d",&n);
 if(n<=9)
     		{
     			printf("Case #%d: %d\n",w,n);
     			}	
 else{
 
  	for(int i=n;i>=9;--i)
 	{ 
 		int g=0;
 		a=i;
 	int	k=0;

 		flag=1;
 		 		 c=a;
 		b[100]={0};
 			g=1;
 		while(c>=10)
 		{
 			if(g>=2)
 			{
 			c=c/(10);
 			}
 			b[k]=c%10;
 			
 			if(b[k]>b[k-1])
 			{
 				flag=0;
 				break;
 				}
 				++k;
 				
 				++g;
 			
 		}
 	
 		b[k]=c;
 	if(flag==1)
 		{
printf("Case #%d: %d\n",w,a);
 		break;
 			}
     		}
     	}
    	
 	
 }	return 0;
 }

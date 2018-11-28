#include<stdio.h>
main()
{
	int arr[10],i,j=0,n,t,flag=0;
	scanf("%d",&t);
	int a=0;
	while(a++<t)
	{
		scanf("%d",&n);
               x:
               	 flag=0;
               	j=0;
               	if(n<10&&n!=0)
               	   printf("Case #%d: %d\n",a,n);
		else
                 {
                  for(i=n;i>0;i=i/10)
		
		arr[j++]=i%10;
                        
			 
		for(i=1;i<j;i++)
		{
			if(arr[i-1]<arr[i]||(arr[i-1]==0)||(arr[i]==0))
			{
			flag=1;
			break;
		        }
		}
		if(flag)
		{
		  n--;
		  goto x;
	       }
	       else
	       printf("Case #%d: %d\n",a,n);
            }
	}
}

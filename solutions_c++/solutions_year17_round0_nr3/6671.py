#include<stdio.h>
int main()
{
	int t,p=1;
	scanf("%d",&t);
	while(t-->0)
	{
	    
		long long n,k,i,j,z,id,ls,rs,b,max,min;
		z=1;
		scanf("%lld %lld",&n,&k);
		long long arr[n],base[n];
		for(i=1;i<=n;i++)					//initialise all elements by 0
			arr[i]=0;
		for(i=1;i<=n;i++)					//initialise all elements by 0
			base[i]=0;
		
		/*	for(i=1;i<=n;i++)
				printf("%lld ",base[i]);
				printf("\n");	*/
		
		for(j=1;j<=k;j++)					//each person entering
		{
			for(i=1;i<=n;i++)				//loop to put values of second array
			{
				if(arr[i]==1)
					base[i]=0;
				else
				{
				
				if(i==1)
				{
					z=1;
					base[i]=z;
				}
				else
				{
					if(arr[i]==arr[i-1])
					{
						z++;
						base[i]=z;
					}
					else
					{
						z=1;
						base[i]=z;
					}
				}				
			}}
			
			
		/*	for(i=1;i<=n;i++)
				printf("%lld ",base[i]);
				printf("\n");	*/
			
			
			
			long long max=base[1],max_id=1;
			for(i=1;i<=n;i++)						//loop to find max in second array
			{
				if(base[i]>max)
				{
					max=base[i];
					max_id=i;
				}
			}
		/*	printf("%lld\n",max_id);	*/
			id=max_id-(max/2);
			arr[id]=1;
			
			
		}
		for(i=1;i<=n;i++)				//loop to put values of second array
			{
				if(arr[i]==1)
					base[i]=0;
				else
				{
				
				if(i==1)
				{
					z=1;
					base[i]=z;
				}
				else
				{
					if(arr[i]==arr[i-1])
					{
						z++;
						base[i]=z;
					}
					else
					{
						z=1;
						base[i]=z;
					}
				}				
			}}
		/*	for(i=1;i<=n;i++)
				printf("%lld ",base[i]);
				printf("\n");	*/
		if(id==1)
			ls=0;
		else{
		
		ls=base[id-1];}
		
		/*	printf("%lld\n",ls);	*/
		if(base[id+1]==0)
			rs=0;
		else
		{
			if(id==n)
			rs=0;
			else
			{
			
			b=id+1;
			while(base[b+1]>base[b] && (b+1)<= n)
				b++;
			rs=base[b];
		}}
	/*	printf("%lld\n",id);	*/	
	printf("Case #%d: ",p);p++;
		if(ls>=rs)
			printf("%lld %lld\n",ls,rs);
		else
			printf("%lld %lld\n",rs,ls);
	}
	return 0;
}

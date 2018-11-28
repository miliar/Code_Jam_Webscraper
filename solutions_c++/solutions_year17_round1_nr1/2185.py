#include<stdio.h>
#include<string.h>
main()
{
	char a[50][50],temp;
	int i,j,k,t,cse,r,c;
	
	scanf("%d",&t);
	for(cse=1;cse<=t;cse++)
	{
		scanf("%d%d",&r,&c);
		for(i=0;i<r;i++)
		scanf("%s",a[i]);
		x:
		for(i=0;i<r-1;i++)
		{
			for(j=0;j<c-1;j++)
			{
			
			if(a[i][j+1]=='?'&&a[i][j]!='?')
			a[i][j+1]=a[i][j];
		}
	}
	for(i=0;i<r-1;i++)
		{
			for(j=c-1;j>=1;j--)
			{
			
			if(a[i][j-1]=='?'&&a[i][j]!='?')
			a[i][j-1]=a[i][j];
				
			
		}
	}
	for(i=r-1,j=0;j<c;j++)
	{
			if(a[i][j+1]=='?'&&a[i][j]!='?')
			a[i][j+1]=a[i][j];
		
	}
		for(i=r-1,j=c-1;j>=1;j--)
	{
			if(a[i][j-1]=='?'&&a[i][j]!='?')
			a[i][j-1]=a[i][j];
		
	}
	
	for(i=0;i<r-1;i++)
	if(a[i][0]=='?')
	strcpy(a[i],a[i+1]);
	
	for(i=r-1;i>=1;i--)
	if(a[i][0]=='?')
	strcpy(a[i],a[i-1]);
	
	if(a[0][0]=='?')
	strcpy(a[0],a[1]);
	
	if(a[r-1][0]=='?')
	strcpy(a[r-1],a[r-2]);
	
	
	for(i=0;i<r-1;i++)
	if(a[i][0]=='?')
	goto x;
	
		printf("Case #%d:\n",cse);
		for(i=0;i<r;i++)
		printf("%s\n",a[i]);
		
	}
	
	
}

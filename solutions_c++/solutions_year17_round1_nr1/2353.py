#include<stdio.h>
#include<string.h>
main()
{
	char a[50][50];
	int i,tryy,j,k,t,r,c;
	
	scanf("%d",&t);
	for(tryy=1;tryy<=t;tryy++)
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
	
		printf("Case #%d:\n",tryy);
		for(i=0;i<r;i++)
		printf("%s\n",a[i]);
		
	}
	
	
}

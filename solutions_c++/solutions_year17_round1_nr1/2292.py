#include<stdio.h>
#include<string.h>
main()
{
	char cakea[50][50];
	int i,j,k,t,ctr,r,c;
	
	scanf("%d",&t);
	for(ctr=1;ctr<=t;ctr++)
	{
		scanf("%d%d",&r,&c);
		for(i=0;i<r;i++)
		scanf("%s",cakea[i]);
		postal:
		for(i=0;i<r-1;i++)
		{
			for(j=0;j<c-1;j++)
			{
			
			if(cakea[i][j+1]=='?'&&cakea[i][j]!='?')
			cakea[i][j+1]=cakea[i][j];
		}
	}
	for(i=0;i<r-1;i++)
		{
			for(j=c-1;j>=1;j--)
			{
			
			if(cakea[i][j-1]=='?'&&cakea[i][j]!='?')
			cakea[i][j-1]=cakea[i][j];
				
			
		}
	}
	for(i=r-1,j=0;j<c;j++)
	{
			if(cakea[i][j+1]=='?'&&cakea[i][j]!='?')
			cakea[i][j+1]=cakea[i][j];
		
	}
		for(i=r-1,j=c-1;j>=1;j--)
	{
			if(cakea[i][j-1]=='?'&&cakea[i][j]!='?')
			cakea[i][j-1]=cakea[i][j];
		
	}
	
	for(i=0;i<r-1;i++)
	if(cakea[i][0]=='?')
	strcpy(cakea[i],cakea[i+1]);
	
	for(i=r-1;i>=1;i--)
	if(cakea[i][0]=='?')
	strcpy(cakea[i],cakea[i-1]);
	
	if(cakea[0][0]=='?')
	strcpy(cakea[0],cakea[1]);
	
	if(cakea[r-1][0]=='?')
	strcpy(cakea[r-1],cakea[r-2]);
	
	
	for(i=0;i<r-1;i++)
	if(cakea[i][0]=='?')
	goto postal;
	
		printf("Case #%d:\n",ctr);
		for(i=0;i<r;i++)
		printf("%s\n",cakea[i]);
		
	}
	
	
}

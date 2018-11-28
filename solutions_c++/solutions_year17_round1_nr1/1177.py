#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;

int main()
{
    int t,x=1;
    scanf("%i",&t);
    while(t--)
    {
    	int r,c;
    	char s[30][30];
        scanf("%i%i",&r,&c);
        printf("Case #%i:\n",x);
        for(int i=0;i<r;i++)
        {
        	scanf("%s",&s[i]);
        }
        /*for(int i=0;i<r;i++)
        {
        	for(int j=0;j<c;j++)
        	{
        		printf("%c",s[i][j] );
        	}
        	printf("\n");
        }*/
        for(int i=1;i<r;i++)
        {
        	for(int j=0;j<c;j++)
        	{
        		if(s[i][j]=='?')
        			s[i][j]=s[i-1][j];
        	}
        }
        for(int i=r-2;i>=0;i--)
        {
        	for(int j=0;j<c;j++)
        	{
        		if(s[i][j]=='?')
        			s[i][j]=s[i+1][j];
        	}
        }
        for(int i=0;i<r;i++)
        {
        	for(int j=1;j<c;j++)
        	{
        		if(s[i][j]=='?')
        			s[i][j]=s[i][j-1];
        	}
        }
        for(int i=0;i<r;i++)
        {
        	for(int j=c-2;j>=0;j--)
        	{
        		if(s[i][j]=='?')
        			s[i][j]=s[i][j+1];
        	}
        }
        for(int i=0;i<r;i++)
        {
        	for(int j=0;j<c;j++)
        	{
        		printf("%c",s[i][j] );
        	}
        	printf("\n");
        }
        x++;
    }
	return 0;
}

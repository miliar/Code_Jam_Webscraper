#include <stdio.h>
#include <iostream>
using namespace std;
int main()
{
	freopen("A-largesb.in","r",stdin);
	freopen("sb2.out","w",stdout);
	int T;
 	cin>>T;
	for(int s=1;s<=T;s++)
	{
		char now[50][50];
		int length,width;
		cin>>length>>width;
		for(int i=0;i<length;i++)
		{
			for(int j=0;j<width;j++)cin>>now[i][j];	
		}
		for(int i=0;i<length;i++)
		{
			for(int j=0;j<width;j++)
			{
				if(now[i][j]!='?')
				{
					int temp=j-1;
					while(now[i][temp]=='?')
					{
						now[i][temp]=now[i][j];
						temp--;
					}
					temp=j+1;
					 while(now[i][temp]=='?')
					{
						now[i][temp]=now[i][j];
						temp++;
					}
				}
			}
		}

		for(int i=0;i<length;i++)
		{
			for(int j=0;j<width;j++)
			{
				if(now[i][j]!='?')
				{
					int temp=i-1;
					while(now[temp][j]=='?')
					{
						now[temp][j]=now[i][j];
						temp--;
					}
					temp=i+1;
					 while(now[temp][j]=='?')
					{
						now[temp][j]=now[i][j];
						temp++;
					}
				}
			}
		}
	
		printf("Case #%d:\n",s);
		for(int i=0;i<length;i++)
		{
			for(int j=0;j<width;j++)printf("%c",now[i][j]);
			printf("\n");
		}
		
	}
 } 

#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#define s(n) scanf("%d", &n)
#define s2(a,b) scanf("%d %d",&a, &b)
#define ss(n) scanf("%s",n)
#define pb push_back
#define vi vector<int>
using namespace std;
char grid[26][26];
int t,T,i,j,r,c,firstr,first[26];
bool flag,mark[26];
int main()
{
	freopen("input.in","r",stdin);
	freopen("opx.txt","w",stdout);
	s(T);
	for(t=1;t<=T;t++)
	{
		s2(r,c);
		for(i=0;i<r;i++)
		{
			ss(grid[i]);
			flag=0;
			mark[i]=0;
			first[i]=0;
			for(j=0;j<c;j++)
			{
				if(grid[i][j]!='?' && flag==0)
				{	
					flag=1;
					first[i]=j;
				}
			}
			if(flag==0)
			{
				mark[i]=1;
			}
		}
		flag=0;
		firstr=0;
		for(i=0;i<r;i++)
		{
			if(mark[i]==0)
			{
				if(flag==0)
				{
					flag=1;
					firstr=i;
				}
				j=0;
				char prev=grid[i][first[i]];
				while(j<first[i])
				{
					grid[i][j]=prev;
					j++;
				}
			//	prev=grid[i][j];
				j++;
				while(j<c)
				{
				 if(grid[i][j]=='?')
				 grid[i][j]=prev;
				 else
				 prev=grid[i][j];
				 j++;	
				}
			}
		}
		i=0;
		while(i<firstr)
		{
			for(j=0;j<c;j++)
			grid[i][j]=grid[firstr][j];
			i++;
		}
		int idx=firstr;
		i++;
		while(i<r)
		{
			if(mark[i]==1)
			{
				for(j=0;j<c;j++)
				grid[i][j]=grid[idx][j];
			}
			else
			idx=i;
			i++;
		}
		printf("Case #%d: \n",t);
		for(i=0;i<r;i++)
		{
			printf("%s\n",grid[i]);
		}
	}
	return 0;
}

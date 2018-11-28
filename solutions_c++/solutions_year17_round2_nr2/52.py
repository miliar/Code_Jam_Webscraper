#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<string>
#include<set>
#include<sstream>
using namespace std;
typedef long long lld;
#define mp make_pair
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define eps 1e-8
#define pi acos(-1.0)
int at[100010];
string solve(int a1,int a2,int a3)
{
	string ans="";
	int n=a1+a2+a3;
	if(n%2 == 0)
	{
		int i=0;
		for(int j=0;j<n/2;j++)
		{
			at[j]=i;
			i=(i+2)%n;
		}
		i=1;
		for(int j=0;j<n/2;j++)
		{
			at[j+n/2]=i;
			i=(i+2)%n;
		}
	}
	else
	{
		int i=0;
		for(int j=0;j<n;j++)
		{
			at[j]=i;
			i=(i+2)%n;
		}
	}
	for(int i=0;i<n;i++)
		ans+='0';
	int big=max(a1,max(a2,a3));
	if(big == a1)
	{
		if(a1 > a2+a3)
			return "";
		int id=-1;
		while(a1--)
		{
			id++;
			ans[at[id]]='R';
		}
		while(a2--)
		{
			id++;
			ans[at[id]]='Y';
		}
		while(a3--)
		{
			id++;
			ans[at[id]]='B';
		}
	}
	else if(big == a2)
	{
		if(a2 > a1+a3)
			return "";
		int id=-1;
		while(a2--)
		{
			id++;
			ans[at[id]]='Y';
		}
		while(a1--)
		{
			id++;
			ans[at[id]]='R';
		}
		while(a3--)
		{
			id++;
			ans[at[id]]='B';
		}
	}
	else
	{
		if(a3 > a1+a2)
			return "";
		int id=-1;
		while(a3--)
		{
			id++;
			ans[at[id]]='B';
		}
		while(a2--)
		{
			id++;
			ans[at[id]]='Y';
		}
		while(a1--)
		{
			id++;
			ans[at[id]]='R';
		}
	}
	return ans;
}
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		printf("Case #%d: ",cc);
		int n,a1,a2,a3,a12,a13,a23;
		scanf("%d %d %d %d %d %d %d",&n,&a1,&a12,&a2,&a23,&a3,&a13);
		if(a12 > a3 || a13 > a2 || a23 > a1)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		if(a12 == a3 && a12 != 0)
		{
			if(a12 + a3 == n)
			{
				for(int i=0;i<n/2;i++)
					printf("OB");
				printf("\n");
			}
			else
				printf("IMPOSSIBLE\n");
			continue;
		}
		if(a13 == a2 && a13 != 0)
		{
			if(a13 + a2 == n)
			{
				for(int i=0;i<n/2;i++)
					printf("YV");
				printf("\n");
			}
			else
				printf("IMPOSSIBLE\n");
			continue;
		}
		if(a23 == a1 && a23 != 0)
		{
			if(a23 + a1 == n)
			{
				for(int i=0;i<n/2;i++)
					printf("RG");
				printf("\n");
			}
			else
				printf("IMPOSSIBLE\n");
			continue;
		}
		a1-=a23;
		a2-=a13;
		a3-=a12;
		string ans=solve(a1,a2,a3);
		if(ans == "")
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		int len=ans.size();
		for(int i=0;i<len;i++)
		{
			printf("%c",ans[i]);
			if(ans[i] == 'R')
			{
				if(a23 != 0)
				{
					for(int j=0;j<a23;j++)
						printf("GR");
					a23=0;
				}
			}
			if(ans[i] == 'Y')
			{
				if(a13 != 0)
				{
					for(int j=0;j<a13;j++)
						printf("VY");
					a13=0;
				}
			}
			if(ans[i] == 'B')
			{
				if(a12 != 0)
				{
					for(int j=0;j<a12;j++)
						printf("OB");
					a12=0;
				}
			}
		}
		printf("\n");
	}
	return 0;
}
/*
4
6 2 0 2 0 2 0
3 1 0 2 0 0 0
6 2 0 1 1 2 0
4 0 0 2 0 0 2

4
4 0 0 2 0 0 2
8 0 2 2 0 2 2
4 2 0 0 2 0 0
4 0 2 0 0 2 0

 */

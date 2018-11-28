#include <stdio.h> 
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ll;
int w, h;
int t;
int n, k, l;

int min(int a, int b)
{
	if (a > b)return b;
	return a;
}
int max(int a, int b)
{
	if (a > b)return a;
	return b;
}

const int MAXN = 30;
int a[MAXN];
int b[MAXN];

void desc(int p, int delta)
{
	for(int i=0;i<p;i++)
		b[i] = a[i];

	if(p==l)
		return ;
	

	b[p] = a[p]-delta;
	for(int i=p+1;i<l;i++)
	{
		if(delta==0)
			b[i]=a[i];
		else
			b[i]=9;
	}
}

int check()
{
	for(int i=1;i<l;i++)
	{
		if(b[i]<b[i-1] || b[i] < 0)
			return 0;
	}
	return 1;
}

void print()
{
	int i=0;
	while(b[i]==0)
		i++;

	while(i<l)
	{
		printf("%d",b[i]);
		i++;
	}
	printf("\n");
}
int main()
{ 
	int tc;
	freopen("blarge.txt","r",stdin);
	freopen("b3.txt","w",stdout);
	scanf("%d",&tc);

	for(int t=1;t<=tc;t++)
	{
		char c[MAXN];
		scanf("%s",c);

		l = strlen(c);

		for(int i=0;i<l;i++)
			a[i] = c[i]-'0';

		int ans=0;
		for(int i=l;i>=0&&ans==0;i--)
		{
			for(int j=0;j<10&&ans==0;j++)
			{
				desc(i, j);
				if(check())
				{
					printf("Case #%d: ",t);
					print();
					ans=1;
				}
			}
		}
	
	}

	return 0;
}


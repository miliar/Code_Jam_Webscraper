#include <iostream>
#include <string.h>

using namespace std;

void minus_one(int *s,int start)
{
	s[start]--;
	if(s[start]<0)
	{
		s[start]=9;
		minus_one(s,start-1);
	}
}
void solve(int *s,int end)
{
	for(int i=0;i<end;i++)
	{
		if(i==0)
			continue;
		if(s[i]<s[i-1])
		{
			minus_one(s,i-1);
			for(int j=i;j<end;j++)
				s[j]=9;
			solve(s,i);
			break;
		}
	}
}

int main()
{
	int N;
	int s[20];
	scanf("%d",&N);
	getchar();
	for (int i=1;i<=N;i++)
	{
		memset(s,0,20);
		printf("Case #%d: ",i);
		char c;
		c= getchar();
		int j=0;
		while(c!='\n')
		{
			s[j]=c-'0';
			j++;
			c=getchar();
		}
		solve(s,j);

	
	bool print=false;
	for(int k=0;k<j;k++)
	{
		if(!print && s[k]==0)
			continue;
		print=true;
		printf("%d",s[k]);
	}
	printf("\n");}
	return 0;
}

#include<bits/stdc++.h>
using namespace std;


int check(char s[],int n)
{
	for(int i=0;i<n;i++)
	{	if(s[i]=='-')return 0;
	}
	return 1;
	
}

int main()
{
	int t,k;
	char s[2000];
	scanf("%d",&t);
	int iteration=1;
	while(t--)
	{	scanf("%s",&s);
		scanf("%d",&k);
		int count=0;
		int n = strlen(s);
		for(int i=0;i<=n-k;i++)
		{	if(s[i]=='-')
			{	for(int j=i;j<i+k;j++)
				{	if(s[j]=='-')s[j]='+';
					else if(s[j]=='+')s[j]='-';
				}
				count++;
			}
			
		}
		if(check(s,n))
		{	printf("Case #");printf("%d: %d\n",iteration,count);
		}
		else
		{	printf("Case #");printf("%d: IMPOSSIBLE\n",iteration);
		}
		iteration++;
	}
	
}

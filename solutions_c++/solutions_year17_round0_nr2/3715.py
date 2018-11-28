#include<bits/stdc++.h>
using namespace std;
char s[100];
int main()
{
	int t,n,i,j;
	scanf("%d",&t);
	int temp=t;
	while(t--)
	{
		scanf("%s",s);
		printf("Case #%d: ",temp-t);
		int len=strlen(s);
		int n=len;
		if (len==1)
			printf("%s\n",s);
		
		else
		{
			
			int A[25];
			for(i=0;i<n;i++)
				A[i]=s[i]-'0';
			for(i=1;i<n;i++)
			{
				if (A[i]>=A[i-1])
				{
					continue;
				}
				else
				{
					A[i-1]--;
					//
					int k=i-1;
					while(k-1>=0 && A[k]<A[k-1])
					{
						A[k]=9;
						A[k-1]--;
						k--;
					}
						
					for(j=i;j<n;j++)
						A[j]=9;
					break;
				}
		}
		i=0;
		while(A[i]==0)i++;
		for(;i<n;i++)
				printf("%d",A[i]);
		printf("\n");
		}
	}
	return 0;
}
			

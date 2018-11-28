#include<bits/stdc++.h>
using namespace std;

typedef unsigned long long int LLU;

int main()
{
	LLU N,T,temp,flag,min,rem;
	scanf("%llu",&T);
	for(LLU i=1;i<=T;i++)
	{
		scanf("%llu",&N);
		//printf("%llu\n",N);
		for(LLU j=N;j>=1;j--)
		{
			min=j%10;
			temp=j;
			flag=1;
			while(temp!=0)
			{
				//cout<<"check"<<endl;
				rem=temp%10;
				if(rem>min)
				{
					flag=0;
					break;
				}
				else
				{
					min=rem;
					temp=temp/10;
				}
			}
			if(flag)
			{
				printf("Case #%llu: %llu\n",i,j);
				break;
			}
		}
	}


	
	return 0;
}
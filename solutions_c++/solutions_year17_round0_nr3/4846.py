#include <cstdio>
#include <iostream>
#include <map>
using namespace std;

int main()
{
	int T,N,K;
	int max,min;
	int temp;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		scanf("%d %d",&N,&K);
		while(K != 1)
		{
			if(K%2 == 1 && N%2 == 0)
			{
				N = N/2-1;
			} else{
				N = N/2;
			}
			K = K/2;
		}
		max = N/2;
		min = N/2;
		if(N%2 == 0 && min != 0)
		{
			min -= 1;
		}
		printf("CASE #%d: %d %d\n",i,max,min);
	}
	return 0;
}


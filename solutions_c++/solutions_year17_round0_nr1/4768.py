#include <cstdio>
#include <algorithm>
#include <queue>
#include <math.h>
#include <iostream>
#include <stdlib.h>
#include <map>
using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int numCases;
	scanf("%d", &numCases);
	for (int i=0;i<numCases;i++)
	{
		bool pancakes[1001];
		int flip,size=0;
		char c;
		scanf("%c",&c);
		printf("Case #%d: ",i+1);
		for (int j=0;;j++)
		{
			scanf("%c",&c);
			if (c=='+')
			{
				pancakes[j]=1;
				size++;
			} else if (c=='-') {
				pancakes[j]=0;
				size++;
			} else {
				break;
			}
		}
		scanf("%d",&flip);
		bool broken=0;
		int steps=0;
		for (int j=0;j<size;j++)
		{
			if (pancakes[j]==0)
			{
				steps++;
				for (int k=0;k<flip;k++)
				{
					if (k+j>=size)
					{
						printf("IMPOSSIBLE\n");
						broken=1;
						break;
					}
					if (pancakes[k+j]==0)
					{
						pancakes[k+j]=1;
					} else {
						pancakes[k+j]=0;
					}
				}
				if (broken==1)
				{
					break;
				}
			}
		}
		if (broken==0)
		{
			printf("%d\n",steps);
		}

	}
}

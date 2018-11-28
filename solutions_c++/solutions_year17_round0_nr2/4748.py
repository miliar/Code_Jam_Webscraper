#include <cstdio>
#include <algorithm>
#include <queue>
#include <math.h>
#include <iostream>
#include <stdlib.h>
#include <map>
using namespace std;

bool check(long long num) {
	int prev = 10;
	for (;num > 0;num = num / 10) {
		if (prev >= num % 10) {
			prev = num % 10;
		} else {
			return 0;
		}
	}
	return 1;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int numNums;
	scanf("%d", &numNums);
	for (int i=0;i<numNums;i++)
	{
		int nCount = 0;
		long long num;
		scanf("%lld",&num);
		printf("Case #%d: ",i+1);
		for (;;)
		{
			if (check(num)==1)
			{
				if (num>0)
					printf("%lld",num);
				for (int j=0;j<nCount;j++)
				{
					printf("9");
				}
				printf("\n");
				break;
			} else {
				num-=(num%10+1);
				num=num/10;
				nCount++;
			}
		}
	}
}

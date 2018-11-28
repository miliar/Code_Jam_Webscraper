#include <cstdio>
#include <algorithm>
#include <queue>
#include <math.h>
#include <iostream>
#include <stdlib.h>
#include <map>
using namespace std;

int main() {
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("C-small-2-attempt0.out", "w", stdout);
	int numCases;
	scanf("%d", &numCases);
	for (int i=0;i<numCases;i++)
	{
		printf("Case #%d: ",i+1);
		long long size,people;
		priority_queue<long long>lengths;
		scanf("%lld %lld",&size,&people);
		lengths.push(size);
		for (int i=1;i<people;i++)
		{
			long long top=lengths.top();
			lengths.push(top/2);
			lengths.push(top-(top/2)-1);
			lengths.pop();
		}
		if (lengths.top()%2==0)
		{
			printf("%lld %lld\n",lengths.top()/2,(lengths.top()/2)-1);
		} else {
			printf("%lld %lld\n",lengths.top()/2,lengths.top()/2);
		}
	}
}

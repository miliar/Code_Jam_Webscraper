#include <iostream>
#include <queue>
#include <string>
#include <cstdlib>
#include <math.h>
#include <stdio.h>

using namespace std;


int main(int argc, char const *argv[])
{
	/* code */
	
		int t;
	scanf("%d",&t);
	for (int i = 0; i < t; i++)
		{
			/* code */
		priority_queue<long long int> q;
		long long int n;
		long long int k;
		scanf("%lld",&n);
		scanf("%lld",&k);
		q.push(n);
		for (long long int j = 1; j < k; j++)
		{
			long long int dummy = q.top();
			q.pop();
			long long int rsd= (ceil((dummy-1.0)/2.0));
			long long int lsd= (floor((dummy-1.0)/2.0));
			q.push(rsd);
			q.push(lsd);
			
			/* code */
			//printf("%lld\n",dummy);

		}

		long long int val = q.top();
		long long int rs= (ceil((val-1.0)/2.0));
		long long int ls=(floor((val-1.0)/2.0));
			
		printf("Case #%d: %lld %lld\n",i+1,rs,ls);	
		
			
		}


	return 0;
}
#include <stdio.h>
#include <queue>
#include <iostream>

using namespace std;

int main(void) {

	int t;
	scanf("%d", &t);
	for( int cnt=0; cnt<t; cnt++ ) {

		long long int n, k, y, z;
		scanf("%lld%lld", &n, &k);
		printf("Case #%d: ", cnt+1);
		// if( ( n%2==0 && k>n/2 ) || ( n%2 && k>n/2+1 ) ) {
		// 	printf("0 0\n");
		// 	continue;
		// }

		priority_queue<long long int> q;
		q.push(n);

		while( k-- ) {
			long long int max = q.top();
			q.pop();

			y = max/2;
			if( max%2 ) z = y;
			else z = y-1;

			q.push(y);	q.push(z);
		}

		printf("%lld %lld\n", y, z);
	}

	return 0;
}

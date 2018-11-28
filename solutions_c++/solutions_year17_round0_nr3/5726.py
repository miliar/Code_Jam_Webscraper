#include <stdio.h>
#include <vector>
#include <queue>
#include <algorithm>
#include <string>
using namespace std;
#define ll longlong

int main(void) {
	int T, K, N;
	string S;
	scanf("%i", &T);
	for (int i=0;i<T;i++) {
		scanf("%i %i", &N, &K);
		int r, r1, r2; //z,k,r1,r2,z1,z2,k1,k2;
		priority_queue <int> p;
		p.push(N);
		for (int j=0; j<K; j++) {
			r = p.top();
			//z = p.front().second;
			p.pop();
			r1 = r/2;
			r2 = (r-1)/2;
			//k=r+z-1;
			//z1=r/2+z; k1=k; r1=k1-z1+1;
			//z2=z; k2=r/2+z-2; r2=k2-z2+1;
			p.push(r1);
			p.push(r2);
		}
		printf("Case #%i: %i %i\n", i+1, r1, r2);
	}
	return 0;
}

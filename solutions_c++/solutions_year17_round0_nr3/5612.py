#include <cstdio>
#include <queue>

using namespace std;

int main() {
	int testcases;
	long nstalls, npeople;
	long dmin, dmax;
	
	priority_queue <long> pqranges;
	
	scanf("%d", &testcases);
	
	for(int t = 0; t < testcases; ++t) {
		scanf("%ld %ld", &nstalls, &npeople);
		
		pqranges.push(nstalls);
		
		for(long i = 0; i < npeople; ++i) {
			long u = pqranges.top();
			pqranges.pop();
			
			if(u & 0x1) {
				dmin = dmax = u >> 1;
				
				pqranges.push(u >> 1);
				pqranges.push(u >> 1);
			}
			else {
				dmin = (u >> 1) - 1;
				dmax = u >> 1;
				
				pqranges.push((u >> 1) - 1);
				pqranges.push(u >> 1);
			}
		}
		
		while(!pqranges.empty()) {
			pqranges.pop();
		}
		
		printf("Case #%d: %ld %ld\n", t + 1, dmax, dmin);
	}
}
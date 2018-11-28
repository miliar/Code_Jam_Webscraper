#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>

using namespace std;

int main() {
	vector <int> distvec;
	queue <int> bfsqueue;
	
	char pcakes[1005];
	int testcases, w, slen, cakeint;

	scanf("%d", &testcases);
	
	for(int t = 0; t < testcases; ++t) {
		scanf("%s %d", pcakes, &w);
		
		slen = strlen(pcakes);
		distvec.assign((1 << slen) + 5, -1);
		
		cakeint = 0;
		for(int i = 0; i < slen; ++i) {
			cakeint <<= 1;
			cakeint |= (pcakes[i] == '+' ? 1 : 0);
		}
		
		distvec[cakeint] = 0;
		bfsqueue.push(cakeint);
		while(!bfsqueue.empty()) {
			int u = bfsqueue.front();
			int fmask = (1 << w) - 1;
			bfsqueue.pop();
			
			for(int i = 0; i < slen - w + 1; ++i) {
				int d = u ^ (fmask << i);
				
				if(distvec[d] == -1) {
					distvec[d] = distvec[u] + 1;
					bfsqueue.push(d);
				}
			}
		}
		
		printf("Case #%d: ", t + 1);
		
		if(distvec[(1 << slen) - 1] >= 0) {
			printf("%d\n", distvec[(1 << slen) - 1]);
		}
		else {
			printf("IMPOSSIBLE\n");
		}
	}

	return 0;
}
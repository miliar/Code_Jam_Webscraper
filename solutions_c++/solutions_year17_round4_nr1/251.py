#include <bits/stdc++.h>

#define SZ(a) (int)a.size()
#define PB push_back

using namespace std;

typedef long long ll;

int main() {
	
	int T;
	scanf("%d ", &T);
	
	for(int tt = 1; tt <= T; tt++) {
		printf("Case #%d: ", tt);
		
		int N,P;
		scanf("%d %d", &N, &P);
		
		vector<int> count(P, 0);
		
		for(int i = 0; i < N; i++) {
			int G;
			scanf("%d", &G);
			count[G%P]++;
		}
		
		if(P==2) {
			printf("%d\n", N - (count[1]/2));
			continue;
		}
		if(P==3) {
			int m = min(count[1],count[2]);
			int mm = max(count[1],count[2]) - m;
			int w = (mm+2)/3;
			printf("%d\n", N - m - mm + w);
		}
	}
	
	return 0;
}

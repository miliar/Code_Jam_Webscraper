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
		
		int N,C,M;
		scanf("%d %d %d", &N, &C, &M);
		
		vector<int> c(C,0);
		vector<int> n(N,0);
		int max_seat = 0;
		
		for(int i = 0; i < M; i++) {
			int a,b;
			scanf("%d%d", &a, &b);
			a--;
			b--;
			c[b]++;
			n[a]++;
			max_seat = max(max_seat, n[a]);
		}
		
		int r1 = max(c[0],c[1]);
		int r2 = n[0];
		
		if(r2 >= r1) printf("%d 0\n", r2);
		else printf("%d %d\n", r1, max(0,max_seat-r1));
	}
	
	return 0;
}

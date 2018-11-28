#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <string>
using namespace std;

int main(void) {
	int T, N, P, i;
	int G[128];
	int hist[4];
	int ans, a;
	
	cin >> T;
	for (int t=1; t<=T; t++) {
		printf("Case #%d: ", t);
		cin >> N >> P;
		for (i=0; i<N; i++) cin >> G[i];
		for (i=0; i<N; i++) G[i] = G[i] % P;
		for (i=0; i<4; i++) hist[i] = 0;
		for (i=0; i<N; i++) hist[G[i]]++;
		//for (i=0; i<4; i++) printf("%d ", hist[i]);
		ans = hist[0];	//mod 0 goes first everyone gets fresh
		if (P==2) {
			a = hist[1] / 2;	//pair up odd groups
			ans += a;
			hist[1] -= 2*a;		//there could be 1 unpaired group
			if (hist[1]) ans++;	//who gets fresh
		}
		if (P==3) {
			//pair up mod 1 and 2
			a = hist[1];
			if (hist[2] < a) a = hist[2];
			ans += a;
			hist[1] -= a;
			hist[2] -= a;
			//one of hist[1] or hist[2] is now 0
			//pair up mod 1 with itself
			a = hist[1] / 3;
			ans += a;
			hist[1] -= 3*a;
			//pair 2 with itself
			a = hist[2] / 3;
			ans += a;
			hist[2] -= 3*a;
			//leftovers
			if (hist[1] || hist[2]) ans++;
		}
		if (P==4) {
			//pair up mod 1 and 3
			a = hist[1];
			if (hist[3] < a) a = hist[3];
			ans += a;
			hist[1] -= a;
			hist[3] -= a;
			//one of hist[1] or hist[3] is now 0
			//pair up mod 2 with itself
			a = hist[2] / 2;
			ans += a;
			hist[2] -= 2*a;
			//hist[2] is either 0 or 1
			//try 1 1 2
			if (hist[1] >= 2 && hist[2] >= 1) {
				ans++;
				hist[1] -= 2;
				hist[2] -= 1;
			}
			//try 3 3 2
			if (hist[3] >= 2 && hist[2] >= 1) {
				ans++;
				hist[3] -= 2;
				hist[2] -= 1;
			}
			//pair 1 with itself
			a = hist[1] / 4;
			ans += a;
			hist[1] -= 4*a;
			//pair 3 with itself
			a = hist[3] / 4;
			ans += a;
			hist[3] -= 4*a;
			//leftovers
			if (hist[1] || hist[2] || hist[3]) ans++;
		}
		printf("%d", ans);
		printf("\n");
	}
	
	return 0;
}
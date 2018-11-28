#include <bits/stdc++.h>
using namespace std;

void solve() {
	int T;
	scanf("%d", &T);
	getchar();
	for (int i = 0; i < T; i++) {
		long long N , K;
		scanf("%lld%lld", &N, &K);
		stack<int > trav;

		while (K != 1) {
			long long pow = 0;
			long long one = 1;
			while(K >= one << pow)
				pow++;
			pow--;
			if (K <= ((one << pow)-one + (one << (pow-one)))) {
				trav.push(0);
				K -= one << (pow-one); 
			}
			else {
				trav.push(1);
				K -= one << (pow);
			}
		}

		/*zerrechnen!!!*/
		while (!trav.empty()) {
			if (trav.top())
				if (N % 2 == 0)
					N = (N-2)/2;
				else
					N = (N-1)/2;
			else
				if (N % 2 == 0)
					N = N/2;
				else
					N = (N-1)/2;
			trav.pop();
		}

		long long sol1 = 0, sol2 = 0;

		if (N % 2 == 0) {
			sol2 = (N-2)/2;
			sol1 = N/2;
		}
		else {
			sol2 = (N-1)/2;
			sol1 = (N-1)/2;
		}
		printf("Case #%d: %lld %lld\n", i+1, sol1, sol2);
	}
}

int main() {
	solve();
	return 0;
}
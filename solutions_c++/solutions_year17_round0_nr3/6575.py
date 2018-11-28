#include <bits/stdc++.h>

using namespace std;

int main() {
	int tc, n, k;
	scanf("%d", &tc);
	for (int t = 0; t < tc; t++) {
		bool occ[1002] = {};
		int leftDist[1002] = {}, rightDist[1002] = {}, last;
		
		scanf("%d %d", &n, &k);
		occ[0] = occ[n + 1] = true;
		
		for (int i = 0; i < n + 2; i++) {
			if (occ[i]) {
				leftDist[i] = 0;
				last = i;
			} else {
				leftDist[i] = i - last;
			}
		}
		
		for (int i = n + 1; i >= 0; i--) {
			if (occ[i]) {
				rightDist[i] = 0;
				last = i;
			} else {
				rightDist[i] = last - i;
			}
		}
		
		/*for (int j = 0; j < n + 2; j++) {
			printf("LR %d %d\n", leftDist[j], rightDist[j]);
		}*/
		
		int bestPos;
		for (int i = 0; i < k; i++) {
			bestPos = -1;
			for (int j = 0; j < n + 2; j++) {
				if (occ[j]) {
					continue;
				}
				
				if (bestPos == -1) {
					bestPos = j;
					continue;
				}
				
				if (min(leftDist[j], rightDist[j]) > min(leftDist[bestPos], rightDist[bestPos])) {
					bestPos = j;
				} else if (min(leftDist[j], rightDist[j]) == min(leftDist[bestPos], rightDist[bestPos])) {
					if (max(leftDist[j], rightDist[j]) > max(leftDist[bestPos], rightDist[bestPos])) {
						bestPos = j;
					}
				}
			}
			
			//printf("Bestpos %d\n", bestPos);
			
			if (i == k - 1) {
				break;
			}
			
			occ[bestPos] = true;
			
			for (int j = 0; j < n + 2; j++) {
				if (occ[j]) {
					leftDist[j] = 0;
					last = j;
				} else {
					leftDist[j] = j - last;
				}
			}
			
			for (int j = n + 1; j >= 0; j--) {
				if (occ[j]) {
					rightDist[j] = 0;
					last = j;
				} else {
					rightDist[j] = last - j;
				}
			}
			
			/*for (int j = 0; j < n + 2; j++) {
				printf("LR %d %d\n", leftDist[j], rightDist[j]);
			}*/
		}
		
		//printf("Final %d\n", bestPos);
		printf("Case #%d: %d %d\n", t + 1, max(leftDist[bestPos], rightDist[bestPos]) - 1, min(leftDist[bestPos], rightDist[bestPos]) - 1);
	}
}

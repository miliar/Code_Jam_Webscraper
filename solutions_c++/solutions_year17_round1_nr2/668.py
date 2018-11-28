#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;

inline int getMin(int base, int package) {
	return (package*10 + 11*base - 1) / (11*base);
}

inline int getMax(int base, int package) {
	return (package*10) / (9*base);
}

int main(void) {
	int T, N, P, n, p;
	int **list;
	list = new int * [64];
	for (int i=0; i<64; i++) list[i] = new int [64];
	int base[64];
	int mini[64];
	int maxi[64];
	int pos[64];
	int largestMin, smallestMax, index;
	int kit;
	
	cin >> T;
	for (int t=1; t<=T; t++) {
		printf("Case #%d: ", t);
		kit = 0;
		cin >> N >> P;
		for (n=0; n<N; n++) cin >> base[n];
		for (n=0; n<N; n++) for (p=0; p<P; p++) cin >> list[n][p];
		
		for (n=0; n<N; n++) sort(&list[n][0], &list[n][P]);
		//for (n=0; n<N; n++) { printf("\n"); for (p=0; p<P; p++) printf("%d ", list[n][p]); }
		
		for (n=0; n<N; n++) pos[n] = 0;
		
		while (1) {
			for (n=0; n<N; n++) {
				mini[n] = getMin(base[n], list[n][pos[n]]);
				maxi[n] = getMax(base[n], list[n][pos[n]]);
			}
			
			//for (n=0; n<N; n++) printf("index %d, min %d, max %d\n", n, mini[n], maxi[n]);
			
			largestMin = mini[0];
			for (n=1; n<N; n++) {
				if (mini[n] > largestMin) {
					largestMin = mini[n];
				}
			}
			smallestMax = maxi[0];
			for (n=1; n<N; n++) {
				if (maxi[n] < smallestMax) {
					smallestMax = maxi[n];
				}
			}
			
			if (largestMin <= smallestMax) {	//make a kit
				//printf("kit %d\n", kit);
				kit++;
				for (n=0; n<N; n++) {
					pos[n]++;
					if (pos[n] == P) goto finish;
				}
				for (n=0; n<N; n++) {
					mini[n] = getMin(base[n], list[n][pos[n]]);
					maxi[n] = getMax(base[n], list[n][pos[n]]);
				}
			}
			else {	//walk the smallest min forward, if tie choose smallest max, that package won't be used in any kit
				index = 0;
				for (n=1; n<N; n++) {
					if (mini[n] < mini[index]) index = n;
					else if (mini[n] == mini[index] && maxi[n] < maxi[index]) index = n;
				}
				n = index;
				//printf("incr %d\n", n);
				pos[n]++;
				if (pos[n] == P) goto finish;
				mini[n] = getMin(base[n], list[n][pos[n]]);
				maxi[n] = getMax(base[n], list[n][pos[n]]);
			}
		}
		finish:
		printf("%d\n", kit);
	}
	
	return 0;
}
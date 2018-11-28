#pragma warning(disable:4996)
#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

char color[7]="ROYGBV";

int main() {
//	freopen("B-small-attempt0.in", "r", stdin);
//	freopen("B-small-attempt0.out", "w", stdout);
	int T;
	cin >> T;
	int N;
	int c[7];
	char out[1001];
	out[1000]=0;
	for (int tc = 1; tc <= T; tc++) {
		cin >> N;
		out[N] = 0;
		for (int i=0; i<6; i++) {
			cin >> c[i];
		}

		int Max = 0;
		int pos = 1;
		int iMax = -1;	
		for (int i=0; i<6; i++) {
			if (c[i] > N/2) {
				pos = 0;
				i=10;
			}
			if (c[i] > Max) {
				Max = c[i];
				iMax = i;
			}
		}


		if (pos == 0) {
			printf("Case #%d: IMPOSSIBLE\n", tc);
			continue;
		}

		int j=0;
		int i1 = iMax;
		int i2 = (iMax+2)%6;
		int i3 = (iMax+4)%6;
		while (c[i1]<c[i2]+c[i3]) {
			c[i1]--;
			out[j++] = color[i1];
			c[i2]--;
			out[j++] = color[i2];
			c[i3]--;
			out[j++] = color[i3];
		}

		while (j<N && c[i2]>0) {
			c[i1]--;
			out[j++] = color[i1];
			c[i2]--;
			out[j++] = color[i2];
		}
		while (j<N) {
			c[i1]--;
			out[j++] = color[i1];
			c[i3]--;
			out[j++] = color[i3];
		}
			

		printf("Case #%d: %s\n", tc, out);
		
		

	}
	return 0;
}

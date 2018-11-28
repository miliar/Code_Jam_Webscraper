#include <bits/stdc++.h>
using namespace std;
int t, n;

int main () {
	scanf("%d", &t);
	for (int k=1; k<=t; k++) {
		printf("Case #%d: ", k);
		scanf("%d", &n);
		for (int i=n; i>0; i--) {
			if (i>=100 && i!=1000) {
				int c=i/100;
				int d=(i%100)/10;
				int u=(i%100)%10;
				if (c<=d && d<=u) {
					printf("%d\n", i);
					break;
				}
			}
			else if (i<100 && i>=10) {
				int d=i/10;
				int u=i%10;
				if (d<=u) {
					printf("%d\n", i);
					break;
				}
			}
			else if (i<10 && i>=1) {
				printf("%d\n", i);
				break;
			}
		}
	}
}

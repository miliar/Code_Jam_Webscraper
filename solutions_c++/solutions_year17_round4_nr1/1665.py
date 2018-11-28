#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
using namespace std;
typedef long long ll;

int n, p;


#define abs(X) ((X)<0?-(X):(X))
#define MAX(X, Y) ((X)<(Y)?(Y):(X))
#define MIN(X, Y) ((X)>(Y)?(Y):(X))

void T(int TC) {
	int a[100], b[100];
	int c[5][100], z[5] = {0};
	int i;
	scanf("%d %d", &n, &p);
	for(i=0;i<n;i++) {
		scanf("%d", a + i);
		b[i] = a[i] % p;
		c[b[i]][z[b[i]]++] = p - i;
	}

	int result = z[0];
	if(p == 2) {
		result += (z[1] + 1) / 2;
	} else if(p == 3) {
		result += MIN(z[1], z[2]) + (abs(z[1] - z[2]) + 2) / 3;
		
	} else {
		result += MIN(z[1], z[2]) + (abs(z[1] - z[3]) + 3) / 4 + ((z[2]+1) / 2);
	}

	printf("%d\n", result);
}

int main() {
	int t;
	scanf("%d", &t);
	for(int i=1;i<=t;i++) {
		printf("Case #%d: ", i);
		T(i);
	}
	return 0;
}

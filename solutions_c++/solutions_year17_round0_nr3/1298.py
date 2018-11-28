#include<stdio.h>
#include<string.h>
#include <algorithm>
#include<queue>
#include<string>
#include<math.h>
#include<vector>
#include <map>
#include <stack>
#include<set>

using namespace std;


int main() {
	int tc, t, i, j;
	FILE *fp1,*fp2;
	fp1= fopen("1.in", "r");
	fp2 = fopen("2.out","w");
	fscanf(fp1, "%d", &tc);
	for (t = 1; t <= tc; t++) {
		priority_queue<long long>Q;
		long long n, k;
		fscanf(fp1, "%lld%lld", &n, &k);
		fprintf(fp2, "Case #%d: ", t);
		while (k >= 2) {
			if (n % 2 == 1) {
				n /= 2;
				k /= 2;
			}
			else {
				if (k % 2 == 0) {
					n /= 2;
					k /= 2;
				}
				else {
					n /= 2; n--;
					k /= 2;
				}
			}
		}
		if (n % 2 == 1)
			fprintf(fp2, "%lld %lld\n", n / 2, n / 2);
		else {
			fprintf(fp2, "%lld %lld\n", n / 2, n / 2-1);
		}
	}
	fclose(fp1);
	fclose(fp2);
}



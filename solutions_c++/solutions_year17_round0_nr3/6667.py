#include <cstdio>  
#include <algorithm>  
#include <cstring>  
using namespace std;

int main() {
	int a, n, k;
	freopen("C-small-1-attempt1.in", "r", stdin);
 	freopen("outputc.out", "w", stdout);  
	scanf("%d", &a);
	for (int i = 1; i <= a; i++) {
		scanf("%d %d", &n, &k);
		bool t[1003] ={
			false
		};
		t[0] = true;
		t[n + 1] = true;
		int min, max;
		for (int j = 0; j < k; j++) {
			min = 0;
			max = 0;
			int index = -1;
			for (int m = 1; m <= n; m++) {
				if (!t[m]) {
					int mintemp = 0;
					int maxtemp = 0;
					int q1 = 1;
					while (q1 <= m && !t[m - q1]) {
						q1++;
					}
					int q2 = 1;
					while (q2 + m <= n + 1 && !t[m + q2]) {
						q2++;
					}
					if (q1 < q2) {
						mintemp = q1 - 1;
						maxtemp = q2 - 1;
					} else {
						mintemp = q2 - 1;
						maxtemp = q1 - 1;
					}
					if (mintemp > min  || (mintemp == min && maxtemp > max)) {
						min = mintemp;
						max = maxtemp;
						index = m;
					}
				}
			}
			t[index] = true;
			if (j == k -1) {
				printf("Case #%d: %d %d\n", i, max, min);
			}			
		}
	}
	return 0;
}
					/*bool left = false;
					bool right = false;
					for (int q = 1; q <= m && q + m <= n; q++) {
						if (!left && t[m - q]) {
							left = true;
							if (!right) {
								min = min < q : q : min;
							} else {
								max = max < q : q : max;
							}
						} else if (!right && t[q + m]) {
							right = true;
							if (!left) {
								min = min < q : q : min;
							}
						}
				}*/
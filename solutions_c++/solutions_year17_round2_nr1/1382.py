#include <stdio.h>
#include <bits/stdc++.h>

using namespace std;

#define mp make_pair
#define ss second
#define ff first

pair <int, int> h[1010];

int main () {
	
	int t;
	
	int d, n;
	
	scanf("%d", &t);
	
	for (int i = 0; i < t; i++) {
		
		scanf("%d %d", &d, &n);
		
		for (int j = 0; j < n; j++) {
			scanf("%d %d", &h[j].ff, &h[j].ss);
		}
		
		sort(h, h + n);
		
		double min = 0.0;
		double max = 1e26;
		double meio;
		for (int a = 0; a < 200; a++) {
			meio = (min + max) / 2;
			int j;
			for (j = 0; j < n; j++) {
				if (meio > h[j].ss + 1e-9) {
					double s = meio * h[j].ff / (meio - h[j].ss);
					
					//printf("%lf %d %lf %d\n", meio, h[j].ss, s, d);
					
					if (s < ((double) d)) {
						//printf("1\n");
						max = meio;
						break;
					}
				}
			}
			if (j == n) {
				min = meio;
			}
		}
		printf("Case #%d: %.9lf\n", i + 1, min);
	}
	
	return 0;
	
}

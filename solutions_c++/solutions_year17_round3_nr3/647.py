#include <bits/stdc++.h>

using namespace std;

int main() {
	int tc;
	scanf("%d", &tc);
	for (int t = 0; t < tc; t++) {
		int n, k;
		double u, p[50];
		
		scanf("%d %d", &n, &k);
		scanf("%lf", &u);
		for (int i = 0; i < n; i++) {
			scanf("%lf", &p[i]);
		}
		
		double smallest, secondSmallest;
		vector<int> smallestId;
		sort(p, p + n);
		while (u > 0) {
			smallest = -1;
			secondSmallest = -1;
			smallestId.clear();
			
			smallest = p[0];
			for (int i = 0; i < n; i++) {
				if (p[i] != smallest) {
					secondSmallest = p[i];
					break;
				}
				smallestId.push_back(i);
			}
			
			//printf("smallest %lf, secondsmallest %lf\n", smallest, secondSmallest);
			
			double diff = secondSmallest - smallest;
			if (secondSmallest != -1 && u >= diff * smallestId.size()) {
				// Training unit suffices
				u -= diff * smallestId.size();
				for (int i = 0; i < smallestId.size(); i++) {
					p[smallestId[i]] = secondSmallest;
				}
			} else {
				// Training unit does not suffice
				double increase = u / smallestId.size();
				u = 0;
				for (int i = 0; i < smallestId.size(); i++) {
					p[smallestId[i]] += increase;
				}
			}
		}
		
		double prob = 1;
		for (int i = 0; i < n; i++) {
			//printf("%lf ", p[i]);
			prob *= p[i];
		}
		//printf("\n");
		printf("Case #%d: %.9lf\n", t + 1, prob);
	}
}

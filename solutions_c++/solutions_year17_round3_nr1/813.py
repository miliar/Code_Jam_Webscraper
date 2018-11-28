#include <bits/stdc++.h>
#define PI acos(-1)

using namespace std;

pair<double, int> side[1000];
int radius[1000];
int height[1000];
bool taken[1000];

int main() {
	int tc;
	scanf("%d", &tc);
	for (int t = 0; t < tc; t++) {
		int n, k, r, h;
		
		scanf("%d %d", &n, &k);
		
		for (int i = 0; i < n; i++) {
			scanf("%d %d", &r, &h);
			side[i] = make_pair(2 * PI * r * h, i);
			radius[i] = r;
			height[i] = h;
		}
		sort(side, side + n, greater<pair<double, int> >());
		
		double maxArea = 0;
		// Try as base
		for (int i = 0; i < n; i++) {
			double area = 0;
			memset(taken, 0, sizeof(taken));
			
			area += PI * radius[i] * radius[i] + 2 * PI * radius[i] * height[i];
			taken[i] = true;
			
			int num = 1;
			for (int j = 0; j < n; j++) {
				if (num == k) {
					break;
				}
				
				if (taken[side[j].second]) {
					continue;
				}
				
				if (radius[side[j].second] > radius[i]) {
					continue;
				}
				
				area += side[j].first;
				taken[side[j].second] = true;
				num++;
			}
			
			maxArea = max(area, maxArea);
		}
		
		printf("Case #%d: %.9lf\n", t + 1, maxArea);
	}
}

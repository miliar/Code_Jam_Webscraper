#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <string>
#include  <cstring>
#include <cstdlib>
#include <cmath>

using namespace std;

const double pi = acos(-1);

vector<pair<double, double> > pancakes;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int test = 1; test<=t; test++) {
		int n, k;
		scanf("%d %d", &n, &k);
		pancakes.clear();
		for(int i = 0; i < n; i++) {
			double r, h;
			scanf("%lf %lf", &r, &h);
			pancakes.push_back({r, h});
		}
		double maximum = 0;
		sort(pancakes.rbegin(), pancakes.rend());
		for(int i = 0; i+k-1 < n; i++) {
			double partial = pancakes[i].first*pancakes[i].first*pi + 2*pi*pancakes[i].first*pancakes[i].second;
			vector<double> hs;
			for(int j = i+1; j < n; j++) {
				hs.push_back(2*pi*pancakes[j].first*pancakes[j].second);
			}
			sort(hs.rbegin(), hs.rend());
			for(int j = 0; j<k-1; j++) {
				partial += hs[j];
			} 
			maximum = max(maximum, partial);
		}
		
		printf("Case #%d: %.7f\n", test, maximum);
		
	}
	return 0;
}


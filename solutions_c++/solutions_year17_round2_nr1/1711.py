#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <string>
#include  <cstring>
#include <cstdlib>

using namespace std;

#define EPS 1e-9

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int test = 1; test<=t; test++) {
		vector<pair<double, int> > horses;
		double d;
		int n;
		scanf("%lf %d", &d, &n);
		for(int i = 0; i<n; i++) {
			double x;
			int s;
			scanf("%lf %d", &x, &s);
			horses.push_back({ x, s });
		}
		double time = 0;
		sort(horses.begin(), horses.end());
		while(horses.size()) {
			double minimum = 2000000000;
			int idxToDelete = 0;
			for(int i = 0; i<horses.size(); i++) {
				if(i == (int)horses.size()-1) {
					if(minimum > (d-horses[i].first)/horses[i].second+EPS) {
						minimum = (d-horses[i].first)/horses[i].second;
						idxToDelete = i;
					}
					minimum = min(minimum, (d-horses[i].first)/horses[i].second);
				} else {
					if(horses[i].second > horses[i+1].second) {
						if(minimum > (horses[i+1].first-horses[i].first)/(horses[i].second-horses[i+1].second) + EPS) {
							minimum = min(minimum, (horses[i+1].first-horses[i].first)/(horses[i].second-horses[i+1].second));
							idxToDelete = i;
						}
					}
				}
			}
			for(int i = 0; i<horses.size(); i++) {
				horses[i].first += minimum*horses[i].second;
			}
			time += minimum;
			horses.erase(horses.begin()+idxToDelete);
		}
		printf("Case #%d: %.7lf\n", test, d/time);
	}
	return 0;
}

#include <cstdio>
#include <iostream>
#include <memory.h>
#include <queue>
#include <stack>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>

#define pi acos(-1)

using namespace std;

int main() {
	int T;
	scanf("%d",&T);
	for (int tc = 1; tc <= T; tc++) {
		int N,K;
		scanf("%d %d",&N,&K);
		pair<double,double> pancake[1005];
		for (int i = 0; i < N; i++) {
			double r,h;
			scanf("%lf %lf",&r,&h);
			pancake[i].first = pi*r*r;
			pancake[i].second = 2.0*pi*r*h;
		}
		sort(pancake, pancake + N);
		double res = 0;
		for (int i = N-1; i >= K-1; i--) {
			int maxR = pancake[i].first;
			vector<double> temp;
			for (int j = i-1; j >= 0; j--) {
				temp.push_back(pancake[j].second);
			}
			sort(temp.begin(),temp.end());
			double totalAreaH = pancake[i].second;
			int a = temp.size() - 1;
			int b = temp.size() - K;
			for (int j = a; j > b; j--) {
				totalAreaH += temp[j];
			}
			res = max(res, pancake[i].first + totalAreaH);
		}
		printf("Case #%d: %.9lf\n", tc, res);
	}
	return 0;
}
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstdio>
struct horse{
	double dist, speed;
};
horse a[1000000];
bool cmp(horse a, horse b){
	return a.dist > b.dist;
}
using namespace std;
int main(){
	int t;
	cin >> t;
	for (int z = 1; z <= t; z++){
		double d;
		int n;
		cin >> d >> n;
		for (int i = 1; i <= n; i++)
			cin >> a[i].dist >> a[i].speed;
		sort(a + 1, a + 1 + n, cmp);
		double atime = (d - a[1].dist) / a[1].speed;
		for (int i = 2; i <= n; i++)
			atime = max(atime, (d - a[i].dist) / a[i].speed);
		printf("Case #%d: %.6f\n", z, d / atime);
	}
	return 0;
}
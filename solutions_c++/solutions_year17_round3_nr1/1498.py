#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstdio>
using namespace std;
struct cake{
	double r, h;
};
cake a[1000001], b[1000001];
const double pi = 3.1415926535897932384626;
bool cmp(cake x, cake y){
	return (x.r * x.h) > (y.r * y.h);
}
int main(){
	int t;
	cin >> t;
	for (int z = 1; z <= t; z++){
		int n, k;
		cin >> n >> k;
		int index;
		for (int i = 1; i <= n; i++)
			cin >> a[i].r >> a[i].h;
		double max = 0;
		for (int i = 1; i <= n; i++){
			for (int j = 1; j <= n; j++){
				b[j].r = a[j].r;
				b[j].h = a[j].h;
			}
			sort(b, b + 1 + n, cmp);
			bool equal = false;
			int count = 0;
			double ans = pi * a[i].r * (a[i].r + 2 * a[i].h);
			for (int j = 1; j <= n; j++){
				if (count == k - 1) break;
				if (b[j].r > a[i].r) continue;
				if (b[j].r == a[i].r){
					if (b[j].h == a[i].h){
						if (!equal){
							equal = true;
							continue;
						}
					}
				}
				count++;
				ans += 2 * pi * b[j].h * b[j].r;
			}
			if ((count == k - 1) && (ans > max)) max = ans;
		}
		printf("Case #%d: %.9f\n", z, max);
	}
	return 0;
}
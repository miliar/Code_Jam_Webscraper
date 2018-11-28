#include <bits/stdc++.h>

using namespace std;

typedef struct {
	int index;
	long double r;
	long double h;
	long double sidearea;
	//long double toparea;
} pancake;

bool larger (pancake a, pancake b) {
	return (a.r > b.r) || (a.r == b.r && a.h > b.h);
}

bool largersidearea (pancake a, pancake b) {
	return (a.sidearea > b.sidearea) || (a.sidearea == b.sidearea && a.r > b.r);
}

const long double PI = 3.14159265358979323846;

int main() {
	cout.precision(9);
	cout << fixed;
	int t;
	int n,k;
	cin >> t;
	for (int i = 1; i<=t; i++) {
		cin >> n >> k;
		pancake pancakes[n];
		pancake pancake2[n];
		for (int j = 0; j < n; j++) {
			pancakes[j].index = j;
			cin >> pancakes[j].r >> pancakes[j].h;
			pancakes[j].sidearea = 2 * PI * pancakes[j].r * pancakes[j].h;
			//pancakes[j].toparea = PI * pancakes[j].r * pancakes[j].r
			pancake2[j].index = j;
			pancake2[j].r =  pancakes[j].r;
			pancake2[j].h =  pancakes[j].h;
			pancake2[j].sidearea =  pancakes[j].sidearea;
		}
		//sort(pancakes,pancakes+n,larger);
		sort(pancake2,pancake2+n,largersidearea);
		long double kminusonearea = 0;
		long double rmax = 0;
		for (int j = 0; j < k-1; j++) {
			kminusonearea += pancake2[j].sidearea;
			if (pancake2[j].r > rmax) {
				rmax = pancake2[j].r;
			}
		}
		long double maxarea = 0;
		for (int j = k-1; j < n; j++) {
			long double temparea = kminusonearea;
			temparea += pancake2[j].sidearea;
			if (pancake2[j].r > rmax) {
				temparea += PI * pancake2[j].r * pancake2[j].r;
			} else {
				temparea += PI * rmax * rmax;
			}
			if (temparea > maxarea) {
				maxarea = temparea;
			}
		}

		cout << "Case #" << i << ": " << maxarea << endl;
	}
	return 0;
}
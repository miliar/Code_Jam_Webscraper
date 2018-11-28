#define _CRT_SECURE_NO_WARNINGS
#include <iostream> 
#include <vector>
#include <algorithm>
#include <map> 
#include <string>
#include <set> 
#include <iterator> 
#include <deque>
#include <iomanip>
#include <string> 
#include <math.h> 
#include <time.h>
#include <queue> 
#include <stdio.h>
#include <valarray>
#include <stack>
#include <cstdio>

#define mp(x, y) make_pair(x, y)
#define all(x) x.begin(), x.end() 
#define det(a, b, c, d) a*d - b*c

typedef long long ll;

using namespace std;

int main() {
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		double d;
		int n;
		cin >> d >> n;
		vector<pair<double, double> > h(n);
		for (int i = 0; i < n; i++) {
			cin >> h[i].first >> h[i].second;
		}
		sort(all(h));
		double time = 0;
		for (int j = 0; j < n; j++) {
			double tmp = 0;
			double speed = h[j].second;
			double start = h[j].first;
			for (int k = j + 1; k < n; k++) {
				auto val = (h[k].first - start) / (speed - h[k].second);
				if (val > 0 && (start + val*speed) < d) {
					start += speed*val;
					speed = h[k].second;
					tmp += val;
				}
			}
			tmp += (d - start) / speed;
			time = max(time, tmp);
		}
		cout <<fixed << setprecision(6) << "Case #" << i << ": " <<  d / time << endl;
	}
	return 0;
}
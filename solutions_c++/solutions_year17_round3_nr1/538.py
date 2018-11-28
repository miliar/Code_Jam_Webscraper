#include <iostream>
#include <queue>
#include <algorithm>
#include <math.h>

using namespace std;

using num = long double;

num getside(num r, num h) {
	return 2*r*h*M_PIl;
}

num getbig(num r, num h) {
	return getside(r, h) + r*r*M_PIl;
}

int main() {
	int cases;
	cin >> cases;
	for (int casei=1; casei<=cases; casei++) {
		int n, k;
		cin >> n >> k;
		pair<num, num> arr[n];
		for (auto& p : arr) cin >> p.first >> p.second;
		sort(arr, arr+n);
		num sum=0;
		num best=0;
		priority_queue<num, vector<num>, greater<num>> q;
		for (auto p : arr) {
			num r=p.first, h=p.second;
			while (q.size() >= k) {
				sum -= q.top();
				q.pop();
			}
			best = max(best, getbig(r, h) + sum);
			num x = getside(r, h);
			sum += x;
			q.push(x);
		}
		cout.precision(17);
		cout << "Case #" << casei << ": " << best << endl;
	}
}

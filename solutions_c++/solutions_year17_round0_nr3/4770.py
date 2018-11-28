#include <queue>
#include <iostream>

using namespace std;

int main() {

	int T, k, n;
	cin >> T;

	for(int i=1; i<=T; i++) {
		cin >> n >> k;
		
		priority_queue<int> q;
		q.push(n);

		int dist, left, right;
		for (int i=0; i<k; i++) {
			int x = q.top(); q.pop();
			left = (x - 1) / 2;
			right = x - 1 - left;
			dist = min(left, right);
			if (right > 0) q.push(right);
			if (left > 0) q.push(left);
		}

		cout << "Case #" << i << ": " << right << " " << left << endl;
	}
}
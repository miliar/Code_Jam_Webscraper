#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <list>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <bitset>

#define ull unsigned long long
#define ll long long

using namespace std;

int main() {
	//freopen("stdin.inp", "r", stdin);
	//freopen("stdout.out", "w", stdout);

	int t;
	ull n;
	ll k;
	int count = 0;
	cin >> t;

	priority_queue<pair<ull, ull>, vector<pair<ull, ull>>> pq;
	ull x, y;
	ull max, min;

	while (t--) {
		++count;
		while (!pq.empty()) {
			pq.pop();
		}

		cin >> n >> k;

		pq.push(pair<int, int>(n, 1));
		while (k > 0) {
			x = pq.top().first;
			y = pq.top().second;
			pq.pop();

			k -= y;
			max = x >> 1;
			if (x % 2 == 0) {
				min = max - 1;
				pq.push(pair<ull, ull>(min, y));
			}
			else {
				min = max;
				y *= 2;
			}
			if (!pq.empty()) {
				if (pq.top().first == max) {
					y += pq.top().second;
					pq.pop();
				}
			}
			pq.push(pair<ull, ull>(max, y));

		}
		cout << "Case #" << count << ": " << max << " " << min << endl;
	}
	return 0;
}
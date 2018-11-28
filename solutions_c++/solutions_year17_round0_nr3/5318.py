#include <iostream>
#include <queue>
using namespace std;

int main()
{
	int t_no;
	cin >> t_no;

	for (int t = 1; t <= t_no; ++t) {
		int n, k;
		cin >> n >> k;

		priority_queue<int> pq;
		pq.push(n);

		int mn, mx;
		for (int i = 0; i < k; ++i) {
			int cur = pq.top();
			pq.pop();

			if (cur % 2 == 1) {
				mn = (cur - 1) / 2;
				mx = (cur - 1) / 2;
			}
			else {
				mn = cur / 2 - 1;
				mx = cur / 2;
			}

			pq.push(mn);
			pq.push(mx);
		}


		cout << "Case #" << t << ": " << mx << ' ' << mn << '\n';
	}

	return 0;
}

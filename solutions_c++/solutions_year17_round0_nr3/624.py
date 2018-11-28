#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <queue>
using namespace std;

int main()
{
	int T; cin >> T;

	for (int t = 0; t < T; t++) {
		long long n, k; cin >> n >> k;
		long long cnt = 1;

		if (cnt >= k) {
			cout << "CASE #" << t + 1 << ": " << n / 2 << " " << (n-1) / 2 << endl;
			continue;
		}

		priority_queue<pair<long long, long long>>PQ;
		PQ.push(make_pair((n - 1) / 2, 1));
		PQ.push(make_pair(n / 2, 1));

		while (1) {
			pair<long long, long long>PI1 = PQ.top(); PQ.pop();
			pair<long long, long long>PI2 = PQ.top(); PQ.pop();
			//cout << PI1.first << endl;
			//cout << PI2.first << endl;
			cnt += PI1.second;
			if (cnt >= k) {
				cout << "CASE #" << t + 1 << ": " << PI1.first / 2 << " " << (PI1.first - 1) / 2 << endl;
				break;
			}

			cnt += PI2.second;
			if (cnt >= k) {
				cout << "CASE #" << t + 1 << ": " << PI2.first / 2 << " " << (PI2.first - 1) / 2 << endl;
				break;
			}

			pair<long long, long long>pi1 = make_pair(PI1.first / 2, 0), pi2 = make_pair((PI2.first - 1) / 2, 0);
			if (PI1.first % 2 == 0)pi1.second+=PI1.second, pi2.second+=PI1.second;
			else pi1.second += 2 * PI1.second;
			if (PI2.first % 2 == 0)pi1.second += PI2.second, pi2.second += PI2.second;
			else pi2.second += 2 * PI2.second;

			PQ.push(pi1); PQ.push(pi2);
		}
	}

    return 0;
}


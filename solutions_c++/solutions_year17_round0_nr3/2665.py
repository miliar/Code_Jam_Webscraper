#include <bits/stdc++.h>
using namespace std;

pair<long long, long long> getNext(long long n) {
	long long mid = n/2;
	return (n%2 == 0? make_pair(mid, mid-1) : make_pair(mid, mid));
}

int main() {

	freopen("C-large.in", "rt", stdin);
	freopen("C-large.out", "wt", stdout);

	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) { //test cases
		long long n, k;
		cin >> n >> k;

		map<long long, long long> mp;
		mp.insert(make_pair(n, 1));
		long long count = 0LL;

		while(!mp.empty()) {
			//max value of map
			map<long long, long long>::reverse_iterator it = mp.rbegin();
			long long key = it->first;
			long long value = it->second;

			//next values
			pair<long long, long long> next = getNext(key);

			count += value;
			if(count >= k) {
				cout << "Case #" << t << ": " << next.first << ' '
						<< next.second << '\n';
				break;
			}

			mp[next.first] += value;
			mp[next.second] += value;
			mp.erase(key);
		}

	}

	return 0;
}

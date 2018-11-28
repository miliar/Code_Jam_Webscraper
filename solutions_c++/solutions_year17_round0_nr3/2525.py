#include <bits/stdc++.h>

using namespace std;

int main(int argc, char** argv) {

	ifstream in("../data/c_large.in");
	ofstream out("../data/c_large.out");

	int T;  // cases
	in >> T;
	for (int z = 1; z <= T; z++) {

		long long n, k;
		in >> n >> k;

		long long maxDist, minDist;
		map<long long, long long> intervals;
		intervals[n] = 1;

		long long power = 1;

		while (k > power) {
			map<long long, long long> newIntervals;
			// cout << k << '\t' << power << '\t';
			for (auto it = intervals.begin(); it != intervals.end(); it++) {
				// cout << it->first << '-' << it->second << '\t';
				long long l = it->first - 1;
				long long c = it->second;
				long long l1 = l / 2;
				long long l2 = (l + 1) / 2;
				if (newIntervals.count(l1) == 0)
					newIntervals[l1] = 0;
				newIntervals[l1] += c;
				if (newIntervals.count(l2) == 0)
					newIntervals[l2] = 0;
				newIntervals[l2] += c;
			}
			// cout << '\n';
			intervals = newIntervals;
			k -= power;
			power *= 2;
		}

		// cout << k << '\t';
		for (auto it = intervals.rbegin(); it != intervals.rend(); it++) {
			// cout << it->first << '-' << it->second << '\t';
			long long c = it->second;
			if (k > c)
				k -= c;
			else {
				long long l = it->first - 1;
				minDist = l / 2;
				maxDist = (l + 1) / 2;
				break;
			}
		}
		// cout << '\n';

		out << "Case #" << z << ": ";
		// print the result
		out << maxDist << ' ' << minDist;
		out << endl;

	}

	in.close();
	out.close();
	
	return 0;
}
#include <iostream>
#include <sstream>
#include <map>

using namespace std;


int main() {
	int T=1;
	cin >> T;
	int t = 0;
	while (++t <= T) {
		long long int n = 5;
		long long int k = 2;
		cin >> n >> k;

		map<long long int, long long int> range;
		range[n]=1;

		int maxl, minl;
		while (--k >= 0) {
			long long int len = range.rbegin()->first;
			if (range.rbegin()->second == 1)
				range.erase(len);
			else
				range.rbegin()->second--;

			minl = (len - 1) / 2;
			if (len % 2 == 0) {
				maxl = minl + 1;
				range[maxl]++;
				range[minl]++;

			}
			else {
				maxl = minl;
				range[minl]+=2;
			}
		}



		cout << "Case #" << t << ": " << maxl << " " << minl << endl;
	}
	return 0;
}
#include <iostream>
#include <string>

using namespace std;

int main() {

	int testcase;
	cin >> testcase;

	for (int i = 1; i <= testcase; i++) {

		long long people_number;
		long long stall_number;
		cin >> stall_number;
		cin >> people_number;
		int min;
		int max;

		bool * stalls = new bool[stall_number + 2];
		for (int k = 0; k <= stall_number+1; k++) {
			if (k == 0 || k == stall_number + 1) {
				stalls[k] = true;
			}
			else {
				stalls[k] = false;
			}
		}

		for (int j = 1; j <= people_number; j++) {

			int max_interval = 0;
			int finish = 0;
			int temp = 0;
			for (int k = 0; k <= stall_number + 1; k++) {
				if (stalls[k] == false) {
					temp++;
				}
				else {
					if (temp > max_interval) {
						max_interval = temp;
						finish = k;
					}
					temp = 0;
				}
			}

			int last = finish - 1;
			int first = finish - max_interval;
			int ort = (last + first) / 2;

			stalls[ort] = true;

			if (j == people_number) {
				min = ort - first;
				max = last - ort;
			}
		}

		cout << "Case #" << i << ": " << max << " " << min << endl;

	}

	return 0;
}
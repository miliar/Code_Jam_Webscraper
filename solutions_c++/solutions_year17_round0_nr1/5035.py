#include <iostream>
#include <vector>

using namespace std;

#define FLIP(x) (((x) == '+') ? '-' : '+')

int main() {
	int T, t;
	cin >> t; T = t;
	while (t--) {
		string pc; int k;
		cin >> pc; cin >> k;

		int sz = pc.size(); int flips = 0;
		int i = 0; int flag = 0; int j;
		while (i < sz) {
			if (pc[i] == '+') {
				i++;
				continue;
			}
			// encounter a '-'
			
			// impossible
			if (i + k > sz) {
				flag = 1;
				break;
			}

			// Flip k pancakes
			j = 0;
			while (j < k) {
				pc[i + j] = FLIP(pc[i + j]);
				j++;
			}
			flips++;
			i++;
		}

		if (flag)
			cout << "Case #" << T - t << ": " << "IMPOSSIBLE" << "\n";
		else 
			cout << "Case #" << T - t << ": " << flips << "\n";

	}
	return 0;
}
#include<iostream>
#include<algorithm>
#include<math.h>
#include<string>
#include<map>
using namespace std;
int main() {
	int NoOfTestCases;
	cin >> NoOfTestCases;
	for (int k = 0; k < NoOfTestCases; k++) {
		long long int N, K;
		cin >> N >> K;
		long long int CurrNo = 0;
		long long int mapper[10][2];
		long long int x, y;
		for (int i = 0; i < 10; i++)
			for (int j = 0; j < 2; j++)
				mapper[i][j] = 0;
		// Logic starts here
		mapper[0][0] = N;
		mapper[0][1] = 1;
		while (CurrNo < K) {
			// Find and Break the max value
			long long int maxvalue = 0, index;
			for (int i = 0; i < 10; i++) {
				if (mapper[i][0] > maxvalue) {
					maxvalue = mapper[i][0];
					index = i;
				}
			}
			// Break the value and fill new positions
			if (maxvalue % 2 == 1) {
				x = y = maxvalue / 2;
			}
			else {
				y = maxvalue / 2;
				x = y - 1;
			}

			// Refill the mapper and counter
			CurrNo += mapper[index][1];
			int i, j;
			for (i = 0; i < 10; i++) {
				if (mapper[i][0] == x) {
					mapper[i][1] += mapper[index][1];
					break;
				}
			}
			// Find the first 0 in list
			if (i == 10)
				for (i = 0; i < 10; i++) {
					if (mapper[i][0] == 0) {
						mapper[i][0] = x;
						mapper[i][1] += mapper[index][1];
						break;
					}
				}

			for (i = 0; i < 10; i++) {
				if (mapper[i][0] == y) {
					mapper[i][1] += mapper[index][1];
					break;
				}
			}
			// Find the first 0 in list
			if (i == 10)
				for (i = 0; i < 10; i++) {
					if (mapper[i][0] == 0) {
						mapper[i][0] = y;
						mapper[i][1] += mapper[index][1];
						break;
					}
				}
			mapper[index][0] = mapper[index][1] = 0;
		}
		cout << "Case #" << k + 1 << ": " << max(x,y) << " " << min(x,y)<< endl;
	}
	return 0;
}
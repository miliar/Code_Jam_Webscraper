#include <iostream>
#include <vector>

using namespace std;

int main() {
	unsigned long long int T, N;
	cin >> T;
	for(unsigned long long int ix = 1; ix <= T; ix++) {
		vector<int> arr;
		cin >> N;
		if(N < 10) {
			cout << "Case #" << ix << ": " << N << endl;
			continue;
		}

		while(N > 0) {
			arr.push_back(N % 10);
			N /= 10;
		}

		for(long long int iy = 0; iy < arr.size()-1; iy++) {
			if(arr[iy] < arr[iy+1]) {
					arr[iy+1]--;
					for(int long long iz = iy; iz >= 0; iz--)
						arr[iz] = 9;
			}
		}

		cout << "Case #" << ix << ": ";
		bool left = true;
		for(long long int iy = arr.size()-1; iy >= 0; iy--) {
			if(left && arr[iy] == 0)
				continue;

			cout << arr[iy];
			left = false;
		}
		cout << endl;
	}

	return 0;
}

// Case #1: 129
// Case #2: 999
// Case #3: 7
// Case #4: 99999999999999999

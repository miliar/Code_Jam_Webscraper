#include <iostream>
#define ll long long int
using namespace std;

ll tenpow(ll x) {
	if (x == 0) {return 1;}
	else {return 10 * tenpow(x-1);}
}

int main() {
	int T;
	cin >> T;
	for(int z = 0; z < T; z++) {
		int arr[19];
		ll answer = 0;
		for(int i = 0; i < 19; i++) {
			arr[i] = 0;
		}
		ll number;
		cin >> number;
		for(int i = 18; i >= 0; i--) {
			arr[i] = number % 10;
			number /= 10;
		}

		for(int i = 17; i >= 0; i--) {
			if(arr[i] > arr[i+1]) {
				arr[i]--;
				for(int j = i+1; j < 19; j++) {
					arr[j] = 9;
				}
			}
		}
		for(int i = 0; i < 19; i++) {
			answer += arr[i] * tenpow(18-i);
		}

		cout << "Case #" << z+1 << ": " << answer << endl;

	}
}
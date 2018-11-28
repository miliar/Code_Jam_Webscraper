#include <iostream>

using namespace std;

int main(int argc, char const *argv[]) {
	
	int T;
	string K;
	
	cin >> T;

	for (int k = 1; k <= T; ++k) {
		cin >> K;
		cout << "Case #" << k << ": ";

		int i;
		int first = -1;
		bool less = false;
		for (i = 0; i < K.length()-1; ++i) {
			if(first == -1 && K[i+1] <= K[i]) {
				first = i+1;
			}
			if(K[i+1] < K[i]) {
				less = true;
				break;
			}
		}

		if(less) {
			
			for (i = first; i < K.length(); ++i) {
				K[i] = '9';
			}

			K[first-1] -= 1;
		}

		if(K[0] == '0') {
			cout << K.substr(1) << endl;
		} else {
			cout << K << endl;
		}
	}

	return 0;
}
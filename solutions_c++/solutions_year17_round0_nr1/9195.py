#include <iostream>

using namespace std;

int min_flips(string pancakes, int K) {
	int flips = 0;
	for (int i = 0; i < pancakes.length(); i++) {
		if (pancakes[i] == '-') {
			if (i+K < pancakes.length()+1) {
				for (int j = i; j < K+i; j++) {
					if (pancakes[j] == '-') {
						pancakes[j] = '+';
					} else {
						pancakes[j] = '-';
					}
				}
				flips += 1;
			} else {
				return -1;
			}
		} 
	}	
	return flips;
}

int main() {
	int T, K;
	string pancakes;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cin >> pancakes >> K;
		int flips = min_flips(pancakes, K);
		string output = ((flips != -1) ? to_string(flips):"IMPOSSIBLE"); 
		cout << "Case #" << i << ": " << output << endl;
	}
	return 1;
}

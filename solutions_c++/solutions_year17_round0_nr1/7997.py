#include <iostream>

using namespace std;

int compute(bool f[], int l, int k) {
	int moves = 0;
	int i;
	for(i = 0; i<=l-k; ++i) {
		if(!f[i]) {
			moves++;
			for(int j = i+1; j<i+k; ++j) {
				f[j] = !f[j];
			}
		}
	}
	for(; i<l; ++i) {
		if(!f[i]) return -1;
	}
	return moves;
}

int main() {
	int cases; cin >> cases;
	for(int c = 0; c<cases; ++c) {
		string pancakes;
		int k;
		cin >> pancakes >> k;
		int l = pancakes.length();
		bool f[l];
		for(int i = 0; i<l; ++i) {
			f[i] = (pancakes[i] == '+');
		}
		int moves = compute(f, l, k);
		cout << "Case #" << c+1 << ": ";
		if(moves == -1) {
			cout << "IMPOSSIBLE";
		}
		else {
			cout << moves;
		}
	    cout << endl;
	}
}

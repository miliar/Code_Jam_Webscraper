#include <iostream>
using namespace std;

enum Color {re,ye,bl};

int main() {
    int ncase = 0;
    cin >> ncase;
    for (int round = 1; round <= ncase; ++round) {
		int n, r,o,y,g,b,v;
		cin >> n >> r >> o >> y >> g >> b >> v;
		Color max;
		int output[10];
		char outchar[10];
		if (r >= y && r >= b) {
			max = re;
			output[0] = r;
			output[1] = y;
			output[2] = b;
			outchar[0] = 'R';
			outchar[1] = 'Y';
			outchar[2] = 'B';
		} else if (y >= r && y >= b) {
			max = ye;
			output[0] = y;
			output[1] = r;
			output[2] = b;
			outchar[0] = 'Y';
			outchar[1] = 'R';
			outchar[2] = 'B';
		} else {
			max = bl;
			output[0] = b;
			output[1] = r;
			output[2] = y;
			outchar[0] = 'B';
			outchar[1] = 'R';
			outchar[2] = 'Y';
		}
		int overlap = 0;
		switch(max) {
			case re:
				overlap = (y+b) - r;
				break;
					
			case ye:
				overlap = (r+b) - y;
				break;
			case bl:
				overlap = (r+y) - b;
				break;
		}

		if (overlap < 0) {
			cout << "Case #" << round << ": IMPOSSIBLE" << endl;
			continue;
		}

        cout << "Case #" << round << ": ";

		for(int i = 0; i < output[0]; ++i) {
			cout << outchar[0];
			if (output[1] > 0){
				cout << outchar[1];
				output[1]--;
			} else if (output[2] > 0){
				cout << outchar[2];
				output[2]--;
			}
			if (overlap > 0) {
				cout << outchar[2];
				overlap--;
				output[2]--;
			}
		}

        cout << endl;
    }
    return 0;
}

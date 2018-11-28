#include <iostream>

using namespace std;
int main(){
	int numOfCases;
	cin >> numOfCases;
	for (int cases = 1; cases <= numOfCases; cases++){
		string pancake;
		int flipper;
		cin >> pancake;
		cin >> flipper;
		int count = 0;
		for (int i = 0; i < pancake.length(); i++) {
			if (pancake[i] == '-' && i + flipper - 1 < pancake.length()){
				for (int j = 0; j < flipper; j++){
					if (pancake[i + j] == '-') {
						pancake[i + j] = '+';
					} else {
						pancake[i + j] = '-';
					}
				}
				count ++;
			}
		}
		bool solved = true;
		for (int i = 0; i < flipper; i++) {
			if (pancake[pancake.length() - 1 - i] == '-'){
				solved = false;
			}
		}
		cout << "Case #" << cases << ": ";
		if (!solved) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			cout << count << endl;
		}
	}
	return 0;
}
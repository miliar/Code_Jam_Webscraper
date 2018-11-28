#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(int argc, char** argv) {
	int iRounds = 0;
	cin >> iRounds;
	string strInput;
	string strResult;

	for (int i = 0; i < iRounds; i++) {
		int iLen = 0;
		int iFallback = 0;
		cin >> strInput;
		iLen = strInput.length();
		iFallback = -1;
		// search if max is tidy
		for (int j = 0; j < iLen; j++) {
			if (iFallback >= 0) {
				strInput[j] = '9';
			} else if ((j+1) < iLen && strInput[j] > strInput[j+1]) {
				iFallback = j;
			}
		}
		if (iFallback == -1) {
			strResult = strInput;
		} else {
			// handle falling back
			for (int j = iFallback; j > 0; j--) {
				if ((strInput[j] - 1) >= strInput[j-1]) {
					iFallback = j;
					strInput[j] -= 1;
					break;
				} else {
					strInput[j] = '9';
					iFallback--;
				}
			}
			// boundary
			if (iFallback == 0) {
				strInput[0] -= 1;
			}
		}
		// output
		cout << "Case #" << i+1 << ": ";
		if (strInput[0] == '0') {
			// skip first 0, here only 1 leading zero is possible
			cout << strInput.c_str() + 1;
		} else {
			cout << strInput;
		}
		cout << endl;
	}
	return 0;
}

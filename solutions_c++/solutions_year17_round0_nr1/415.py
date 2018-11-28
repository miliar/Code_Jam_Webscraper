#include <iostream>
#include <string>
#include <vector>
using namespace std;

int flipping(const string&, const int);

int main(int argc, char** argv) {
	int iRounds = 0;
	int iFlipperSize = 0;
	int iFlipNum = 0;
	string strPans;
	cin >> iRounds;
	for (int i = 0; i < iRounds; i++) {
		cin >> strPans;
		cin >> iFlipperSize;
		iFlipNum = flipping(strPans, iFlipperSize);
		// output results
		cout << "Case #" << i + 1 << ": "; 
		if (iFlipNum < 0) {
			cout << "IMPOSSIBLE";
		} else {
			cout << iFlipNum;
		}
		cout << endl;
	}

	return 0;
}

int flipping(const string& strPan, const int iFlipperSize) {
	int iLen = strPan.length();
	int iCurFlip = 0;
	int iTotalFlip = 0;
	vector<int> flip(iLen, 0);
	for (int i = 0; i < iLen; i++) {
		int iHappy = (strPan[i] == '+');
		if (i > iLen - iFlipperSize) {
			// check feasibility
			if ((iHappy ^ iCurFlip) == 0) {
				return -1;
			}
		} else if ((iHappy ^ iCurFlip) == 0) {
			// do flipping
			// need flip here
			iTotalFlip += 1;
			flip[i] = 1;
			iCurFlip ^= 1;
		}
		// update current flip state
		if (i >= iFlipperSize - 1) {
			iCurFlip = iCurFlip ^ flip[i-iFlipperSize+1];
		}
	}
	return iTotalFlip;
}

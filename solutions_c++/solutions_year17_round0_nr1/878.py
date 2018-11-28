#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<bool> stringToVec(const string data) {
	vector<bool> v;
	for (char c : data)
		v.push_back(c == '-');
	return v;
}

void swapRegion(vector<bool> & pancake, int pos, int len) {
	for (int i = 0; i < len; i++)
		pancake[i + pos] = !pancake[i + pos];
}

int solveCase(const string dataString, int flipperSize) {
	auto pancake = stringToVec(dataString);
	int flips = 0;

	for (int i=0;i<=pancake.size() - flipperSize;i++) {
		if (pancake[i]) {
			swapRegion(pancake, i, flipperSize);
			++flips;
		}
	}

	bool failed = false;
	for (int i=0;i<pancake.size();i++) {
		if (pancake[i]) {
			failed = true;
			break;
		}
	}

	if (failed)
		return -1;
	return flips;
		 


	
}

void main() {
	int cases;
	cin >> cases;

	for (int i=0;i<cases;i++) {
		string caseData;
		int pancakeFlipper;
		cin >> caseData >> pancakeFlipper;
		int solution = solveCase(caseData, pancakeFlipper);
		cout << "Case #" << i + 1 << ": ";
		if (solution == -1)
			cout << "IMPOSSIBLE";
		else
			cout << solution;
		cout << endl;
	}


	
	
}
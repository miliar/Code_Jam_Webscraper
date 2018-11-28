#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

vector<int> numToVector(long long n) {
	vector<int> digitVector;
	while (n) {
		digitVector.push_back(n % 10);
		n /= 10;
	}
	return digitVector;
}

long long vectorToNum(vector<int>& digitVector) {
	long long i = 1;
	long long n = 0;
	for (const int& d : digitVector) {
		n += d*i;
		i *= 10;
	}
	return n;
}

void changeDigit(int i, vector<int>& digitVector) {
	bool hasCarry = true;
	digitVector[i] = 9;
	while (hasCarry) {
		++i;
		if (digitVector[i] != 0) {
			hasCarry = false;
			--digitVector[i];
		}
		else digitVector[i] = 9;
	}
}

bool isTidy(vector<int>& digitVector) {
	bool isTidy = true;
	for (unsigned i = 0; i < digitVector.size() - 1; ++i) {
		if (digitVector[i] < digitVector[i + 1]) isTidy = false;
	}
	return isTidy;
}

void makeTidy(vector<int>& digitVector) {
	int i = 0;
	while (!isTidy(digitVector)) {
		changeDigit(i, digitVector);
		++i;
	}
}

long long tidyUpToN(long long N) {
	vector<int> digitVector = numToVector(N);
	makeTidy(digitVector);
	return vectorToNum(digitVector);
}

int main() {
	long long n;
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cin >> n;
		cout << "case #" << i << ": ";
		cout << tidyUpToN(n) << '\n';
	}
}
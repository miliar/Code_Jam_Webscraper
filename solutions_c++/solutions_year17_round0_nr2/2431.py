#include <algorithm>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#define SREP(s,i,m) for(unsigned int i = s; i < m; ++i)
#define REP(i,m) SREP(0,i,m)

using namespace std;

#ifdef _MSC_VER
using LONG = __int64;
using ULONG = unsigned __int64;
#else
using LONG = long long int;
using ULONG = unsigned long long int;
#endif

bool isTidy(string num) {
	int lastDigit = 0;
	for (int i = 0; i < num.size(); i++) {
		int digit = num[i] - '0';
		if (lastDigit > digit) return false;
		lastDigit = digit;
	}
	return true;
}

int getDigits(int num) {
	int digits = 0;
	do {
		num /= 10; digits++;
	} while (num != 0);
	return digits;
}

bool isTidy(int num) {
	int lastDigit = 9;
	int digits = getDigits(num);
	int divider = 1;
	for (int i = 0; i < digits; i++) {
		int digit = (num / divider) % 10;
		if (digit > lastDigit) return false;
		lastDigit = digit;
		divider *= 10;
	}
	return true;
}

string getGreatestTidiy(string numStr, int width) {
	stringstream ss(numStr);
	int num;  ss >> num;
	int lastTidiy;
	for (int i = 1; i <= num; i++) {
		if (isTidy(i)) lastTidiy = i;
	}
	ostringstream os;
	os << setfill('0') << setw(width) << lastTidiy;
	return os.str();
}

void solve(string num) {
	for (int i = 0; i < num.size() - 1; i++) {
		string substr = num.substr(i, 2);
		if (!isTidy(substr)) {
			string replacer = getGreatestTidiy(substr, 2);
			num.replace(i, 2, replacer);
			for (int j = i + 2; j < num.size(); j++) {
				num[j] = '9';
			}
			i = -1;
			continue;
		}
	}
	for (int i = 0; i < num.size(); i++) {
		if (num[i] != '0') break;
		num.erase(i, 1);
	}
	cout << num << endl;
}

int main(void) {
	int T;
	cin >> T;
	REP(i, T) {
		string num;
		cin >> num;
		cout << "Case #" << (i + 1) << ": ";
		solve(num);
	}
	return 0;
}
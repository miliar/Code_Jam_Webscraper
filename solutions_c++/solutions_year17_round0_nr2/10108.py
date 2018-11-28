#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

template<class I>
void find(I& i) {
	bool found = false;
	while (!found) {
		bool tidy = true;
		ostringstream oss;
		oss << i;
		string num = oss.str();
		for (int p = 0; p < num.size() - 1; ++p) {
			if (num[p] > num[p + 1]) {
				tidy = false;
				break;
			}
		}
		if (tidy) { found = true; }
		else { --i; }
	}
}

int main(int argc, char const *argv[])
{
	int T;
	cin >> T;
	unsigned int number;
	for (int c = 0; c < T; ++c) {
		cin >> number;
		find<unsigned int>(number);
		cout << "Case #" << c + 1 << ": " << number << endl;
	}
	return 0;
}

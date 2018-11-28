// CodeJam.cpp : Defines the entry point for the console application.
//
#include <iostream>
#include <string>

using namespace std;

struct opt {
	unsigned __int64 size = 0;
	unsigned __int64 count = 0;
};

void updateOpt(opt & current, opt & newOpt1, opt & newOpt2){
	unsigned __int64 newSize = current.size - 1;
	if (newSize % 2 == 0) {
		auto checkSize = newSize / 2;
		if (newOpt1.size == 0 || newOpt1.size == checkSize) {
			newOpt1.size = checkSize;
			newOpt1.count += current.count * 2;
		}
		else {
			newOpt2.size = checkSize;
			newOpt2.count += current.count * 2;
		}
	}
	else {
		newOpt1.size = current.size / 2;
		newOpt1.count += current.count;
		newOpt2.size = (current.size - 2) / 2;
		newOpt2.count += current.count;
	}
}

int main()
{
	int t;
	unsigned __int64 n, k, index;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		cin >> n >> k;

		index = 1;
		opt opt1, opt2;
		opt1.size = n;
		opt1.count = 1;
		while (index < k) {
			k = k - index;
			index *= 2;
			opt newOpt1, newOpt2;
			updateOpt(opt1, newOpt1, newOpt2);
			if (opt2.count != 0) {
				updateOpt(opt2, newOpt1, newOpt2);
			}
			opt1 = newOpt1;
			opt2 = newOpt2;
		}
		unsigned __int64 size1, size2;
		if (k > opt1.count) {
			unsigned __int64 newSize = opt2.size - 1;
			if (newSize % 2 == 0) {
				size1 = newSize / 2;
				size2 = size1;
			}
			else {
				size1 = opt2.size / 2;
				size2 = (opt2.size - 2) / 2;
			}
		}
		else {
			unsigned __int64 newSize = opt1.size - 1;
			if (newSize % 2 == 0) {
				size1 = newSize / 2;
				size2 = size1;
			}
			else {
				size1 = opt1.size / 2;
				size2 = (opt1.size - 2) / 2;
			}
		}

		cout << "Case #" << i << ": " << size1 << " " << size2 << endl;
	}
	//cin >> t;
	return 0;
}
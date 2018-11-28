#include "stdafx.h"
#include <string>
#include <iostream>

std::string tidy(std::string n) {
	for (auto k = 1; k < n.length(); ++k) {
		if (n[k - 1] > n[k]) {
			n[k - 1] = n[k - 1] - 1;
			for (auto i = k; i < n.length(); ++i) {
				n[i] = '9';
			}
			return tidy(n);
		}		
	}
	n.erase(0, n.find_first_not_of('0'));
	return n;
}

int main()
{
		
		int count = 0;
		std::cin >> count;
		for (auto k = 0; k < count; ++k) {
			std::string N;
			std::cin >> N;
			std::cout << "Case #" << (k + 1) << ": " << tidy(N) << std::endl;
		}		
    return 0;
}


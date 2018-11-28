#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>

using namespace std;

char flip(char c) {
	switch (c) {
		case '+': return '-';
		case '-': return '+';
		default: throw std::string("Invalid character flipped ") + std::string(c, 1);
	}
}
int main() {
	
	int T;
	
	cin >> T;
	
	for (int i = 0; i < T; i++) {
		std::string pancake;
		size_t k;
		cin >> pancake >> k;
		
		std::cout << "Case #" << i+1 << ": ";
		try {
			int count = 0;
			for (size_t j = 0; j < pancake.size(); j++) {
				if (pancake[j] == '-') {
					count++;
					for (size_t m = 0; m < k; m++) {
						if (j+m < pancake.size()) {
							pancake[j+m] = flip(pancake[j+m]);
						} else {
							throw std::string("IMPOSSIBLE");
						}
					}
				}
				
			}
			std::cout << count;
		} catch (const std::string& e) {
			std::cout << e;
		}
		std::cout << std::endl;
	}
	
	return 0;
}
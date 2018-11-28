#include <iostream>
#include <string>

void solve() {
	std::string row, number;
	std::cin >> row;
	number = row;
	int len = row.size();
	
	if (len == 1) {
		std::cout << row;
		return;
	}
	
	char last = row[0];
	
	int dec_pos = 1;
	for (; dec_pos < len; ++dec_pos) {
		if (row[dec_pos] < last) {
			--dec_pos;
			break;
		}
		last = row[dec_pos];
	}
	
	if (dec_pos < len) {
		int i = dec_pos;
		while (i > 0 && row[i - 1] == row[dec_pos]) {
			--i;
		}
		
		--number[i];
		if (number[i] == '0') {
			number[i] = ' ';
		}
		for (i = i + 1; i < len; ++i) {
			number[i] = '9';
		}
				
	}
	std::cout << number;
	
	return;
}

int main() {
	int t;
	std::cin >> t;
	for (int i = 0; i < t; i++) {
		std::cout << "Case #" << i + 1 << ": ";
		solve();
		std::cout << std::endl;
	}
	return 0;
}

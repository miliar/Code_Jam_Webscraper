#include <iostream>
#include <fstream>
#include <string>

bool isTidy(long long N) {
	std::string number = std::to_string(N);
	for (int i = 0; i < number.size() - 1; i++) {
		if (number[i] > number[i + 1]) return false;
	}
	return true;
}

std::string makeTidy(std::string number) {
	if (number.size() == 1) return number;
	if (number[0] > number[1]) {
		number[0]--;
		std::string buff;
		buff.resize(number.size() - 1, '9');
		return number[0] + makeTidy(buff);
	} 
	return number[0] + makeTidy(number.substr(1));
}

long long getTidy(long long N) {
	while (!isTidy(N)) {
		N = std::stoll(makeTidy(std::to_string(N)));
	}
	return N;
}

int main() {
	int T;
	std::ifstream file_in("tidy_numbers.txt");
	std::ofstream file_out("tidy_numbers_result.txt");
	file_in >> T;
	for (long long i = 0; i < T; i++) {
		long long N;
		file_in >> N;
		file_out << "Case #" << i + 1 << ": " << getTidy(N) << std::endl;
	}
	return 0;
}
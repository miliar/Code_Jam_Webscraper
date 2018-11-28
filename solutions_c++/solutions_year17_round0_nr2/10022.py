#include <iostream>
#include <fstream>
#include <string>

bool is_tidy(long long n) {
	int old = n % 10;
	
	while (n != 0) {
		n = n / 10;
		
		if (n % 10 > old)
			return false;
		
		old = n % 10;
	}

	return true;
}

long long tidy_number(long long index) {
	long long i;
	
	for (i = index; i >= 0; i--) {
		if (is_tidy(i)) {
			return i;
		}
	}
	
	return i;
}

int main() {
	std::string name = "B-small-attempt2";
	std::ifstream fin(name + ".in");
	std::ofstream fout(name + ".out");

	if (!fin.is_open() || !fout.is_open())
		return - 2;

	int N; fin >> N;
	long long index;

	for (int i = 1; i <= N; i++) {
		fin >> index;
		fout << "Case #" << i << ": " << tidy_number(index);
		if (i != N)	fout << std::endl;
	}

	return 0;
}
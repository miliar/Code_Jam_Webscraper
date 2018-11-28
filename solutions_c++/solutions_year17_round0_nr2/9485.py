#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>
#include <string>
#include <algorithm>    // std::sort
#include <vector>       // std::vector
#include <map>
#include <stdlib.h>
#include <sstream>

#define HAPPY 1
#define BLANK 2
int S[1001] = {0};
std::string str;


/*
 * ---+-++-
 * ++++-++-
 * +++++---
 *
 * */
bool check_descending_digits(int N) {
	int digit, old_d;
	old_d = N % 10;
	N = N / 10;
	while ((N / 10) != 0) {
		digit = N % 10;
		if (digit > old_d) {
		    //std::cout << "false"<< std::endl;
			return false;
		}
		old_d = digit;
		std::cout << digit << " ";
		N = N / 10;
	}
	std::cout << std::endl;
	digit = N % 10;
	if (digit > old_d) {
		//std::cout << "false"<< std::endl;
		return false;
	}
	//std::cout << digit << std::endl;
	//std::cout << "true"<< std::endl;
	return true;
}

void print(int* arr, int size) {
	for (int i = 0; i < size; i++) {
		if (arr[i] == HAPPY) {
			std::cout << "+";
		} else
			std::cout << "-";
	}
	std::cout << std::endl;
}

void flip(int index, int*arr, int k) {
	for (int i = index;i < index + k ;i++) {
		if (arr[i] == HAPPY)
			arr[i] = BLANK;
		else if (arr[i] == BLANK)
			arr[i] = HAPPY;
	}
}


int resolve(int* arr, int k, int size) {
	int index = 0;
	int flips = 0;
	while (arr[index] == HAPPY) index++;
	if (arr[index] == 0) {
		return flips;
	}
	while (index < size) {
		//std::cout << "index: " << index << std::endl;
		std::cout << "index: " << index << std::endl;
		print(arr, size);
		if ((size - index) < k) {
			return -1;
		}
		flip(index, arr, k);
		flips++;
		while (arr[index] == HAPPY) index++;
	}
	//std::cout << "end:\n";
	print(arr, size);
	return flips;
}
/*
int main() {
	int T, t, index, k, size;
	char c = 0;
	std::ifstream fin("A-large.in");
	std::ofstream fout("A-large.out");

	fin >> T;
	for (t = 1; t <= T; t++) {
		std::cout << "**************\n";
		index = 0;
		fin.get(c);
		fin.get(c);
		//std::cout << c;
		while (c != ' ') {
			if (c == '-') {
				S[index++] = BLANK;
			} else {
				S[index++] = HAPPY;
			}
			size++;
			fin.get(c);
		}
		fin >> k;
		char c_k[33];
		int result = resolve(S, k, size);
		//std::cout << result << std::endl;
		fout << "Case #" << t << ": ";
		if (result == -1) {
			fout << "IMPOSSIBLE\n";
		} else {
			fout << itoa(result, c_k, 10) << std::endl;
		}
		for (int i =0; i < 1001; i++)
			S[i] = 0;
		size = 0;
	}
}
*/

int main() {
	std::ifstream fin("B-small-attempt0.in");

	std::ofstream fout("B-small-attempt0.out");

	int T;
	unsigned int N;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		fin >> N;
		std::cout << "N = " << N << std::endl;
		while (N > 0) {
			if (check_descending_digits(N)) {
				break;
			}
			N -= 1;
		}

		fout << "Case #" << t << ": " << N << std::endl;
	}

}

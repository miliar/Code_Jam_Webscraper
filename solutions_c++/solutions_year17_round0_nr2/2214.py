// Code Jam.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <fstream>
#include <string>
#include <vector>
using namespace std;

long long Rectify(long long N)
{
	vector<char> ls;
	ls.reserve(20);
	bool rectify = false;
	auto NN = N;
	while (NN) {
		char curr_digit = NN % 10;
		ls.push_back(curr_digit);
		NN /= 10;
	}
	for (int i = 0; i < ls.size() - 1; ++i) {
		if (ls[i] < ls[i + 1]) {
			rectify = true;
			ls[i + 1] -= 1;
			for (int j = 0; j <= i; ++j) {
				ls[j] = 9;
			}
		}
	}
	if (!rectify) return N;
	long long ret = ls[ls.size() - 1];
	for (int i = ls.size() - 2; i >= 0; --i) {
		ret *= 10;
		ret += ls[i];
	}
	return ret;
}

void TidyNumbers(string input_file_name, string output_fina_name)
{
#ifndef WIN32
#define _atoi64(val)     strtoll(val, NULL, 10)
#endif
	ifstream ifs(input_file_name, ios::in);
	ofstream ofs(output_fina_name, ios::out);
	if (!ifs.is_open() || !ofs.is_open()) return;
	long long N = 0;
	int case_count = 0;
	const char max_length = 20;
	char buff[max_length] = { 0 };
	ifs.getline(buff, max_length);
	case_count = _atoi64(buff);
	if (case_count <= 0) return;
	int i = 0;
	while (!ifs.eof()) {
		ifs.getline(buff, max_length);
		N = _atoi64(buff);
		if (N < 0) continue;
		long long result = 0;
		long long old_N = N;
		while (N) {
			long long NN = N;
			bool pass = true;
			while (NN) {
				char current_digit = NN % 10;
				NN /= 10;
				char prev_digit = NN % 10;
				if (prev_digit > current_digit) {
					pass = false;
					break;
				}
			}
			if (pass) {
				result = N;
				break;
			}
			N = Rectify(N);
		}
		ofs << "Case #" << i + 1 << ": " << result << endl;
		printf("%lld, %lld\n", old_N, result);
		if (++i == case_count) {
			break;
		}
	}
	ifs.close();
	ofs.close();
}

int main()
{
	TidyNumbers("F:\\dev\\projects\\Code Jam\\Code Jam\\B-large.in", "F:\\dev\\projects\\Code Jam\\Code Jam\\TidyNumbersOutput.txt");
	getchar();
    return 0;
}


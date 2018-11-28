// Code Jam.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <fstream>
#include <string>
#include <vector>
using namespace std;

void OversizedPancakeFlipper(string input_file_name, string output_fina_name)
{
#ifndef WIN32
#define _atoi64(val)     strtoll(val, NULL, 10)
#endif
	ifstream ifs(input_file_name, ios::in);
	ofstream ofs(output_fina_name, ios::out);
	if (!ifs.is_open() || !ofs.is_open()) return;
	int case_count = 0;
	const int max_length = 1024;
	char buff[max_length] = { 0 };
	ifs.getline(buff, max_length);
	case_count = _atoi64(buff);
	if (case_count <= 0) return;
	int case_index = 0;
	while (!ifs.eof()) {
		long long K(0);
		ifs.getline(buff, max_length);
		char pancakes[max_length] = { 0 };
		memset(pancakes, 0x00, max_length);
		sscanf(buff, "%s %lld", pancakes, &K);
		int length = strlen(pancakes);
		int times = 0;
		bool impossible = false;
		for (int i = 0; i < length; ++i) {
			if ('-' == pancakes[i]) {
				if (i + K > length) {
					impossible = true;
					break;
				}
				for (int j = 0; j < K; ++j) {
					if (pancakes[i + j] == '-') {
						pancakes[i + j] = '+';
					} else if (pancakes[i + j] == '+') {
						pancakes[i + j] = '-';
					}
				}
				++times;
			}
		}
		if (impossible) {
			ofs << "Case #" << case_index + 1 << ": IMPOSSIBLE" << endl;
			printf("%s, %lld   |   IMPOSSIBLE  %s\n", buff, K, pancakes);

		} else {
			ofs << "Case #" << case_index + 1 << ": " << times << endl;
			printf("%s, %lld   |   %d  %s\n", buff, K, times, pancakes);

		}
		if (++case_index == case_count) {
			break;
		}
	}
	ifs.close();
	ofs.close();
}

int main()
{
	OversizedPancakeFlipper("F:\\dev\\projects\\Code Jam\\Code Jam\\A-small-attempt0.in", "F:\\dev\\projects\\Code Jam\\Code Jam\\OversizedPancakeFlipperOutput.txt");
	getchar();
	return 0;
}


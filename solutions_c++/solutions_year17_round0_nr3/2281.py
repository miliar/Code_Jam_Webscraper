// Code Jam.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <fstream>
#include <string>
#include <vector>
using namespace std;

void CalcMaxMin(long long N, long long K, long long& Max, long long& Min)
{
	if (K <= 1) {
		Max = N / 2;
		Min = (N - 1) / 2;
		return;
	}
	if (K & 0x01) {
		if (N & 0x01) {
			return CalcMaxMin(N / 2, K / 2, Max, Min);
		} else {
			return CalcMaxMin((N - 1) / 2, (K - 1) / 2, Max, Min);
		}
	} else {
		if (N & 0x01) {
			return CalcMaxMin((N - 1) / 2, K / 2, Max, Min);
		} else {
			return CalcMaxMin(N / 2, K / 2, Max, Min);
		}
	}
}

void BathroomStalls(string input_file_name, string output_fina_name)
{
#ifndef WIN32
#define _atoi64(val)     strtoll(val, NULL, 10)
#endif
	ifstream ifs(input_file_name, ios::in);
	ofstream ofs(output_fina_name, ios::out);
	if (!ifs.is_open() || !ofs.is_open()) return;
	int case_count = 0;
	const char max_length = 50;
	char buff[max_length] = { 0 };
	ifs.getline(buff, max_length);
	case_count = _atoi64(buff);
	if (case_count <= 0) return;
	int i = 0;
	while (!ifs.eof()) {
		long long N(0), K(0), Max(0), Min(0);
		ifs.getline(buff, max_length);
		sscanf(buff, "%lld %lld", &N, &K);
		CalcMaxMin(N, K, Max, Min);
		ofs << "Case #" << i + 1 << ": " << Max << " " << Min << endl;
		printf("%lld, %lld   |   %lld, %lld\n", N, K, Max, Min);
		if (++i == case_count) {
			break;
		}
	}
	ifs.close();
	ofs.close();
}

int main()
{
	BathroomStalls("F:\\dev\\projects\\Code Jam\\Code Jam\\C-small-1-attempt1.in", "F:\\dev\\projects\\Code Jam\\Code Jam\\BathroomStallsOutput.txt");
	getchar();
    return 0;
}


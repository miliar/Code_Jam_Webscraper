// Code Jam.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <fstream>
#include <string>
#include <set>
using namespace std;


void CruiseControl(string input_file_name, string output_fina_name)
{
#ifndef WIN32
#define _atoi64(val)     strtoll(val, NULL, 10)
#endif
	ifstream ifs(input_file_name, ios::in);
	ofstream ofs(output_fina_name, ios::out);
	if (!ifs.is_open() || !ofs.is_open()) return;
	int case_count = 0;
	const int max_length = 100;
	char buff[max_length] = { 0 };
	ifs.getline(buff, max_length);
	case_count = atoi(buff);
	if (case_count <= 0) return;
	int case_index = 0;
	while (!ifs.eof()) {
		int N(0), D(0);
		ifs.getline(buff, max_length);
		sscanf(buff, "%d %d", &D, &N);
		char* stage = new char[N * N];
		memset(stage, 0x00, N * N);
		double speed_limit =-1;
		for (int i = 0; i < N; ++i) {
			int K(0), S(0);
			char horse[max_length] = { 0 };
			ifs.getline(horse, max_length);
			sscanf(horse, "%d %d", &K, &S);
			double time = (double)(D - K) / S;
			double speed = D / time;
			if (speed_limit < 0) speed_limit = speed;
			else {
				if (speed < speed_limit) speed_limit = speed;
			}
		}
		if (speed_limit < 0.000001) speed_limit = 0;

		ofs << "Case #" << case_index + 1 << ": " << std::fixed << (double)speed_limit << endl;
		if (++case_index == case_count) {
			break;
		}
	}
	ifs.close();
	ofs.close();
}

int main()
{
	CruiseControl("F:\\dev\\projects\\Code Jam\\Code Jam\\A-large (1).in", "F:\\dev\\projects\\Code Jam\\Code Jam\\CruiseControlOutput.txt");
	printf("__________________done\n");
	getchar();
	return 0;
}


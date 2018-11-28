// google-code-jam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <string>
#include <iostream>
#include <fstream>

void run_case(char* x) {
	int z = -1;
	int l = strlen(x);
	for (int i = 0; i < l - 1; i++)
	{
		if (x[i] > x[i + 1])
		{
			z = i;
			break;
		}
	}
	if (z > -1)
	{
		for (int i = z; i >= 0; i--)
		{
			x[i] = x[i] - 1;
			if (x[i - 1] <= x[i]) {
				for (int j = i + 1; j < l; j++) {
					x[j] = '9';
				}
				break;
			}
		}
	}
}
/*
void run_case_bruteforce(char* x) {
	int y = atoi(x);
	for (int i = y; i >= 0; i--) {
		itoa(i, x, 10);
		int l = strlen(x);
		bool ok = true;
		for (int idx = 1; idx < l; idx++) {
			if (x[idx] < x[idx - 1]) {
				ok = false;
				break;
			}
		}
		if (ok) return;
	}
}
*/
int main()
{
	std::ifstream filein("B-large.in");
	std::ofstream fileout("B-large.out");
	if (filein.is_open()) {
		char line[255];
		if (filein.getline(line, 255)) {
			int items = atoi(line);
			for (int i = 1; i <= items; i++) {
				if (filein.getline(line, 255)) {
					run_case(line);
					if (line[0] != '0') {
						fileout << "Case #" << i << ": " << &line[0] << std::endl;
					}
					else {
						fileout << "Case #" << i << ": " << &line[1] << std::endl;
					}
				}
			}
		}
		fileout.close();
		filein.close();
	}
	return 0;
}

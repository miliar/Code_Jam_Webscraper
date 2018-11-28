#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;

int check(char str[100]) {
	int i = 0;
	while (1) {
		if (str[i] == '-')
			return 0;
		if (str[i + 1] != '-' && str[i + 1] != '+')
			return 1;
		i++;
	}
}

void flip(char PM[100], int N, int caseN) {
	ofstream output("output.txt", ios_base::app);
	int i = 0, t, count = 0;
	while(1) {
		if (PM[i] == '-' && PM[i + N-1] != '-' && PM[i + N - 1] != '+') {
			output << "Case #" << caseN << ": IMPOSSIBLE\n";
			break;
		}
		if (PM[i] == '-') {
			for (t = 0; t < N; t++) {
				if (PM[i + t] == '-')
					PM[i + t] = '+';
				else
					PM[i + t] = '-';
			}
			count++;
		}
		if (check(PM) == 1) {
			output << "Case #" << caseN << ": " << count << endl;
			break;
		}
		i++;
	}
	output.close();
}

int main()
{
	int B, N, i = 0;
	char A[100];

	ifstream input("input.txt");
	input >> B;
	for (i = 0; i < B; i++) {
		input >> A >> N;
		flip(A, N, i+1);
	}
	input.close();
	return 0;
}
// 02_tidy_num.cpp : Defines the entry point for the console application.
//

// 01_pancake.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		string N;
		string tidyN;

		cin >> N;
		tidyN = string(N.length(), '9');
		bool fixed = false;
		for (int i = 0; i < N.length() && !fixed; ++i) {
			if (N[i] < tidyN[i]) {
				tidyN[i] = N[i];
			}

			int j = i;
			while (j) {
				if (tidyN[j] >= tidyN[j - 1])
					break;
				tidyN[j - 1] -= 1;
				tidyN[j] = '9';
				--j;
				fixed = true;
			}

		}
		while (tidyN.length() && tidyN[0] == '0')
			tidyN = tidyN.substr(1);
		if (tidyN.length() == 0)
			tidyN = "0";
		cout << "case #" << i + 1 << ": " << tidyN << endl;
	}
	return 0;
}



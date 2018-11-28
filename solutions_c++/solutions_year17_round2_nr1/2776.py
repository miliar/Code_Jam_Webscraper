#include <windows.h>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace::std;


int main(int argc, char* argv[])
{
	ifstream cin(argv[1]);

	int nCount, numCase = 1;
	cin >> nCount;

	while (numCase <= nCount)
	{
		double D;
		int N;

		cin >> D >> N;

		double hh[1000][2];

		for(int i = 0; i < N; i++)
		{
			cin >> hh[i][0] >> hh[i][1];
		}

		double max_t = -1;
		for (int i = 0; i < N; i++)
		{
			double t = (D - hh[i][0]) / hh[i][1];
			max_t = max(t, max_t);
		}

		char s[64];
		sprintf(s, "%f", D / max_t);

 		cout << "Case #" << numCase << ": ";
		cout << s;
 		cout << "\n";

		numCase++;
	}
	return 0;
}

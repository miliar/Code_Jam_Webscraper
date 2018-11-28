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
		long long N, K;

		cin >> N >> K;

		long long highbit = K;
		while(highbit & (highbit - 1))
			highbit &= highbit - 1;

		long long already = highbit - 1;
		long long avail = N - already;
		long long minrange = avail / highbit;
		long long remaining = avail - minrange * highbit;

		long long index = (K & (highbit - 1)) + 1;
		long long lastspace = minrange + (index <= remaining ? 1 : 0);

		long long totalmin = (lastspace - 1) / 2;
		long long totalmax = totalmin + (lastspace - 1) % 2;

 		cout << "Case #" << numCase << ": ";
		cout << totalmax << " " << totalmin;
 		cout << "\n";

		numCase++;
	}
	return 0;
}

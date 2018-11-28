#include <stdio.h>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
using namespace std;

void main() {
	FILE *fin = freopen("A-small.in", "r", stdin);
	assert(fin != NULL);
	FILE *fout = freopen("A-small.out", "w", stdout);
	int T;
	cin >> T;
	
	for (int t = 1; t <= T; t++)
	{
		int c;
		bool* container = new bool[1000];
		int continerIndex = 0;
		while (true)
		{
			c = getc(fin);
			if (c == ' ')
				break;
			else if (c == '-')
				container[continerIndex++] = false;
			else if (c == '+')
				container[continerIndex++] = true;
		}

		int k;
		cin >> k;
		int flipCount = 0; 
		
		for (int i = 0; i < continerIndex;i++)
		{
			if (false == container[i])
			{					
				if ((k) > abs(i - continerIndex))
				{
					flipCount = -1;
					break;
				}
				else
				{
					++flipCount;
					for (int j = 0; j < k; ++j)
					{
						container[i + j] = !container[i + j];
					}
				}
			}			
		}

		if ( 0 <= flipCount)
			std::cout << "Case #" << t << ": " << flipCount << std::endl;
		else
			std::cout << "Case #" << t << ": " << "IMPOSSIBLE" << std::endl;
	}

	
	exit(0);
}
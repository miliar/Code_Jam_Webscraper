#include <cstdio>
#include <vector>
#include <deque>
#include <queue>
#include <map>
#include <algorithm>
#include <functional>
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <string.h>

using namespace std;

bool isTidy(unsigned long long n, int& place)
{
	string s = to_string(n);
	for (unsigned long long i = 0; i < s.length() - 1; i++)
	{
		if (s[i] > s[i + 1])
		{
			int count = 0;
/*			int k = i;
			while ((k != 0) && (s[k - 1] == s[k]))
			{
				k--;
				count++;
			}*/
			place = s.length() - 1 - i + count;
			return false;
		}
	}
	place = 0;
	return true;
}

int main(int argc, const char **argv)
{
    if (argc != 2)
    {
        fprintf(stderr, "Error:%d\n", __LINE__);
        return -1;
    }

    ifstream fin(argv[1]);
    ofstream fout("out.txt");

    int T;
    fin >> T;
    for (int j = 0; j < T; j++)
    {
        unsigned long long N;
        fin >> N;

		unsigned long long n = N;
		while (1)
		{
			int place = 0;
			if (isTidy(n, place) == true)
			{
				break;
			}
			unsigned long long x = 1;
			while (place != 0)
			{
				x *= 10;
				place--;
			}
			n -= n % x;
			n--;
		}

		fout << "Case #" << j + 1 << ": " << n << endl;
    }
	
    return (0);
}

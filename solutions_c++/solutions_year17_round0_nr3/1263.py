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

bool isOdd(long long x)
{
	bool ret = false;
	if (x % 2 == 1)
	{
		ret = true;
	}
	return ret;
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
		unsigned long long K;
		fin >> K;

		unsigned long long n = N;
		for (long long k = K; k != 1; k /= 2)
		{
			if (isOdd(k) == false)
			{
				n /= 2;
			}
			else
			{
				n = (n - 1) / 2;
			}
		}

		unsigned long long maxLsRs = n / 2;
		unsigned long long minLsRs = (n - 1) / 2;
		fout << "Case #" << j + 1 << ": " << maxLsRs << " " << minLsRs << endl;
	}
	
    return (0);
}

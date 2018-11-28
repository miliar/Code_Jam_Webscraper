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

#define PI 3.14159265358979323846

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
		int N;
		fin >> N;
		int K;
		fin >> K;

		unsigned long long r[1000];
		unsigned long long h[1000];
		for (int i = 0; i < N; i++)
		{
			fin >> r[i];
			fin >> h[i];
		}

		unsigned long long x[1000];
		for (int i = 0; i < N; i++)
		{
			x[i] = 2 * r[i] * h[i];
		}

		unsigned long long max = 0;
		for (int k = 0; k < N; k++)
		{
			unsigned long long y[1000];
			for (int i = 0; i < N; i++)
			{
				y[i] = x[i];
			}

			unsigned long long z = y[k];
			y[k] = 0;
			sort(y, y + N, greater<unsigned long long>());

			for (int i = 0; i < K - 1; i++)
			{
				z += y[i];
			}

			if (max < r[k] * r[k] + z)
			{
				max = r[k] * r[k] + z;
			}
		}

		fout << "Case #" << j + 1 << ": " << fixed << PI * max << endl;
	}

    return (0);
}

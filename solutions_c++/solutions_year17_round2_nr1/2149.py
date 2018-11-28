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
		long D;
		fin >> D;
		int N;
		fin >> N;

		long K[1000];
		int S[1000];
		for (int i = 0; i < N; i++)
		{
			fin >> K[i];
			fin >> S[i];
		}

		double max = 0.0;
		for (int i = 0; i < N; i++)
		{
			double h = (double)(D - K[i]) / S[i];
			if (h > max)
			{
				max = h;
			}
		}

		fout << "Case #" << j + 1 << ": " << fixed << D / max << endl;
	}
	
    return (0);
}

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
		int N;
		fin >> N;

		int C[6];
		for (int i = 0; i < 6; i++)
		{
			fin >> C[i];
		}

		char COLOR[] = "ROYGBV";

		int max = 0;
		int oldx;
		int x = 0;
		for (int i = 0; i < 6; i += 2)
		{
			if (max < C[i])
			{
				max = C[i];
				oldx = x;
				x = i;
			}
		}

		if (max > N / 2)
		{
			fout << "Case #" << j + 1 << ": IMPOSSIBLE" << endl;
		}
		else
		{
			string str;
			str += COLOR[x];
			C[x]--;
			int prev = x;
			int firstx = x;
			while (!(C[0] == 0 && C[2] == 0 && C[4] == 0))
			{
				int max = 0;
				int oldx = 4;
				int x = 0;
				for (int i = 0; i < 6; i += 2)
				{
					if (max < C[i])
					{
						max = C[i];
						oldx = x;
						x = i;
					}
				}

				if (max == C[firstx])
				{
					x = firstx;
				}

				if (prev != x)
				{
					str += COLOR[x];
					C[x]--;
					prev = x;
				}
				else
				{
					if (oldx != x)
					{
						str += COLOR[oldx];
						C[oldx]--;
						prev = oldx;
					}
					else
					{
						int y = 0;
						if (oldx == 0)
						{
							y = 2;
						}
						str += COLOR[y];
						C[y]--;
						prev = y;
					}
				}
			}

			fout << "Case #" << j + 1 << ": " << str << endl;
		}
	}
	
    return (0);
}

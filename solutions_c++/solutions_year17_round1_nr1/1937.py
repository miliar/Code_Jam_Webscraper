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
		int R;
		fin >> R;
		int C;
		fin >> C;

		char cake[25][25];
		for (int i = 0; i < R; i++)
		{
			string str;
			fin >> str;
			for (int k = 0; k < C; k++)
			{
				cake[i][k] = str[k];
			}
		}

		for (int i = 0; i < R; i++)
		{
			char c = '0';
			for (int k = 0; k < C; k++)
			{
				if (cake[i][k] != '?')
				{
					c = cake[i][k];
				}
				else
				{
					if (c != '0')
					{
						cake[i][k] = c;
					}
				}
			}
			c = '0';
			for (int k = C - 1; k >= 0; k--)
			{
				if (cake[i][k] != '?')
				{
					c = cake[i][k];
				}
				else
				{
					if (c != '0')
					{
						cake[i][k] = c;
					}
				}
			}

			if (cake[i][0] == '?')
			{
				if (i != 0 && cake[i - 1][0] != '?')
				{
					for (int k = 0; k < C; k++)
					{
						cake[i][k] = cake[i - 1][k];
					}
				}
			}
		}

		for (int i = R - 1; i >= 0; i--)
		{
			if (cake[i][0] == '?')
			{
				if ((i != R - 1) && cake[i + 1][0] != '?')
				{
					for (int k = 0; k < C; k++)
					{
						cake[i][k] = cake[i + 1][k];
					}
				}
			}
		}

		fout << "Case #" << j + 1 << ":" << endl;
		for (int i = 0; i < R; i++)
		{
			for (int k = 0; k < C; k++)
			{
				fout << cake[i][k];
			}
			fout << endl;
		}
	}
	
    return (0);
}

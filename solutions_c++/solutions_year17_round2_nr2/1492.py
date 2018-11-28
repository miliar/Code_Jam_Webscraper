#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <cmath>
#include <limits>
#include <iomanip>

using namespace std;

#define RED 1
#define YELLOW 2
#define BLUE 3

typedef long long ll;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<vi> vvi;
typedef vector<vb> vvb;

ifstream fin;
ofstream fout;

void init(string inputFile, string outputFile)
{
	fin.open(inputFile);
	fout.open(outputFile);
}

void end()
{
	fin.close();
	fout.close();
}

int main()
{
	init("B-small-attempt0.in", "output.txt");
	int T;
	fin >> T;
	
	for (int t = 0; t < T; t++)
	{
		int N;
		fin >> N;
		int R, Y, B;
		int temp;
		fin >> R >> temp >> Y >> temp >> B >> temp;
		int last = 0;
		vector<int> res(N);
		for (int i = 0; i < N; i++)
		{
			if (last == 0)
			{
				int maxc = max(R, max(Y, B));
				if (R == maxc)
				{
					last = RED;
					res[i] = RED;
					R--;
					continue;
				}
				if (B == maxc)
				{
					last = BLUE;
					res[i] = BLUE;
					B--;
					continue;
				}
				if (Y == maxc)
				{
					last = YELLOW;
					res[i] = YELLOW;
					Y--;
					continue;
				}
			}
			if (last == RED)
			{
				if ((Y > B) || ((Y == B) && (res[0] == YELLOW)))
				{
					res[i] = YELLOW;
					Y--;
					last = YELLOW;
				}

				else
				{
					res[i] = BLUE;
					B--;
					last = BLUE;
				}
				continue;
			}
			if (last == BLUE)
			{
				if (R > Y || ((R == Y) && (res[0] == RED)))
				{
					res[i] = RED;
					R--;
					last = RED;
				}

				else
				{
					res[i] = YELLOW;
					Y--;
					last = YELLOW;
				}
				continue;
			}
			if (last == YELLOW)
			{
				if (R > B || ((R == B) && (res[0] == RED)))
				{
					res[i] = RED;
					R--;
					last = RED;
				}

				else
				{
					res[i] = BLUE;
					B--;
					last = BLUE;
				}
				continue;
			}
		}

		fout << "Case #" << t + 1 << ": ";
		if ((R < 0) || (Y < 0) || (B < 0) || (res[0] == res[N-1]))
		{
			fout << "IMPOSSIBLE" << endl;
			continue;
		}

		for (int i = 0; i < N; i++)
		{
			if (res[i] == RED)
			{
				fout << "R";
			}

			if (res[i] == YELLOW)
			{
				fout << "Y";
			}
			if (res[i] == BLUE)
			{
				fout << "B";
			}
		}

		fout << endl;
		//double res = (d / maxTime);
		//ll temp = res * 1000000;
		//fout << temp / 1000000 << "." << temp % 1000000 << endl;
		//fout.precision(7);
		//fout << "Case #" << t + 1 << ": ";
		//fout << fixed << setprecision(6);
		//fout << (d / maxTime) << endl;
	}
	end();
	return 0;
}
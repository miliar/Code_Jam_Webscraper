#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <cmath>
#include <limits>
#include <iomanip>

using namespace std;

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
	init("A-large.in", "output.txt");
	int T;
	fin >> T;
	
	for (int t = 0; t < T; t++)
	{
		double maxTime = 0;
		double d;
		int n;
		fin >> d >> n;
		for (int i = 0; i < n; i++)
		{
			double x, y;
			fin >> x >> y;
			maxTime = max((d - x) / y, maxTime);
		}

		//double res = (d / maxTime);
		//ll temp = res * 1000000;
		//fout << temp / 1000000 << "." << temp % 1000000 << endl;
		//fout.precision(7);
		fout << "Case #" << t + 1 << ": ";
		fout << fixed << setprecision(6);
		fout << (d / maxTime) << endl;
	}
	end();
	return 0;
}
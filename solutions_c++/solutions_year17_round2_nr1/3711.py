#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <iomanip>
#include <queue>

using namespace std;

int main(int argc, char* argv[])
{
	argv[1] = "D:\\Other\\BISHI\\GoogleCodeJam\\A\\A-small-attempt2.in";
	argv[2] = "D:\\Other\\BISHI\\GoogleCodeJam\\A\\A-small-attempt2.out";

	//ifstream fin(stdin);
	//ofstream fout(stdout);
	ifstream fin(argv[1]);
	ofstream fout(argv[2]);

	string line;
	getline(fin, line);
	int testNum = stoi(line);
	for (int i = 0; i < testNum; i++)
	{
		getline(fin, line);
		int space = line.find(" ");
		long long D = stol(line.substr(0, space));
		long long N = stol(line.substr(space + 1, line.length() - space - 1));
		float min = FLT_MAX;

		for (int i = 0; i < N; i++)
		{
			getline(fin, line);
			space = line.find(" ");
			long long Ki = stol(line.substr(0, space));
			long long Si = stol(line.substr(space + 1, line.length() - space - 1));
			float s = D*Si*1.0 / (D - Ki);
			if (s < min)
				min = s;
		}
		fout.setf(ios::showpoint);
		fout.precision(6);
		fout.setf(ios::fixed);
		fout << "Case #" << i + 1 << ": " << min << endl;
	}

	fin.close();
	fout.close();
}
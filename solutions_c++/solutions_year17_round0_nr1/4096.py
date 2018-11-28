#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int main(int argc, char* argv[])
{
	argv[1] = "D:\\Other\\BISHI\\GoogleCodeJam\\A\\A-large.in";
	argv[2] = "D:\\Other\\BISHI\\GoogleCodeJam\\A\\A-large.out";

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
		string S = line.substr(0, space);
		int K = stoi(line.substr(space + 1, line.length() - space - 1));

		int result = -1;
		int flipN = 0;
		int lB = 0, rB = S.length() - 1;
		while (rB - lB + 1>= K)
		{
			//考虑从左边数起第一个'-'开始的K的值的反转
			while (lB < S.length() && S[lB] != '-') lB++;
			if (lB == S.length())
			{
				result = flipN;
				break;
			}
			if (rB - lB  + 1 < K)
				break;
			else
			{
				for (int j = lB; j < lB + K; j++)
					(S[j] == '-') ? S[j] = '+' : S[j] = '-';
				flipN++;
			}

			//考虑从右边数起第一个'-'开始的K个值的反转
			while (rB >-1 && S[rB] != '-') rB--;
			if (rB == -1)
			{
				result = flipN;
				break;
			}
			if (rB - lB < K)
				break;
			else
			{
				for (int j = rB; j > rB - K; j--)
					(S[j] == '-') ? S[j] = '+' : S[j] = '-';
				flipN++;
			}

		}

		if (result == -1)
			fout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
		else
			fout << "Case #" << i + 1 << ": " << result << endl;
	}

	fin.close();
	fout.close();
}
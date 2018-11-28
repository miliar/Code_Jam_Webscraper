#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;


void findLsRsOdd(int N, int K, int mult, int& minLsRs, int& maxLsRs)
{
	if (K >= mult)
	{
		minLsRs = N / 2 - 1;
		maxLsRs = N / 2 - 1;
	}
	else if (mult - K == 1)
	{
		minLsRs = N / 2 - 1;
		return;
	}
	else
	{
		return;
	}
	N = N / 2 + 1;
	K = K - mult;
	if (K == 0)
	{
		return;
	}
	findLsRsOdd(N, K, mult * 2, minLsRs, maxLsRs);
}

void findLsRs(int N, int K, int& minLsRs, int& maxLsRs)
{
	vector<int> stalls(1);
	stalls[0] = N;
	for (int i = 0; i < K; ++i)
	{
		int index = 0;
		int max = 0;
		for (int j = 0; j < stalls.size(); ++j)
		{
			if (stalls[j] > max)
			{
				max = stalls[j];
				index = j;
			}
		}
		minLsRs = (int)ceil(((double)stalls[index] / 2.0 - 1));
		maxLsRs = (int)floor(((double)stalls[index] / 2.0));
		stalls[index] = maxLsRs;
		stalls.insert(stalls.begin()+index, minLsRs);
	}
}

void findLsRsOpt(int N, int K, int& minLsRs, int& maxLsRs)
{
	if (N % 2 == 0)
	{
		findLsRs(N, K, minLsRs, maxLsRs);
	}
	else if (N % 2 == 1)
	{
		findLsRsOdd(N, K, 1, minLsRs, maxLsRs);
	}
}

int main(){ 
	ifstream input;
	input.open("input.txt");
	ofstream output;
	output.open("output.txt");
	if (!output.is_open())
	{
		cout << "Cannot open output file!" << endl;
		return 1;
	}
	if (input.is_open())
	{
		string line;
		getline(input, line);
		int cases = stoi(line);
		for (int c = 1; c <= cases; ++c)
		{
			if (!getline(input, line))
			{
				cout << "Cannot find further test cases!" << endl;
				return 1;
			}
			int N = stoi(line.substr(0, line.find(" ")));
			int K = stoi(line.substr(line.find(" ")));
			int minLsRs = -1;
			int maxLsRs = -1;
			findLsRs(N, K, minLsRs, maxLsRs);
			if ((-1 == minLsRs) || (-1 == maxLsRs))
			{
				cout << "Something wrong with minLsRs or maxLsRs!" << endl;
				return 1;
			}
			//cout << "Case #" << c << ": " << maxLsRs << " " << minLsRs << endl;
			output << "Case #" << c << ": " << maxLsRs << " " << minLsRs << endl;
		}
	}
	else
	{
		cout << "Cannot read input file!" << endl;
	}
	input.close();
	output.close();
	return 0;
}
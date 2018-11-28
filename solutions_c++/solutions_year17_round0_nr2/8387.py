#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;
long long getTidy(long long input)
{
	vector<int> nList;
	long long input0 = input;
	while(input0 > 0)
	{
       nList.push_back(input0 % 10);
       input0 /= 10;
	}
	long long res = 0;
	for(int i = 0; i < nList.size(); i++)
	{
		int currentPos = nList.size() - 1 - i;
		int currentNum = nList[currentPos];
		// check if this one need to be replaced 
		long long newNumer = res * 10 + currentNum;
		for(int j = currentPos - 1 ; j >= 0; j--)
		{
			newNumer *= 10;
			newNumer += currentNum;
		}
		if(newNumer <= input)
		{
			res = res * 10 + currentNum;
		}
		else {
			res = res * 10 + currentNum - 1;
			for(int j = currentPos - 1 ; j >= 0; j--)
			{
				res *= 10;
				res += 9;
			}
			return res;
		}
	}
	return res;
}

int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int totalCase;
	fin >> totalCase;
	for(int i = 1; i <= totalCase; i++)
	{
		long long N;
		fin >> N;
		fout << "Case #" << to_string(i) << ": ";
		long long res = getTidy(N);
		fout << res << endl;
	}
	return 0;
}
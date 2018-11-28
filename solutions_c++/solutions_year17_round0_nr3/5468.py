#include <string>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <fstream>
#include <cmath>
#include <algorithm>
using namespace std;

void putInStall(vector<bool> &stalls, int &maxLs, int &maxRs)
{
	int n2 = 0;
	int n1 = 0;

	int pos = 0;

	for (int i = 0; i < stalls.size(); i++)
	{
		if (stalls[i] == 1&&(i-pos>n2-n1))
		{
			n1 = pos;
			n2 = i;
			pos = i;
		}
		else if (stalls[i] == 1)
		{
			pos = i;
		}
	}
	int index = (n2 + n1) / 2;
	maxLs = index - n1 - 1;
	maxRs = n2 - index - 1;
	stalls[index] = true;
	/*
	cout << "index: " << index << endl;
	cout << "n2: " << n2 << endl;
	cout << "n1: " << n1 << endl;
	cout << endl;
	*/
	/*
	int index;
	for (int i = 0; i < stalls.size(); i++)
	{
		int Ls = -1;
		int Rs = -1;
		for (int j = i; j >= 0; j--)
		{
			if (stalls[j])
				break;
			Ls++;
		}
		for (int j = i; j < stalls.size(); j++)
		{
			if (stalls[j])
				break;
			Rs++;
		}
		if (min(Ls, Rs) > min(maxLs, maxRs))
		{
			maxLs = Ls;
			maxRs = Rs;
			index = i;
		}
		else if (min(Ls, Rs) == min(maxLs, maxRs)&&max(Ls, Rs) > max(maxLs, maxRs))
		{
			maxLs = Ls;
			maxRs = Rs;
			index = i;
		}
		else if (min(Ls, Rs) == min(maxLs, maxRs) && max(Ls, Rs) == max(maxLs, maxRs) && Ls < maxLs)
		{
			maxLs = Ls;
			maxRs = Rs;
			index = i;
		}
	}
	stalls[index] = true;*/
}

int main() {
	ifstream inStream;
	ofstream outStream;

	inStream.open("C-small-1-attempt1.in");
	outStream.open("output.txt");

	int loop;
	inStream >> loop;
	
	for (int count = 1; count <= loop; count++)
	{
		int N;
		inStream >> N;
		vector<bool> stalls(N+2); //create vector of stalls
		for (int i = 0; i < stalls.size(); i++) //assign all stalls to false
		{
			stalls[i] = false;
		}
		stalls[0] = true;   //leftmost and rightmost stalls are occupied
		stalls[N + 1] = true;


		int K; //K = number of people to enter bathroom
		inStream >> K;

		if (K == N)
		{
			outStream << "Case #" << count << ": 0 0" << endl;
			cout << "Case #" << count << ": 0 0" << endl;
		}
		else
		{
			int maxLs;
			int maxRs;

			for (int i = 0; i < K; i++)
			{
				maxLs = -1;
				maxRs = -1;
				putInStall(stalls, maxLs, maxRs);
			}
			outStream << "Case #" << count << ": " << max(maxLs, maxRs) << " " << min(maxLs, maxRs) << endl;
			cout << "Case #" << count << ": " << max(maxLs, maxRs) << " " << min(maxLs, maxRs) << endl;
		}
	}

	inStream.close();
	outStream.close();

	return(0);
}
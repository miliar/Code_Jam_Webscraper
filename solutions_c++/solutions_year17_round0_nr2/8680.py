#include <iostream>
#include <string>
#include <fstream>
using namespace std;

bool checkTidyness(int N);

int main()
{
	ifstream infile("B-small-attempt0.in");
	ofstream outfile("B-small-attempt0.out");
	int T;
	int N;

	infile >> T;

	for (int i = 0; i < T; i++)
	{
		infile >> N;

		for (int j = N; j >= 0; j--)
		{
			if (checkTidyness(j))
			{
				outfile << "Case #" << i+1 << ": " << j << endl;
				break;
			}
		}
	}

	return 0;
}

bool checkTidyness(int N)
{
	string num = to_string(N);

	for (int i = 0; i < num.length()-1; i++)
	{
		if (num.at(i) > num.at(i + 1))
			return false;
	}

	return true;
}
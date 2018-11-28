/*
ID: paradoxes
PROG: Oversized Pancake Flipper
LANG: C++
*/

#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int T;

int K, length;

string S;

void flip(int start)
{
	if (start > length - K)
		cerr << "Error 1 has occured" << endl;

	for (int i = start; i < start + K; i++)
	{
		if (S[i] == '+')
			S[i] = '-';
		else
			S[i] = '+';
	}

	return;

}

int main()
{
	ifstream Input("pancake.in");
	ofstream Output("pancake.out");

	Input >> T;

	int counter;

	bool isGood;

	for (int j = 1; j <= T; j++)
	{
		Input >> S >> K;

		length = S.length();

		counter = 0;

		for (int i = 0; i <= length - K; i++)
		{
			if (S[i] != '+')
			{
				flip(i);
				counter++;
			}
		}

		isGood = true;

		for (int i = 0; i < length; i++)
		{
			if (S[i] == '-')
			{
				Output << "Case #" << j << ": " << "IMPOSSIBLE" << endl;
				isGood = false;
				break;
			}
		}

		if(isGood)
			Output << "Case #" << j << ": " << counter << endl;
	}

	return 0;
}
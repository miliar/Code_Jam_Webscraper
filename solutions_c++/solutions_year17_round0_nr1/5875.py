#include <iostream>
#include <string>
#include <map>
#include <fstream>

using namespace std;


char flip(char in) {
	if (in == '-')return '+';
	return '-';
}

bool checkSolution(string in)
{
	for (int i = 0; i < in.length(); i++)
	{
		if (in[i] == '-')return false;
	}
	return true;
}

int main()
{
	
	ofstream of;
	of.open("input.in");


	int n;
	cin >> n;

	for (int i = 1; i <= n; i++)
	{
		int up = 0, down = 0;
		string in;int K;
		cin >> in >> K;

		int count = 0;
		for (int k = 0; k < in.length() - K+1; k++)
		{		
			if (in[k] == '-') { count++; for (int l = k; l < k +K; l++) { in[l] = flip(in[l]); } }
		}

		if (checkSolution(in)) of << "Case #" << i << ": " << count << "\n";
		else of << "Case #" << i << ": IMPOSSIBLE\n";

	}

	of.close();

	return 0;
}
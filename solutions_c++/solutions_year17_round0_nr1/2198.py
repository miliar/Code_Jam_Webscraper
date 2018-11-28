#include <fstream>
#include <string>
#include <vector>
using namespace std;

void flip(vector<bool>& pancakes, int K, int startPos)
{
	for (int i = 0; i < K; ++i)
	{
		pancakes[startPos + i] = !pancakes[startPos + i];
	}
}

bool canFlip(const vector<bool>& pancakes, int K, int startPos)
{
	return (startPos + K - 1 < pancakes.size());
}

bool isPositive(const vector<bool>& pancakes)
{
	for (int i = 0; i < pancakes.size(); ++i)
	{
		if (!pancakes[i])
		{
			return false;
		}
	}

	return true;
}

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	int T;
	in >> T;

	for (int t = 0; t < T; ++t)
	{
		string S;
		int K;
		in >> S >> K;
		
		vector<bool> pancakes(S.size());
		for (int i = 0; i < pancakes.size(); ++i)
		{
			pancakes[i] = (S[i] == '+');
		}

		int flipsCount = 0;
		for (int i = 0; i < pancakes.size(); ++i)
		{
			if (!pancakes[i] && canFlip(pancakes, K, i))
			{
				flip(pancakes, K, i);
				flipsCount++;
			}
		}


		out << "Case #" << t + 1 << ": ";
		if (isPositive(pancakes))
		{
			out << flipsCount << endl;
		}
		else
		{
			out << "IMPOSSIBLE" << endl;
		}
	}

	return 0;
}
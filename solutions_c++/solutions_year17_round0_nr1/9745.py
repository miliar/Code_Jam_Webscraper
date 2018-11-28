#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <unordered_map>
#include <queue>

using namespace std;

string Flip(string &cakes, int pos, int K)
{
	string fliped(cakes);
	for (int i = 0; i < K; ++i)
	{
		if (fliped[pos + i] == '+')
			fliped[pos + i] = '-';
		else
			fliped[pos + i] = '+';
	}
	return fliped;
}

void ProblemA()
{
	ifstream input("C:\\Users\\dal4s\\Downloads\\A-small-attempt1 (1).in");
	ofstream output("C:\\Users\\dal4s\\Desktop\\outputA.txt");
	
	int T(0);
	input >> T;

	string cakes;
	int K(0);

	for (int CASE = 1; CASE <= T; ++CASE)
	{
		bool OK(false);
		unordered_map<string, int> already;
		queue<pair<string, int>> Q;

		input >> cakes >> K;
		output << "Case #" << CASE << ": ";
		int len(cakes.length());

		already.insert({ cakes, 0 });
		Q.push({ cakes, 0 });
		while (!Q.empty())
		{
			string current = Q.front().first;
			int count = Q.front().second;
			Q.pop();

			if (all_of(current.begin(), current.end(), [](char c) { return c == '+'; }))
			{
				output << count << '\n';
				OK = true;
				break;
			}
			else
			{
				for (int i = 0; i <= len - K; ++i)
				{
					string fliped = Flip(current, i, K);
					if (already.insert({ fliped, count + 1 }).second)
						Q.push({ fliped, count + 1 });
				}
			}
		}
		if (OK == false)
			output << "IMPOSSIBLE\n";
	}
}

int main()
{
	ProblemA();
	return 0;
}
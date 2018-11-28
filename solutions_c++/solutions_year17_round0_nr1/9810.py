#include <iostream>
#include <cstdio>
#include <stack>
#include <map>
#include <utility>
#include <queue>

struct Combo
{
	Combo(int flips, std::string sequence) : flips(flips), sequence(sequence) {}
	int flips;
	std::string sequence;
};

Combo flip(Combo& combo, int index, int flipSize)
{
	std::string s = combo.sequence;

	for (int i = index; i < index + flipSize; i++)
	{
		if (s[i] == '+') s[i] = '-';
		else if (s[i] == '-') s[i] = '+';
	}
	return Combo(combo.flips + 1, s);
}

int main()
{
	int T;
	scanf("%d", &T);

	for (int i = 0; i < T; i++)
	{
		char S[2048];
		int K;
		scanf("%s %d", S, &K);
		int N = strlen(S);

		int minFlip = -1;

		std::queue<Combo> stack;
		Combo val(0, std::string(S, S + N));
		stack.push(val);
		std::map<std::string, bool> seen;

		while (!stack.empty())
		{
			Combo c = stack.front();
			stack.pop();
			if (seen.find(c.sequence) != seen.end())
			{
				continue;
			}

			// Min Solved Condition.
			if (c.sequence.find("-") == std::string::npos)
			{
				if (c.flips < minFlip || minFlip == -1)
				{
					minFlip = c.flips;
				}
				continue;
			}
			seen[c.sequence] = true;

			/// Iterate over everything we can flip.
			for (int j = 0; j < (N - K + 1); j++)
			{
				std::string substr = c.sequence.substr(j, K);
				Combo newC = flip(c, j, K);
				if (seen.find(newC.sequence) == seen.end())
				{
					stack.push(newC);
				}
			}
		}
		seen.clear();
		
		if (minFlip == -1)
		{
			printf("Case #%d: IMPOSSIBLE\n", i + 1);
		}
		else
		{
			printf("Case #%d: %d\n", i + 1, minFlip);
		}
	}
	return 0;
}


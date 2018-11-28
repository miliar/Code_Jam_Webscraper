#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>
#include <string>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

struct solution
{
	string input;
	int moves;
	bool impossible;

	bool validate()
	{
		for (auto c : input) if (c != '+') return false;
		return true;
	}
};


solution solve(const string input, const int k)
{
	vector<solution> solutions;
	solution solution{ input, 0, false };
	solutions.push_back(solution);

	int i = 0;
	const int s = input.size();

	while (i < solutions.size())
	{
		//If I am correct, return me.
		if (solutions[i].validate())
			return solutions[i];

		//Iterate
		const auto sol = solutions[i];
		int moves = sol.moves + 1;
		for (int j = 0; j <= s - k; j++)
		{
			string newInput = "";
			for (int l = 0; l < s; l++)
			{
				auto flip = (l >= j && l < j + k);
				if (flip)
					newInput += (sol.input[l] == '+') ? '-' : '+';
				else
					newInput += (sol.input[l] == '+') ? '+' : '-';
				
			}

			//Look for an existing solution. If found and has less moves, abort me.
			bool found = false;
			for (int m = 0; m < solutions.size(); m++)
			{
				if (m != i && newInput == solutions[m].input)
				{
					found = true;
					break;
				}
			}
			if (!found)
				solutions.push_back({ newInput, moves, false });
		}
		i++;
	}

	auto impossibleSolution = solutions[0];
	impossibleSolution.impossible = true;
	return impossibleSolution;
}

void main() {
	int t, n, m;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		string input;
		int k;

		cin >> input;
		cin >> k;

		auto solution = solve(input, k);
		
		if (solution.impossible)
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
		else
			cout << "Case #" << i << ": " << solution.moves << endl;
	}
}
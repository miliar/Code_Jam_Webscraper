#include <iostream>
#include <vector>
#include <cctype>
#include <iterator>

using namespace std;

void impossible()
{
	cout << "IMPOSSIBLE\n";
}

bool flip(vector<char>& pancakes, vector<char>::iterator current, int spatula)
{
	if (distance(current, pancakes.end()) < spatula)
	{
		return false;
	}

	for (int i = 0; i < spatula; ++i)
	{
		if (*current == '+')
		{
			*current = '-';
		}
		else
		{
			*current = '+';
		}
		++current;
	}

	return true;
}


int main()
{
	int test_cases;
	cin >> test_cases;

	vector<char> pancakes;
	int spatula;
	char dump;
	for (int test = 1; test < test_cases + 1; ++test)
	{
		bool complete = false;

		cout << "Case #" << test << ": ";
		
		cin >> ws;
		while (cin.peek() == '-' || cin.peek() == '+')
		{
			dump = getchar();
			pancakes.push_back(dump);
		}
		cin >> spatula;

		// Handle greater case
		if (spatula > pancakes.size())
		{
			impossible();
			pancakes.clear();
			continue;
		}

		// Handle equal case
		if (spatula == pancakes.size())
		{
			char match = pancakes[0];
			for (int i = 0; i < pancakes.size(); ++i)
			{
				if (pancakes[i] != match)
				{
					impossible();
					complete = true;
					break;
				}
			}
			if (complete)
			{
				pancakes.clear();
				continue;
			}

			if (match == '-')
			{
				cout << "1\n";
			}
			else
			{
				cout << "0\n";
			}

			pancakes.clear();
			continue;
		}

		int flips = 0;
		bool result = true;
		// Handle normal case
		vector<char>::iterator current = pancakes.begin();
		for (; current != pancakes.end(); ++current)
		{
			if (*current == '-')
			{
				result = flip(pancakes, current, spatula);
				if (!result)
				{
					impossible();
					complete = true;
					break;
				}
				else
				{
					++flips;
				}
			}
		}

		if (!complete)
		{
			cout << flips << "\n";
		}

		pancakes.clear();
	}

	return 0;
}
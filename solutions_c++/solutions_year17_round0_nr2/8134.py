#include <iostream>
#include <vector>
#include <cctype>

using namespace std;

// Handle leading zeros

void printVector(vector<int> vec)
{
	bool isFirst = true;
	for (int i = 0; i < vec.size(); ++i)
	{
		if (isFirst)
		{
			if (vec[i] != 0)
			{
				cout << vec[i];
				isFirst = false;
			}
		}
		else 
		{
			cout <<vec[i];
		}
	}
}


int main()
{
	int test_cases;
	cin >> test_cases;

	vector<int> num;
	char dump;
	for (int test = 1; test < test_cases + 1; ++test)
	{
		cin >> ws;
		bool done = false;

		while (isdigit(cin.peek()))
		{
			dump = getchar();
			num.push_back(static_cast<int>(dump) - 48);
		}

		if (num.size() == 1)
		{
			cout << "Case #" << test << ": ";
			printVector(num);
			cout << "\n";
			num.clear();
			continue;
		}
		int i = 0;
		bool inc = true;
		while(i < num.size() - 1)
		{
			inc = true;
			if (num[i+1] < num[i])
			{
				for (int k = i; k >= 0; --k)
				{
					if (num[k] != 0)
					{
						--num[k];
						for (int j = k + 1; j < num.size(); ++j)
						{
							num[j] = 9;
						}
						if (k != 0)
						{
							i = k - 1;
							inc = false;
						}
						
						break;
					}
				}
			}
			if (inc)
			{
				++i;
			}
		}

		cout << "Case #" << test << ": ";
		printVector(num);
		cout << "\n";

		num.clear();
	}

	return 0;
}
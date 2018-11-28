#include <iostream>
#include <vector>
#include <string>

using namespace std;

string get_count(string inp, int row_numb)
{
	int count = 0;
	for (int i = 0; i < inp.size(); i++)
	{
		if (inp[i] == '-')
		{
			count++;
			if (i + row_numb > inp.size())
				return "IMPOSSIBLE";

			for (int k = i; k < i + row_numb; k++)
			{
				if (inp[k] == '-')
					inp[k] = '+';
				else inp[k] = '-';
			}
		}
	}

	return to_string(count);
}

void main()
{
	int T = 0;
	cin >> T;

	vector<pair<string,int> > numbers(T);

	for (int i = 0; i < T; ++i)
	{
		string numb("");
		int row_numb = 0;
		cin >> numb >> row_numb;

		numbers[i] = make_pair(numb, row_numb);
	}

	int i = 0;
	vector<pair<string, int> >::iterator it = numbers.begin();
	for (; it != numbers.end(); ++it)
	{
		cout << "Case #" << ++i << ": " << get_count(it->first, it->second) << "\n";
	}
}


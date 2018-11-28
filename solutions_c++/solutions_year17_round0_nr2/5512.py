#include <iostream>
#include <vector>
#include <string>

using namespace std;

string get_less(string inp)
{
	for (int i = inp.size() - 1 ; i > 0 ; i--)
	{
		if (inp[i - 1] > inp[i])
		{
			for (int k = i ; k < inp.size(); k++)
				inp[k] = '9';
			inp[i - 1] -= 1;
		}

		if (i - 1 == 0 && inp[i - 1] == '0')
			inp.erase(0, 1);
	}
	return inp;
}

void main()
{
	int T = 0;
	cin >> T;

	vector<string> numbers(T);

	for (int i = 0; i < T; ++i)
	{
		string numb("");
		cin >> numb;

		numbers[i] = numb;
	}

	int i = 0;
	vector<string>::iterator it = numbers.begin();
	for (; it != numbers.end(); ++it)
	{
		cout << "Case #" << ++i << ": " << get_less(*it) << "\n";
	}
}


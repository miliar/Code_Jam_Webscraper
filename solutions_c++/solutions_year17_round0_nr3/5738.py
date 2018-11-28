#include <iostream>
#include <vector>
#include <string>

using namespace std;

void printValues(string inp, int people)
{
	int firstTotal = 0;
	int maxTotal = 0;
	for (int k = 0; k < people; k++)
	{
		firstTotal = 0;
		maxTotal = 0;

		int maxLenght = 0;
		for (int i = 0; i < inp.size(); i++)
		{
			if (inp[i] == '-')
				maxLenght++;
			else
			{
				if (maxLenght > maxTotal)
				{
					maxTotal = maxLenght;
					firstTotal = i - maxTotal;
				}
				maxLenght = 0;
			}
		}
		inp[firstTotal + ((maxTotal % 2 > 0) ? maxTotal / 2 : maxTotal / 2 - 1)] = '+';
	}

	cout << maxTotal / 2 << " " << (maxTotal / 2 - ((maxTotal % 2 == 0) ? 1 : 0));
}

void main()
{
	int T = 0;
	cin >> T;

	vector<pair<string,int> > numbers(T);

	for (int i = 0; i < T; ++i)
	{
		string numb("");
		int stalls = 0, people = 0;
		cin >> stalls >> people;

		numb += '+';
		for (int k = 0; k < stalls; k++)
			numb += '-';
		numb += '+';

		numbers[i] = make_pair(numb, people);
	}

	int i = 0;
	vector<pair<string, int> >::iterator it = numbers.begin();
	for (; it != numbers.end(); ++it)
	{
		cout << "Case #" << ++i << ": "; 
		printValues(it->first, it->second);
		cout << "\n";
	}
}


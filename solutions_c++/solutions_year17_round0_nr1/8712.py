#include<iostream>
#include<string>

using namespace std;

const char negative = '-';
const char positive = '+';

string swap(string toswap, int index , int numofswaps)
{
	for (int i = 0; i < numofswaps; i++)
	{
		if (toswap[index] == negative)
		{
			toswap[index++] = positive;
		}
		else
			toswap[index++] = negative;
	}
	return toswap;
}

int main()
{
	int casecounter = 1;
	int testcase;
	cin >> testcase;
	string row;
	int persons;
	int flipcount = 0;
	int checkingpoint;
	bool possible = true;
	for (int i = 1; i <= testcase; i++)
	{
		cin >> row;
		cin >> persons;
		flipcount = 0;
		checkingpoint = row.length() - persons + 1;
		int index = row.find(negative);
		if (index != string::npos)
		{
			int j;
			for (j = index; j < checkingpoint; j++)
			{
				if (row[j] == negative)
				{
					row = swap(row, j, persons);
					flipcount++;
				}
			}
			for (int k = j; k < (int)row.length(); k++)
			{
				if (row[j++] == negative)
				{
					possible = false;
					break;
				}
			}
		}
		if (possible)
		{
			cout << "Case #" << i << ": " << flipcount << endl;
		}
		else {
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
		}
		possible = true;
	}
	return 0;
}
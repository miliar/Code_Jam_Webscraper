#include <iostream>
#include <string>
#include <math.h>

using namespace std;

typedef enum {TidyNum, Pancake, Bathroom, Fashion}Problems;

static const Problems PROBLEM = Pancake;

void tidyNum(string &numStr)
{
	unsigned int len = numStr.length();
	for (size_t i = 0; i < len - 1; i++)
	{
		string front, end;
		front = numStr.substr(0, len - i - 1);
		end = numStr.substr(len - i - 1);
		if (front[front.length() - 1] > end[0])
		{
			front[front.length() - 1]--;
			end = string(end.length(), '9');
		}
		numStr = front + end;
	}
	cout << atoll(numStr.c_str()) << "\n";
}

void pancakeFlip(string &cakes, int &size)
{
	string result = "IMPOSSIBLE";
	int flipCount = 0;
	for (size_t i = 0; i < cakes.length() - size + 1; i++)
	{
		if (cakes[i] == '-')
		{
			flipCount++;
			for (size_t j = i; j < i + size; j++)
				cakes[j] = cakes[j] == '-' ? '+' : '-';
		}
	}
	if (cakes.substr(cakes.length() - size).find('-') == string::npos)
		cout << flipCount << "\n";
	else
		cout << result << "\n";
}

int main()
{
	unsigned int loopcount;
	cin >> loopcount;
	switch (PROBLEM)
	{
	case TidyNum:
		for (size_t i = 0; i < loopcount; i++)
		{
			string numStr;
			cin >> numStr;
			cout << "Case #" << i + 1 << ": ";
			tidyNum(numStr);
		}
		break;
	case Pancake:
		for (size_t i = 0; i < loopcount; i++)
		{
			string cakes;
			int size;
			cin >> cakes >> size;
			cout << "Case #" << i + 1 << ": ";
			pancakeFlip(cakes, size);
		}
		break;
	case Bathroom:
		for (size_t i = 0; i < loopcount; i++)
		{

		}
		break;
	default:
		break;
	}

	return 0;
}
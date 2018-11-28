#include <iostream>
#include <string>
#include <math.h>

using namespace std;

typedef enum {TidyNum, Pancake, Bathroom, Fashion}Problems;

static const Problems PROBLEM = TidyNum;

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

int main()
{
	unsigned int loopcount;
	switch (PROBLEM)
	{
	case TidyNum:
		cin >> loopcount;
		for (size_t i = 0; i < loopcount; i++)
		{
			string numStr;
			cin >> numStr;
			cout << "Case #" << i + 1 << ": ";
			tidyNum(numStr);
		}
		break;
	default:
		break;
	}

	return 0;
}
#include <iostream>
#include <string>
#include <assert.h>
using namespace std;

void solveIt(int num[], int start, int size);

int main()
{
	int T;
	cin >> T;

	for(int ti = 1; ti <= T; ++ti)
	{
		int digits[200] = {0};
		string num;
		cin >> num;

		int size = num.size();
		assert(size < 200 && size >= 1);
		for(int i = 0; i < size; ++i)
		{
			digits[i] = num[i] - '0';
		}

		solveIt(digits, 0, size);

		int start = 0;
		while(digits[start] == 0) ++start;

		string result;
		for (int i = start; i < size; ++i)
		{
			result.push_back(digits[i] + '0');
		}

		cout << "Case #" << ti << ": " << result << endl;
	}

	return 0;
}

void solveIt(int num[], int start, int size)
{
	if (size == 1)
		return;
	else
	{
		solveIt(num, start + 1, size - 1);

		if (num[start] <= num[start + 1])
			return;
		else
		{
			--num[start];
			for (int i = start + 1; i < start + size; ++i)
			{
				num[i] = 9;
			}
		}
	}
}

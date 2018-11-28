#include <iostream>
#include <queue>

using namespace std;

void work(int &resultA, int &resultB)
{
	int initialSize;
	cin >> initialSize;

	int people;
	cin >> people;

	priority_queue<int> queue;
	queue.push(initialSize);

	for (int n = people - 1; n >= 0; --n)
	{
		int size = queue.top() - 1;
		queue.pop();

		int a, b;

		if (size % 2 == 0)
		{
			a = b = size / 2;
		}
		else
		{
			a = size / 2 + 1;
			b = size / 2;
		}

		queue.push(a);
		queue.push(b);

		if (n == 0)
		{
			resultA = max(a, b);
			resultB = min(a, b);
		}
	}

	/*int last = queue.top() - 1;

	if (last % 2 == 0)
	{
		resultA = resultB = last / 2;
	}
	else
	{
		resultA = last / 2 + 1;
		resultB = last / 2;
	}*/
}

void main()
{
	cin.tie(nullptr);
	ios_base::sync_with_stdio(false);

	int cases;
	cin >> cases;

	for (int n = 0; n < cases; ++n)
	{
		int resultA, resultB;
		work(resultA, resultB);

		cout << "Case #" << n + 1 << ": " << resultA << " " << resultB << endl;
	}
}
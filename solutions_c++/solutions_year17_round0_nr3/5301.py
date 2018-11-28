#include <iostream>
#include <queue>

using namespace std;

int main()
{
	int t;
	cin >> t;

	for(int i = 0; i < t; i++)
	{
		long long unsigned int n, k;
		cin >> n;
		cin >> k;

		priority_queue<long long unsigned int> q;
		long long unsigned int left, right;

		q.push(n);
		for(long long unsigned int j = 0; j < k; j++)
		{
			long long unsigned int max = q.top();
			q.pop();
			max--;
			if(max % 2 == 0)
			{
				left = max / 2;
				right = left;
			}
			else
			{
				left = max / 2;
				right = left + 1;
			}
			q.push(left);
			q.push(right);
		}

		cout << "Case #" << (i + 1) << ": " << right << " " << left << endl;
	}

	return 0;
}


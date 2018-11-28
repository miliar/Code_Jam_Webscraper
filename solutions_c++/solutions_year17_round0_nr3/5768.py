#include <iostream>
#include <queue>

using namespace std;

unsigned long long int getMaxInterval(unsigned long long int N, unsigned long long int K)
{
	priority_queue<unsigned long long int> que;
	
	que.push(N);

	for (int i = 0; i < K - 1; i++)
	{
		unsigned long long int current = que.top();
		que.pop();

		if (current & 1)
		{
			que.push(current / 2);
			que.push(current / 2);
		}
		else
		{
			que.push(current / 2 - 1);
			que.push(current / 2);
		}
	}

	return que.top();
}

int main()
{
	int T;
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		unsigned long long int N, K;
		cin >> N;
		cin >> K;

		unsigned long long int maxInterval = getMaxInterval(N, K);

		cout << "Case #" << i + 1 << ": ";

		if (maxInterval & 1)
		{
			cout << maxInterval / 2 << " " << maxInterval / 2 << endl;
		}
		else
		{
			cout << maxInterval / 2 << " " << maxInterval / 2 - 1 << endl;
		}
	}
}
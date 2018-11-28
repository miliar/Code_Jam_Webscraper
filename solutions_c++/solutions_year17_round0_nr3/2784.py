#include <iostream>
#include <queue>

using namespace std;

int main()
{
	int T; cin >> T;

	for (int t = 0; t < T; t++)
	{
		int N, K;
		cin >> N >> K;

		priority_queue<int> q;
		q.push(N);

		int top = 0;
		for (int i = 0; i < K; i++)
		{
			top = q.top(); q.pop();

			if (top / 2 != 0)
			{
				q.push(top / 2);
			}

			if ((top - 1) / 2 != 0)
			{
				q.push((top - 1) / 2);
			}
		}

		cout << "Case #" << t + 1 << ": " << top / 2 << " " << (top - 1) / 2 << "\n";
	}
}
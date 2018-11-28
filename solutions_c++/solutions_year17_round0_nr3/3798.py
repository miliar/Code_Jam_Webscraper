#include <iostream>
#include <queue>
#include <cmath>

using namespace std;

int main()
{

	int n, k, t;

	cin >> t;
	for(int i = 0; i < t; i++)
	{
		priority_queue<int> q;
		cin >> n >> k;

		q.push(n);

		for(int j = k; j > 1; j--)
		{
			int tmp = q.top();
			q.pop();

			q.push(ceil( (tmp - 1)/2.0 ));
			q.push(floor( (tmp - 1)/2.0 ));
		}

		cout << "Case #" << i + 1 << ": " << ceil( (q.top() - 1)/2.0 ) << " " << floor( (q.top() - 1)/2.0 ) << endl;
	}

	return 0;
}

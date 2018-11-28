#include <iostream>
#include <queue>

using namespace std;

typedef long long ll;

int main() {
	int T;
	cin >> T;

	ll N, K;
	for (int i = 0; i < T; i++)
	{
		cin >> N >> K;
		cout << "Case #" << i + 1 << ": ";

		priority_queue<ll>q;
		q.push(N);

		ll t1, t2;
		while (K > 1)
		{
			t1 = q.top();
			q.pop();
			t2 = t1 / 2;

			if (t1 & 1)
			{
				q.push(t2);
				q.push(t2);
			}
			else {
				q.push(t2);
				q.push(t2 - 1);
			}
			K--;
		}

		t2 = q.top() / 2;

		if (t2 > 0)
		{
			cout << t2 << " " << t2 - (!(q.top() & 1)) << endl;
		}
		else {
			cout << "0 0" << endl;
		}
	}
}

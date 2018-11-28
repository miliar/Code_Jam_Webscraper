#include<iostream>
#include<queue>
using namespace std;
int main(void)
{
	int T;
	cin >> T;
	for (int z = 1; z <= T; ++z)
	{
		int n, k;
		cin >> n >> k;
		priority_queue<int> q;
		q.push(n);
		for (int i = 0; i < k-1; ++i)
		{
			int x = q.top();
			q.pop();
			int a = x/2;
			int b = x - 1 - a;
			if (a > 0)
				q.push(a);
			if (b > 0)
				q.push(b);
		}
		int result = q.top();
		int ans1 = result/2;
		int ans2 = result - 1 - ans1;
		cout << "Case #"  << z << ": " << ans1 << " " << ans2 << endl;
	}
}

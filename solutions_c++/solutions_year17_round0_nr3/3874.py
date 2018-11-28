#include<iostream>
#include <queue>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i<t; i++)
	{
		long long int n, k;
		cin >> n >> k;
		priority_queue<int> q;
		q.push(n);
		cout << "Case #" << i+1 << ": ";
		if (n!=k)
		{
		while(k > 1)
		{
			int x = q.top();
			q.pop();
			if (x%2 == 0)
			{
				q.push(x/2-1);
				q.push(x/2);
			}
			else
			{
				q.push((x-1)/2);
				q.push((x-1)/2);
			}
			k--;
		}
		
		int x = q.top();
		q.pop();
		
		if   (x%2 == 0)
			cout << x/2 << " " << x/2-1 << endl;
		else
			cout << (x-1)/2 << " " << (x-1)/2 << endl;
		}
		else
		{
			cout << "0 0" <<endl;
		}
	}
}

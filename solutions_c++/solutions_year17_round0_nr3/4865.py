#include <bits/stdc++.h>
using namespace std;

priority_queue<int> pq;

void process() {
	int max1 = pq.top();
	// cout << max1 << " ";
	pq.pop();
	pq.push((max1-1)/2);
	pq.push((max1-1) - (max1-1)/2);
}

int main(int argc, char const *argv[])
{
	int t, n, k;
	cin >> t;
	for (int u = 1; u <= t; ++u)
	{
		pq = priority_queue <int>();
		cin >> n >> k;
		pq.push(n);
		for (int i = 0; i < k-1; ++i)
		{
			process();
			/* code */
		}


		cout << "Case #" << u << ": " << (pq.top()-1) - (pq.top()-1)/2 << " " << (pq.top()-1)/2 << "\n";
		/* code */
	}
	return 0;
}
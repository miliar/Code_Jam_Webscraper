#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;


int main()
{
	int t;
	cin>>t;
	int testCaseNum = 0;
	while(t--)
	{
		ull n,k;
		cin>>n>>k;
		testCaseNum++;
		printf("Case #%d: ", testCaseNum);
		if (n == k)
		{
			printf("0 0\n");
			continue;
		}
		ull currentPerson = 0;
		priority_queue<ull> q;
		q.push(n);
		// while(!q.empty())
		while(currentPerson < k-1)
		{
			ull curr = q.top();
			// printf("front is %llu\n", curr);
			if ((curr%2) == 1)
			{
				q.push((curr - 1)/2);
				q.push((curr - 1)/2);
			}
			else
			{
				q.push((curr)/2);
				q.push(((curr)/2) - 1);
			}
			q.pop();
			// q.pop();
			currentPerson++;
		}
		ull big = q.top();
		if ((big%2) == 1)
		{
			printf("%llu %llu\n", (big -1)/2, (big -1)/2 );
		}
		else
		{
			printf("%llu %llu\n", ((big)/2), ((big)/2) - 1);
		}
		// q.pop();
		// ull small = q.top();
	}



	return 0;
}
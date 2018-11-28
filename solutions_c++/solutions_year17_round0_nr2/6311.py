/*
   132->129
   1000->999
   7->7
   111111111111111110->99999999999999999
 */
#include<bits/stdc++.h>

using namespace std;

bool solve(long long int x)
{
	stack<int> s;
	while(x > 0)
	{
		s.push(x%10);
		x /= 10;
	}

	while(!s.empty())
	{
		if(s.size() == 1)
		{
			return true;
		}
		int x;
		int y;
		x = s.top();
		s.pop();



		if(x > s.top())
		{
			return false;
		}
	}
}

int main()
{
	freopen("in1.txt","r",stdin);
	freopen("out1.txt","wb",stdout);

	int t;
	int test = 1;

	cin >> t;

	while(t--)
	{
		long long int n;
		long long int ans = 0;
		cin >> n;

		for(int i = n;i >= 0;i--)
		{
			if(solve(i))
			{
				ans = i;
				break;
			}
		}

		printf("Case #");
		printf("%d",test);
		printf(": ");

		cout << ans << endl;
		test++;
	}
	return 0;
}

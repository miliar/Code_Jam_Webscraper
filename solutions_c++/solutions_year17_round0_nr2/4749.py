#include <iostream>
using namespace std;

bool isAnswer(int n)
{
	int v = 1000;
	while(n)
	{
		if(n % 10 > v)
		{
			return 0;
		}
		v = n % 10;
		n = n / 10;
	}
	return 1;
}

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);

	int tc;

	scanf("%d", &tc);

	for(int t = 1; t <= tc; t++)
	{
		printf("Case #%d: ", t);

		int val;
		cin>>val;

		for(int i = val; i >= 1; i--)
		{
			if(isAnswer(i))
			{
				cout<<i<<endl;
				break;
			}
		}
	}

	return 0;
}
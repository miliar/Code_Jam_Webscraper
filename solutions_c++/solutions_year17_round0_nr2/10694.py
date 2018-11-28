#include<iostream>
#include<vector>
#include<cstdio>
using namespace std;
vector<long long>digist;
int  isTidy(long long n)
{

	long long testNumber = n;
	while (testNumber != 0)
	{
		digist.push_back((testNumber % 10));
		testNumber /= 10;
	}
	bool isNinePos = true;
	for (long long i = 0; i<digist.size(); i++)
	{
		if ((digist[i] != 0 )&&( digist[i] != 1))
		{
			isNinePos = false;
			break;
		}
	}
	if (isNinePos)
	{
		return digist.size() - 1;
	}
	for (long long i = 0; i<digist.size() - 1; i++) {
		if (digist[i] >= digist[i + 1])
		{
			continue;
		}
		else {
			return 0;
		}
	}
	return 1;

}
int main()
{
	//freopen("B-small-attempt5.in", "r", stdin);
	//freopen("B-small-attempt01out.txt", "w", stdout);

	long long t;
	cin >> t;
	long long n;
	for (int i = 1; i <= t; i++)
	{
		cin >> n;
		if (n <= 10)
		{
			if(n==10)
			{
				printf("Case #%d: %lld\n", i, 9);
			}
			else {
				printf("Case #%d: %lld\n", i, n);
			}

			continue;

		}

		for (long long j = n; j >= 1; j--)
		{
			digist.clear();
			long long countIstidy = isTidy(j);
			if (countIstidy == 1)
			{
				printf("Case #%d: %lld\n", i, j);
				break;
			}
			else if (countIstidy != 0)
			{
			    printf("Case #%d: ",i);
				for (int l = 1; l <= countIstidy; l++)
				{
					cout << "9";
				}
				cout << endl;
				break;
			}
		}
	}
	return 0;
}

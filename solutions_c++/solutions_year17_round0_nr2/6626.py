#include <bits/stdc++.h>
using namespace std;
string A;
int main()
{
	long long N;
	cin >> N;
	for (long long x = 1; x <= N; ++x)
	{
		cin >> A;
		for (int i = A.size()-1; i > 0; --i)
		{
			if (A[i] < A[i-1])
			{
				A[i] = '9';
				int j = i;
				while (A[j-1] == '0' && j > 0)
				{
					A[j-1] = '9';
					--j;
				}
				j = i+1;
				while (j < A.size())
				{
					A[j] = '9';
					++j;
				}
				--A[i-1];
			}
		}
		cout << "Case #" << x << ": ";
		if (A.size() > 1)
		{
			if (A[0] != '0')
			{
				cout << A[0];
			}
			for (int i = 1; i < A.size(); ++i)
			{
				cout << A[i];
			}
		}
		else
		{
			cout << A[0];
		}
		cout << "\n";
	}
	return 0;
}
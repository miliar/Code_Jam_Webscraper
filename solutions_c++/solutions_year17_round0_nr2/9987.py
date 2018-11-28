#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;  

bool check(long long N)
{
	string num = to_string(N);
	for (int i = 0; i < num.length() - 1; i++)
	{
		if (num[i] > num[i + 1])
			return false;
	}
	return true;
}

void main()  
{  
	int T;
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		long long N;
		cin >> N;

		for (; N > 0; N--)
		{
			if (check(N))
				break;
		}

		cout << "Case #" << i+1 << ": " << N << endl;
	}
}  
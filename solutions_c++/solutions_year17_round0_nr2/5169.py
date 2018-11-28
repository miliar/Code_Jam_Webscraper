#include<iostream>
#include<algorithm>
#include<vector>
#include<string>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		long long int n;
		cin >> n;

		vector<int> cipher;
		while (n > 0)
		{
			cipher.push_back(n % 10);
			n /= 10;
		}
		int length = cipher.size();
		int pos = 0;
		for (int j = length -1; j > 0; --j)
		{
			if (cipher[j] > cipher[j - 1])
			{
				pos = j;
				while (pos < length && cipher[pos] == cipher[j])
				{
					++pos;
				}
				break;
			}
		}

		if (pos > 0)
		{
			--cipher[pos - 1];
			for (int j = pos - 2; j >= 0; --j)
			{
				cipher[j] = 9;
			}
		}

		if (cipher[length - 1] == 0)
			cipher.pop_back();

		for (int i = cipher.size() - 1; i >= 0; --i)
		{
			n *= 10;
			n += cipher[i];
		}

		cout << "Case #" << i+1 << ": " << n << '\n';
	}
	return 0;
}
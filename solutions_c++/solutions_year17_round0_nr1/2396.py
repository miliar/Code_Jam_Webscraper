#include<iostream>
#include<string>
#include<vector>

using namespace std;

int64_t solve(std::vector<char>& v, size_t K)
{
	int64_t c = 0;
	for (size_t i = 0; i < v.size(); ++i)
	{
		if (v[i] == '-') {
			if (v.size() - i < K)
			{
				return -1;
			}else{
				++c;
				for (size_t j = i; j < i + K; ++j)
				{
					v[j] ^= 6;
				}
			}
		}
	}
	return c;
}

int main()
{
	size_t T; cin >> T;

	for (size_t i = 0; i < T; ++i)
	{
		string S; size_t K; cin >> S >> K;

		vector<char> v(S.begin(), S.begin() + S.length());

		int64_t j = solve(v, K);

		if (j < 0)
		{
			cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
		}
		else {
			cout << "Case #" << i + 1 << ": " << j << endl;
		}

	}

	return 0;
}
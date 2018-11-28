#include<bits/stdc++.h>
/*
*/

using namespace std;

int main() {
	long long int N;
	cin >> N;
	for (size_t i = 0; i < N; i++)
	{
		string S;
		long long int n;
		cin >> S >> n;
		long long int count = 0;
		for (size_t j = 0; j <= S.length() - n; j++)
		{
			if (S[j] == '-')
			{
				for (size_t k = 0; k < n; k++)
				{
					S[j + k] = S[j + k] == '+' ? '-' : '+';
				}
				count++;
			}
		}
		bool f = true;
		for (size_t j = S.length() - n; j < S.length(); j++)
		{
			if (S[j] == '-')
			{
				f = false;
				break;
			}
		}
		cout << "Case #" << i + 1 << ": " << (f ? to_string(count) : "IMPOSSIBLE") << endl;
	}
}

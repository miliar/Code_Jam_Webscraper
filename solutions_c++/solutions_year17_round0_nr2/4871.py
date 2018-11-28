#include<bits/stdc++.h>
/*
*/

using namespace std;


long long int solve(string N) {
	string ret = N;
	for (size_t i = 0; i < ret.size(); i++)
	{
		char now = ret[i];
		bool f = true;
		if (i + 1 < ret.size() && ret[i] < ret[i + 1])
		{
			continue;
		}
		for (size_t j = i; j < ret.size(); j++)
		{
			if (now > ret[j])
			{
				f = false;
			}
		}
		if (!f)
		{
			ret[i]--;
			for (size_t j = i + 1; j < ret.size(); j++)
			{
				ret[j] = '9';
			}
		}
	}
	return stoll(ret);
}

int main() {

	long long int T;
	cin >> T;
	for (size_t index = 0; index < T; index++)
	{
		long long int N;
		cin >> N;
		long long int prev9 = 0, now9 = 0;
		while (now9 <= N)
		{
			prev9 = now9;
			now9 *= 10;
			now9 += 9;
		}

		cout << "Case #" << index + 1 << ": " << max(prev9, solve(to_string(N))) << endl;
	}
}

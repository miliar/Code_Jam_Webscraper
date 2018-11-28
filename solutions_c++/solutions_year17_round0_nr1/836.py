#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string flipgame(string S, int K)
{
	int i = 0, res = 0;
	while (i + K <= S.size())
	{
		int start = i, count = 0;
		while (i + K <= S.size() && S[i] == '-' && count < K)
		{
			i++;
			count++;
		}
		if (count == 0)
		{
			i++;
			continue;
		}
		int end = min((int)S.size(), start + K);
		for (int j = start; j < end; ++j)
		{
			S[j] = S[j] == '+' ? '-' : '+';
		}
		res++;
	}
	bool success = true;
	for (auto it : S)
	{
		if (it != '+')
		{
			success = false;
			break;
		}
	}
	if (!success) return "IMPOSSIBLE";
	return to_string(res);
}

int main(int argc, char* argv[])
{
	int t;
	cin >> t;
	
	for (int i = 1; i <= t; ++i)
	{
		string S;
		int K;
		cin >> S;
		cin >> K;
		string res = flipgame(S, K);

		cout << "Case #" << i << ": " << res <<'\n';
	}
	return 0;
}
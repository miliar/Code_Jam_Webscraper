#include<iostream>
#include<string>

using namespace std;

string Solve(string s, int k)
{
	int cnt = 0; int n = s.size();
	bool *flag = new bool[n];
	for (int i = 0; i < n; i++) flag[i] = s[i] == '+';
	for (int i = 0; i <= n - k; i++)
	{
		if (!flag[i])
		{
			for (int j = 0; j < k; j++) flag[i + j] = !flag[i + j];
			cnt++;
		}
	}
	for (int i = n - k + 1; i < n; i++) if (!flag[i]) return "IMPOSSIBLE";
	return std::to_string(cnt);
}

int main()
{
	int T, K;
	string S;
	cin >> T;
	for (int c = 1; c <= T; c++)
	{
		cin >> S >> K;
		cout << "Case #" << c << ": " << Solve(S, K) << endl;
	}
}


#include <iostream>
#include <vector>
#include <deque>
#include <unordered_map>
#include <algorithm>
#include <unordered_set>
#include <string>

using namespace std;

string S;
int T,K;

int solve()
{
	bool flips[1001]{ 0 };
	int n = S.length(), res=0,i;

	for(i = 0; i <= n-K; ++i)
	{
		bool cur = (S[i] == '+' ? 0 : 1);
		if(cur ^ flips[i])
		{
			++res;
			for (int j = i + 1; j < min(n, i + K); ++j)
				flips[j] = !flips[j];
		}
	}

	while (i < n)
	{
		bool cur = (S[i] == '+' ? 0 : 1);
		if (cur ^ flips[i]) return -1;
		++i;
	}

	return res;
}

int main()
{
	cin >> T;

	for(int i = 0; i < T; ++i)
	{
		cin >> S >> K;
		int r = solve();
		cout << "Case #" << i + 1 << ": ";
		if (r >= 0) cout << r; else cout << "IMPOSSIBLE";
		cout << endl;
	}
}
#include <iostream>
#include <string>

using namespace std;

bool flip (string &s, int i, int K)
{
	if (i+K > s.size()) return false;
	for(int j = i; j < i + K; j++)
	{
		s[j] = (s[j] == '-')?'+':'-'; 
	}
	return true;
}

int main()
{
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		string s;
		cin >> s;
		int K;
		cin >> K;
		bool done = true;
		int count = 0;
		int n = s.size();
		for (int i = 0; i <= n; ++i)
		{
			if (s[i] == '-')
			{
				if (!flip(s, i, K))
				{
					done = false;
					break;
				}
				count++;
			}
		}
		
		cout << "Case #" << t+1 << ": ";
		if (done)
			cout << count << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}

}
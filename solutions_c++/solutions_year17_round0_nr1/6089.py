#include <iostream>
#include <vector>
#include <string>

using namespace std;

int doCase()
{
	string S;
	cin >> S;
	int len = S.length();
	int K;
	cin >> K;

	vector<bool> pancake(len, 0);
	for (int i=0; i<len; i++)
		if (S[i] == '+')
			pancake[i] = 1;

	int flips = 0;
	for (int i=0; i<len-K+1; i++)
	{
		if (!pancake[i])
		{
			flips++;
			for (int j=0; j<K; j++)
				pancake[i+j] = 1-pancake[i+j];
		}
	}
	for (int i=len-K+1; i<len; i++)
		if (!pancake[i])
			return -1;
	return flips;
}

int main()
{
	int T;
	cin >> T;
	for (int i=0; i<T; i++)
	{
		cout << "Case #" << i+1 << ": ";
		int ans = doCase();
		if (ans<0) cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl;
	}
	return 0;
}
#include <iostream>
#include <string>
#include <bitset>

using namespace std;

#define BMAX 1001

int main() {

	int T;
	cin >> T;

	string S;
	int K;
	for (int i = 0; i < T; i++)
	{
		cin >> S >> K;

		cout << "Case #" << i + 1 << ": ";

		bitset<BMAX> b;

		for (int j = 0; j < S.size(); j++)
		{
			if (S[j] == '+')
			{
				b.set(S.size() - j - 1);
			}

		}

		bitset<BMAX> z;

		for (int j = 0; j < K; j++)
		{
			z.set(j);
		}

		int ans = 0;
		int lmost = S.size() - K + 1;

		for (int j = 0; j < lmost; j++)
		{
			if (!b.test(j))
			{
				ans++;
				b ^= z;
			}

			z <<= 1;
		}
		
		bool t = true;

		for (int j = 0; j < K - 1; j++)
		{
			if (!b.test(j + lmost))
			{
				t = false;
				break;
			}
		}

		if (t)
		{
			cout << ans << endl;
		}
		else {
			cout << "IMPOSSIBLE" << endl;
		}
	}

}

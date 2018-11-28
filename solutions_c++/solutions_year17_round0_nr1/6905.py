#include <iostream>

using namespace std;

const int kMaxLength = 1000;

void Solve()
{
	int K;
	char S[kMaxLength + 1];
	cin >> S >> K;

	int now;
	int cnt = 0;
	for (now = 0; now + K - 1 < strlen(S); now++)
		if (S[now] == '-')
		{
			for (int i = now; i <= now + K - 1; i++)
				S[i] = (S[i] == '-') ? '+' : '-';
			cnt++;
		}

	for (now = 0; now < strlen(S); now++)
		if (S[now] == '-')
		{
			cout << "IMPOSSIBLE";
			return;
		}
	cout << cnt;
}

int main()
{
	int T;
	cin >> T;
	for (int now = 1; now <= T; now++)
	{
		cout << "Case #" << now << ": ";
		Solve();
		cout << endl;
	}
	return 0;
}
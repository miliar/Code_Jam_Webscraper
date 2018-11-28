#include <iostream>

using namespace std;

const int kMaxDigit = 19;

void Solve()
{
	//long long N;
	
	char N[kMaxDigit + 1];
	//long long digit[kMaxDigit+1];
	//digit[1] = 1;
	//for (int now = 2; now <= kMaxDigit; now++)
	//	digit[now] = digit[now - 1] * 10;

	cin >> N;

	int now = strlen(N) - 1;
	while (now > 0 && N[now - 1])
	{
		if (N[now - 1] > N[now])
		{
			N[now - 1]--;
			for (int i = now; i < strlen(N); i++)
				N[i] = '9';
		}

		now--;
	}	

	if (N[0] == '0')
		cout << N + 1;
	else
		cout << N;
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
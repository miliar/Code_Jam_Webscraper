#include <iostream>
#include <string>
using namespace std;

void run();

int main()
{
	long T;
	cin >> T;

	for (int c = 1; c <= T; ++c)
	{
		cout << "Case #" << c << ": ";
		run();
	}
}

void run()
{
	std::string S;
	cin >> S;

	long K;
	cin >> K;
	long length = S.length();

	long N = 0;

	for (long i = 0; i < length; ++i)
	{
		if (S[i] == '-')
		{
			if (i + K > length)
			{
				cout << "IMPOSSIBLE" << endl;
				return;
			}

			++N;
			//S[i] = '+'; //unnecessary
			for (long j = 1; j < K; ++j)
			{
				S[i + j] = S[i + j] == '+' ? '-' : '+';
			}
		}
	}

	cout << N << endl;
}
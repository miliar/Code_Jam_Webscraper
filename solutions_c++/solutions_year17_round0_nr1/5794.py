#include "stdafx.h"

typedef long long i64;
typedef unsigned long long u64;

//void init();
void go(int caseN);

//------------------------------------------------------------------------------------------------------------------------------
int main()
{
	//init();

	ifstream in("A-small-attempt0.in");
	ofstream out("out.txt");
	cin.rdbuf(in.rdbuf());
	cout.rdbuf(out.rdbuf());

	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) go(t);
	return 0;
}

//------------------------------------------------------------------------------------------------------------------------------
void go(int caseN)
{
	string S;
	int K;
	cin >> S >> K;

	cout << "Case #" << caseN << ": ";

	int flips = 0;
	for (int i = 0; i < S.length(); ++i)
	{
		if (S[i] == '-')
		{
			for (int j = 0; j < K; ++j)
			{
				if (i + j >= S.length())
				{
					cout << "IMPOSSIBLE" << endl;
					return;
				}
				S[i + j] = ((S[i + j] - '+') ^ 2) + '+';
			}
			++flips;
		}
	}

	cout << flips << endl;
}

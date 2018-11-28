#include "stdafx.h"

typedef long long i64;
typedef unsigned long long u64;

void go(int caseN);

//------------------------------------------------------------------------------------------------------------------------------
int main()
{
	ifstream in("in.txt");
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
	string N;
	cin >> N;

	cout << "Case #" << caseN << ": ";

	int last = N.length() - 1;
	for (int i = last - 1; i >= 0; --i)
	{
		if (N[i] > N[last])
		{
			for (int j = i + 1; j < N.length(); ++j) N[j] = '9';
			--N[i];
		}
		last = i;
	}

	if (N[0] == '0') N = N.substr(1);

	cout << N << endl;
}

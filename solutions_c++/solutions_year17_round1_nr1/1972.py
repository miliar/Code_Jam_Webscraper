#include "stdafx.h"

typedef long long i64;
typedef unsigned long long u64;

//void init();
void go(int caseN);

//------------------------------------------------------------------------------------------------------------------------------
int main()
{
	//init();

	ifstream in("in.txt");
	ofstream out("out.txt");
	cin.rdbuf(in.rdbuf());
	cout.rdbuf(out.rdbuf());

	int T; 
	cin >> T;
	for (int t = 1; t <= T; ++t) go(t);
    return 0;
}

char rc[25][25];

//------------------------------------------------------------------------------------------------------------------------------
void go(int caseN)
{
	int R,C;
	cin >> R >> C;

	cout << "Case #" << caseN << ":" << endl;

	//char* rc = new char[R * C];

	for (int r = 0; r < R; ++r)
	{
		for (int c = 0; c < C; ++c)
		{
			cin >> rc[r][c];
		}
	}


	for (int r = 0; r < R; ++r)
	{
		char x = '?';
		for (int c = 0; c < C; ++c)
		{
			if (rc[r][c] != '?')
			{
				x = rc[r][c];
				break;
			}
		}

		if (x == '?') continue;

		for (int c = 0; c < C; ++c)
		{
			if (rc[r][c] == '?')
			{
				rc[r][c] = x;
			}
			else
			{
				x = rc[r][c];
			}
		}
	}


	for (int c = 0; c < C; ++c)
	{
		char x = '?';
		for (int r = 0; r < R; ++r)
		{
			if (rc[r][c] != '?')
			{
				x = rc[r][c];
				break;
			}
		}

		if (x == '?') continue;

		for (int r = 0; r < R; ++r)
		{
			if (rc[r][c] == '?')
			{
				rc[r][c] = x;
			}
			else
			{
				x = rc[r][c];
			}
		}
	}



	for (int r = 0; r < R; ++r)
	{
		for (int c = 0; c < C; ++c)
		{
			cout << rc[r][c];
		}
		cout << endl;
	}
}

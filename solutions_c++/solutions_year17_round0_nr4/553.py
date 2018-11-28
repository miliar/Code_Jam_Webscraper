/*
ID: paradoxes
PROG: Fashion Show
LANG: C++
*/

#include<iostream>
#include<fstream>

using namespace std;

int T;

int N, M;

int counter;

bool bish[101][101], rook[101][101];

bool rook_col[101][2];

int abish[101][101], arook[101][101];
int add[101][101];

void clean()
{
	counter = 0;

	for (int i = 0; i <= N; i++)
	{
		rook_col[i][0] = false;
		rook_col[i][1] = false;

		for (int j = 0; j <= N; j++)
		{
			bish[i][j] = false;
			rook[i][j] = false;

			add[i][j] = 0;
		}
	}
}

void do_bish()
{
	for (int i = 1; i <= N; i++)
	{
		if (!bish[1][i])
		{
			if (rook[1][i])
				add[1][i] = 3;
			else
				add[1][i] = 1;

			counter++;
		}
	}

	for (int i = 2; i < N; i++)
	{
		add[N][i] = 1;

		counter++;
	}

	return;
}

void do_rook()
{
	for(int i = 1; i <= N; i++)
	{
		if (rook_col[i][1])
			continue;

		for (int j = 1; j <= N; j++)
		{
			if (!rook_col[j][0])
			{
				rook_col[i][1] = true;
				rook_col[j][0] = true;

				if (add[j][i] == 1)
				{
					add[j][i] = 3;
					break;
				}

				if (bish[j][i])
				{
					add[j][i] = 3;
					counter++;
					break;
				}

				else
				{
					add[j][i] = 2;
					counter++;
					break;
				}
			}
		}

	}

	return;
}

int main()
{
	ifstream Input("fashion.in");
	ofstream Output("fashion.out");

	Input >> T;

	char a;

	int r, c;

	for (int j = 1; j <= T; j++)
	{
		Input >> N >> M;

		if (N == 1)
		{
			if(M == 0)
			{
				Output << "Case #" << j << ": " << 2 << " " << 1 << endl;
				Output << "o 1 1" << endl;
				continue;
			}

			Input >> a >> r >> c;

			if (a == 'o')
			{
				Output << "Case #" << j << ": " << 2 << " " << 0 << endl;
				continue;
			}

			else
			{
				Output << "Case #" << j << ": " << 2 << " " << 1 << endl;
				Output << "o 1 1" << endl;
				continue;
			}
		}

		clean();

		for (int i = 0; i < M; i++)
		{
			Input >> a >> r >> c;

			switch (a)
			{
			case '+':
				bish[r][c] = true;
				break;
			case 'x':
				rook[r][c] = true;
				rook_col[r][0] = true;
				rook_col[c][1] = true;
				break;
			case 'o':
				bish[r][c] = true;
				rook[r][c] = true;
				rook_col[r][0] = true;
				rook_col[c][1] = true;
				break;
			default:
				cerr << "Error 1" << endl;
			}
		}

		do_bish();
		do_rook();

		Output << "Case #" << j << ": " << 3*N - 2 << " " << counter << endl;

		for (int i = 1; i <= N; i++)
		{
			for (int j = 1; j <= N; j++)
			{
				if (add[i][j] == 0)
					continue;
				
				if (add[i][j] == 1)
				{
					Output << "+" << " " << i << " " << j << endl;
					continue;
				}

				if (add[i][j] == 2)
				{
					Output << "x" << " " << i << " " << j << endl;
					continue;
				}

				if (add[i][j] == 3)
				{
					Output << "o" << " " << i << " " << j << endl;
					continue;
				}
			}
		}
	}

	return 0;
}
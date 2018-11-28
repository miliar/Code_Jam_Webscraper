#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void greedyCut(int istart, int jstart, int R, int C, char *cake, bool *cut)
{
	//cout << "start " << istart << " " << jstart << endl;
	bool letterfound = false;
	char letter;
	int jend = jstart;
	int letterrow = -1;
	for (int k = jstart; k < C; k++)
	{
		if (cake[istart*C + k] != '?')
		{
			if (!letterfound)
			{
				letterfound = true;
				letter = cake[istart*C + k];
				letterrow = istart;
			}
			else
			{
				break;
			}
		}
		jend = k;
	}

	//cout << "jend is " << jend << endl;

	int iend = istart;
	for (int k = iend+1; k < R; k++)
	{
		bool ok = true;
		for (int l = jstart; l <= jend; l++)
		{
			if (cake[k*C + l] != '?')
			{
				if (!letterfound)
				{
					letterfound = true;
					letter = cake[k*C + l];
					letterrow = k;
				}
				else
				{
					if (k == letterrow)
					{
						//cout << "in " << k << " " << letterrow << endl;
						jend = l - 1;
					}
					ok = false;
					break;
				}
			}
		}
		if (!ok)
			break;
		iend = k;
	}
	for (int i = istart; i <= iend; i++)
	{
		for (int j = jstart; j <= jend; j++)
		{
			cake[i*C + j] = letter;
			cut[i*C + j] = true;
		}
	}
}

void doCase()
{
	cout << endl;
	int R, C;
	cin >> R >> C;
	char *cake = new char[R*C];
	bool *cut = new bool[R*C];
	for (int i = 0; i < R; i++)
	{
		for (int j = 0; j < C; j++)
		{
			cin >> cake[i*C + j];
			cut[i*C + j] = false;
		}
	}
	for (int i = 0; i < R; i++)
	{
		for (int j = 0; j < C; j++)
		{
			if (cut[i*C + j])
				continue;
			greedyCut(i, j, R, C, cake, cut);
		}
		
	}

	for (int i = 0; i < R; i++)
	{
		for (int j = 0; j < C; j++)
		{
			cout << cake[i*C + j];
		}
		cout << endl;
	}

	delete[] cake;
}

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		doCase();
	}
}
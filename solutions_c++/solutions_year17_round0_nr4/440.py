#include <cstdio>
#include <string>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;

struct cell
{
	char ch;
	bool xshadow;
	bool pshadow;

};



int main(int argc, char *argv[])
{
	FILE *fin, *fout;
	if (argc > 1)
	{
		char tname[200];
		fin = fopen(argv[1], "r");
		strncpy(tname, argv[1], 200);
		strncpy(strstr(tname, ".in"), ".out", 4);
		fout = fopen(tname, "w");
	}
	else {
		fin = fopen("A.in", "r");
		fout = fopen("A.out", "w");
	}


	int t;
	fscanf(fin, "%d", &t);
	cell board[100][100];
	char startconf[100][100];
	for (int ti = 0; ti<t; ti++)
	{
		int n;
		int m;
		fscanf(fin, "%i", &n);
		fscanf(fin, "%i", &m);
		for (int i = 0; i < n; ++i)
		{
			int gi = (i < (n - 1 - i)) ? i : n - 1 - i;
			for (int j = 0; j < n; ++j)
			{
				int gj = (j < (n - 1 - j)) ? i : n - 1 - j;
				if (gj > gi) gj = gi;
				board[i][j].ch = '.';
				startconf[i][j] = '.';
				board[i][j].xshadow = false;
				board[i][j].pshadow = false;
			}
		}
		int oi[10000];
		int oj[10000];
		int loc = 0;
		int gs = n / 2;
		for (int i = 0; i < gs; ++i)
		{
			for (int j = i; j < gs; ++j)
			{
				oi[loc] = i;
				oj[loc] = j;
				++loc;
				oi[loc] = i;
				oj[loc] = n -1 - j;
				++loc;
				oi[loc] = n - 1 - i; 
				oj[loc] = j;
				++loc;
				oi[loc] = n - 1 - i; 
				oj[loc] = n - 1 - j;
				++loc;
			}
			for (int j = i+1; j < gs; ++j)
			{
				oi[loc] = j;
				oj[loc] = i;
				++loc;
				oi[loc] = n - 1 - j;
				oj[loc] = n - 1 - j;
				++loc;
				oi[loc] = j;
				oj[loc] = n - 1 - i;
				++loc;
				oi[loc] = n - 1 - j;
				oj[loc] = n - 1 - i;
				++loc;
			}
			if (n & 1 == 1)
			{
				oi[loc] = i;
				oj[loc] = gs;
				++loc;
				oi[loc] = n - 1 - i;
				oj[loc] = gs;
				++loc;
				oi[loc] = gs;
				oj[loc] = i;
				++loc;
				oi[loc] = gs;
				oj[loc] = n - 1 - i;
				++loc;
			}
		}
		if (n & 1 == 1)
		{
			oi[loc] = gs;
			oj[loc] = gs;
			++loc;
		}

		char buffer[1000];
		fgets(buffer, 100, fin);
		for (int i = 0; i < m; ++i)
		{
			char tch;
			int tti;
			int ttj;
			fscanf(fin, "%c", &tch);
			fscanf(fin, "%i", &tti);
			fscanf(fin, "%i", &ttj);
			--tti;
			--ttj;
			board[tti][ttj].ch = tch;
			startconf[tti][ttj] = tch;
			if (tch == '+' || tch == 'o')
			{
				for (int p = 0; p < n; ++p)
				{
					int tr = ttj + (p - tti);
					if (tr >= 0 && tr < n) board[p][tr].pshadow = true;
					tr = ttj + (tti-p);
					if (tr >= 0 && tr < n) board[p][tr].pshadow = true;
				}
			}
			if (tch == 'x' || tch == 'o')
			{
				for (int p = 0; p < n; ++p)
				{
					board[p][ttj].xshadow = true;
					board[tti][p].xshadow = true;
				}
			}
			fgets(buffer, 100, fin);
		}
//		int gs = (n + 1) / 2;
		for (int i = 0; i < loc; ++i)
		{
			int tti = oi[i];
			int ttj = oj[i];
			if (board[tti][ttj].ch == '.')
			{
				if (!board[tti][ttj].pshadow)
				{
					board[tti][ttj].ch = '+';
					for (int p = 0; p < n; ++p)
					{
						int tr = ttj + (p - tti);
						if (tr >= 0 && tr < n) board[p][tr].pshadow = true;
						tr = ttj + (tti - p);
						if (tr >= 0 && tr < n) board[p][tr].pshadow = true;
					}
				} else if (!board[tti][ttj].xshadow)
				{
					board[tti][ttj].ch = 'x';
					for (int p = 0; p < n; ++p)
					{
						board[p][ttj].xshadow = true;
						board[tti][p].xshadow = true;
					}
				}
			}
		}

		for (int i = 0; i < loc; ++i)
		{
			int tti = oi[i];
			int ttj = oj[i];
			if (board[tti][ttj].ch == '+')
			{
				if (!board[tti][ttj].xshadow)
				{
					board[tti][ttj].ch = 'o';
					for (int p = 0; p < n; ++p)
					{
						board[p][ttj].xshadow = true;
						board[tti][p].xshadow = true;
					}
				}
			}
			if (board[tti][ttj].ch == 'x')
			{
				if (!board[tti][ttj].pshadow)
				{
					board[tti][ttj].ch = 'o';
					for (int p = 0; p < n; ++p)
					{
						int tr = ttj + (p - tti);
						if (tr >= 0 && tr < n) board[p][tr].pshadow = true;
						tr = ttj + (tti - p);
						if (tr >= 0 && tr < n) board[p][tr].pshadow = true;
					}
				}
			}
		}
		int score = 0;
		int changes = 0;
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < n; ++j)
			{
				if (board[i][j].ch == 'x' || board[i][j].ch == '+')
				{
					++score;
				} 	else if (board[i][j].ch == 'o')
				{
					score +=2;
				}

				if (board[i][j].ch != startconf[i][j]) ++changes;
			}
		}

		fprintf(fout, "Case #%d: %i %i\n", ti + 1, score, changes);
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < n; ++j)
			{
				if (board[i][j].ch != startconf[i][j])
				{
					fprintf(fout, "%c %i %i\n", board[i][j].ch, i+1, j+1);
				}

			}
		}
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
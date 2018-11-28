#include <cstdio>
#include <cstring>

using namespace std;

struct cell
{
	char ch;
	bool nox;
	bool noplus;
};

int set_order(int n, int * rowp, int * colp)
{
	int gs = n / 2;
	int curpos = 0;
	for (int i = 0; i < gs; ++i)
	{
		for (int j = i; j < gs; ++j)
		{
			rowp[curpos] = i;
			colp[curpos] = j;
			++curpos;
			rowp[curpos] = i;
			colp[curpos] = n - 1 - j;
			++curpos;
			rowp[curpos] = n - 1 - i;
			colp[curpos] = j;
			++curpos;
			rowp[curpos] = n - 1 - i;
			colp[curpos] = n - 1 - j;
			++curpos;
		}
		for (int j = i + 1; j < gs; ++j)
		{
			rowp[curpos] = j;
			colp[curpos] = i;
			++curpos;
			rowp[curpos] = n - 1 - j;
			colp[curpos] = n - 1 - j;
			++curpos;
			rowp[curpos] = j;
			colp[curpos] = n - 1 - i;
			++curpos;
			rowp[curpos] = n - 1 - j;
			colp[curpos] = n - 1 - i;
			++curpos;
		}
		if (n & 1 == 1)
		{
			rowp[curpos] = i;
			colp[curpos] = gs;
			++curpos;
			rowp[curpos] = n - 1 - i;
			colp[curpos] = gs;
			++curpos;
			rowp[curpos] = gs;
			colp[curpos] = i;
			++curpos;
			rowp[curpos] = gs;
			colp[curpos] = n - 1 - i;
			++curpos;
		}
	}
	if (n & 1 == 1)
	{
		rowp[curpos] = gs;
		colp[curpos] = gs;
		++curpos;
	}
	return curpos;
}


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
	cell stage[100][100];
	char stage_ini[100][100];
	int * rowp = new int[10000];
	int * colp = new int[10000];
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
				stage[i][j].ch = '.';
				stage_ini[i][j] = '.';
				stage[i][j].nox = false;
				stage[i][j].noplus = false;
			}
		}

		int ncell = set_order(n, rowp, colp);
		char buffer[1000];
		fgets(buffer, 100, fin);
		for (int i = 0; i < m; ++i)
		{
			char tch;
			int ii;
			int jj;
			fscanf(fin, "%c", &tch);
			fscanf(fin, "%i", &ii);
			fscanf(fin, "%i", &jj);
			--ii;
			--jj;
			stage[ii][jj].ch = tch;
			stage_ini[ii][jj] = tch;
			if (tch == '+' || tch == 'o')
			{
				for (int p = 0; p < n; ++p)
				{
					int tr = jj + (p - ii);
					if (tr >= 0 && tr < n) stage[p][tr].noplus = true;
					tr = jj + (ii - p);
					if (tr >= 0 && tr < n) stage[p][tr].noplus = true;
				}
			}
			if (tch == 'x' || tch == 'o')
			{
				for (int p = 0; p < n; ++p)
				{
					stage[p][jj].nox = true;
					stage[ii][p].nox = true;
				}
			}
			fgets(buffer, 100, fin);
		}

		for (int i = 0; i < ncell; ++i)
		{
			int ii = rowp[i];
	      	int jj = colp[i];
				if (stage[ii][jj].ch == '.')
				{
					if (!stage[ii][jj].noplus)
					{
						stage[ii][jj].ch = '+';
						for (int p = 0; p < n; ++p)
						{
							int tr = jj + (p - ii);
							if (tr >= 0 && tr < n) stage[p][tr].noplus = true;
							tr = jj + (ii - p);
							if (tr >= 0 && tr < n) stage[p][tr].noplus = true;
						}
					}
					else if (!stage[ii][jj].nox)
					{
						stage[ii][jj].ch = 'x';
						for (int p = 0; p < n; ++p)
						{
							stage[p][jj].nox = true;
							stage[ii][p].nox = true;
						}
					}
				}
		}

		for (int i = 0; i < ncell; ++i)
		{
			int ii = rowp[i];
			int jj = colp[i];

			if (stage[ii][jj].ch == '+')
			{
				if (!stage[ii][jj].nox)
				{
					stage[ii][jj].ch = 'o';
					for (int p = 0; p < n; ++p)
					{
						stage[p][jj].nox = true;
						stage[ii][p].nox = true;
					}
				}
			}
			if (stage[ii][jj].ch == 'x')
			{
				if (!stage[ii][jj].noplus)
				{
					stage[ii][jj].ch = 'o';
					for (int p = 0; p < n; ++p)
					{
						int tr = jj + (p - ii);
						if (tr >= 0 && tr < n) stage[p][tr].noplus = true;
						tr = jj + (ii - p);
						if (tr >= 0 && tr < n) stage[p][tr].noplus = true;
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
				if (stage[i][j].ch == 'x' || stage[i][j].ch == '+')
				{
					++score;
				}
				else if (stage[i][j].ch == 'o')
				{
					score += 2;
				}

				if (stage[i][j].ch != stage_ini[i][j]) ++changes;
			}
		}

		fprintf(fout, "Case #%d: %i %i\n", ti + 1, score, changes);
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < n; ++j)
			{
				if (stage[i][j].ch != stage_ini[i][j])
				{
					fprintf(fout, "%c %i %i\n", stage[i][j].ch, i + 1, j + 1);
				}

			}
		}
	}
	delete[] rowp;
	delete[] colp;
	fclose(fin);
	fclose(fout);
	return 0;
}
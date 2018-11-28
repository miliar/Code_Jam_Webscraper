#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

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
	char abuffer[2000];
	for (int ti = 0; ti<t; ti++)
	{
		int n, r, o, y, g, b, v;
		fscanf(fin, "%d", &n);
		fscanf(fin, "%d", &r);
		fscanf(fin, "%d", &o);
		fscanf(fin, "%d", &y);
		fscanf(fin, "%d", &g);
		fscanf(fin, "%d", &b);
		fscanf(fin, "%d", &v);
		int pos = 0;
		char curc = 'R';
		int * cmax = &r;
		if (o > *cmax)
		{
			curc = 'O';
			cmax = &o;
		}
		if (y > *cmax) 
		{
			curc = 'Y';
			cmax = &y;
		}
		if (g > *cmax)
		{
			curc = 'G';
			cmax = &g;
		}
		if (b > *cmax)
		{
			curc = 'B';
			cmax = &b;
		}
		if (v > *cmax)
		{
			curc = 'V';
			cmax = &v;
		}
		abuffer[pos++] = curc;
		(*cmax)--;
		n--;
		char nextc = 0;
		bool possible = true;
		while (n > 0)
		{
			nextc = 0;
			if (curc == 'R')
			{
				if (g > 0)
				{
					abuffer[pos++] = 'G';
					g--;
					n--;
					curc = 'G';
					if (r > 0)
					{
						abuffer[pos++] = 'R';
						r--;
						n--;
						curc = 'R';
					}
				}
				else {
					cmax = &y;
					nextc = 'Y';
					if (b > *cmax)
					{
						cmax = &b;
						nextc = 'B';
					} else if (b == *cmax && abuffer[0] == 'B')
					{
						cmax = &b;
						nextc = 'B';
					}

					if (*cmax > 0)
					{
						abuffer[pos++] = nextc;
						curc = nextc;
						(*cmax)--;
						n--;
					}
					else {
						possible = false;
						break;
					}
				}
			} else 	if (curc == 'O')
			{
				if (b > 0)
				{
					abuffer[pos++] = 'B';
					b--;
					n--;
					curc = 'B';
				}	else {
					possible = false;
					break;
				}
			}
			else if (curc == 'Y')
			{
				if (v > 0)
				{
					abuffer[pos++] = 'V';
					v--;
					n--;
					curc = 'V';
					if (y > 0)
					{
						abuffer[pos++] = 'Y';
						curc = 'Y';
						y--;
						n--;
					}
				}
				else {
					cmax = &r;
					nextc = 'R';
					if (b > *cmax)
					{
						cmax = &b;
						nextc = 'B';
					}
					else if (b == *cmax && abuffer[0] == 'B')
					{
						cmax = &b;
						nextc = 'B';
					}

					if (*cmax > 0)
					{
						abuffer[pos++] = nextc;
						curc = nextc;
						(*cmax)--;
						n--;
					}
					else {
						possible = false;
						break;
					}
				}
			}
			else if (curc == 'G')
			{
				if (r > 0)
				{
					abuffer[pos++] = 'R';
					r--;
					n--;
					curc = 'R';
				}
				else {
					possible = false;
					break;
				}
			}
			else if (curc == 'B')
			{
				if (o > 0)
				{
					abuffer[pos++] = 'O';
					o--;
					n--;
					curc = 'O';
					if (b > 0)
					{
						abuffer[pos++] = 'B';
						curc = 'B';
						b--;
						n--;
					}
				}
				else {
					cmax = &r;
					nextc = 'R';
					if (y > *cmax)
					{
						cmax = &y;
						nextc = 'Y';
					}
					else if (y == *cmax && abuffer[0] == 'Y')
					{
						cmax = &y;
						nextc = 'Y';
					}

					if (*cmax > 0)
					{
						abuffer[pos++] = nextc;
						curc = nextc;
						(*cmax)--;
						n--;
					}
					else {
						possible = false;
						break;
					}
				}
			}
			else if (curc == 'V')
			{
				if (y > 0)
				{
					abuffer[pos++] = 'Y';
					y--;
					n--;
					curc = 'Y';
				}
				else {
					possible = false;
					break;
				}
			}
		}
		if (possible)
		{
			if (abuffer[0] == 'R')
			{
				if(abuffer[pos-1] == 'R' || abuffer[pos - 1] == 'O' || abuffer[pos - 1] == 'V') possible = false;
			} else if (abuffer[0] == 'O')
			{
				if (abuffer[pos - 1] != 'B') possible = false;
			}
			else if (abuffer[0] == 'Y')
			{
				if (abuffer[pos - 1] == 'Y' || abuffer[pos - 1] == 'O' || abuffer[pos - 1] == 'G') possible = false;
			}
			else if (abuffer[0] == 'G')
			{
				if (abuffer[pos - 1] != 'R' ) possible = false;
			}
			else if (abuffer[0] == 'B')
			{
				if (abuffer[pos - 1] == 'B' || abuffer[pos - 1] == 'G' || abuffer[pos - 1] == 'V') possible = false;
			}
			else if (abuffer[0] == 'V')
			{
				if (abuffer[pos - 1] != 'Y' ) possible = false;
			}
		}
		if (possible)
		{
			abuffer[pos] = 0;
			fprintf(fout, "Case #%d: %s\n", ti + 1, abuffer);
		}
		else {
			fprintf(fout, "Case #%d: IMPOSSIBLE\n", ti + 1);
		}
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
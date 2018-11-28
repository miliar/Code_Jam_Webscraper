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
	string cake[25];
	bool ul[256];
	for (int ti = 0; ti<t; ti++)
	{
		int r, c;
		fscanf(fin, "%d", &r);
		fscanf(fin, "%d", &c);
		char buffer[100];
		for (int ir = 0; ir < r; ++ir)
		{
			fscanf(fin, "%s", buffer);
			cake[ir] = buffer;
		}
		int crst = 0;
		int ccst = 0;
		int crfin = r;
		int ccfin = c;
		char ini;
		bool startblock = true;
		for (int i = 0; i < 256; ++i) ul[i] = false;
		for (int ir = 0; ir < r; ++ir)
		{
			for (int ic = 0; ic < c; ++ic)
			{
				if (cake[ir][ic] == '?')
				{
					if (startblock)
					{
						ccst = ic;
						crst = ir;
						startblock = false;
					}
				}
				else {
					if (!ul[cake[ir][ic]])
					{
						if (startblock)
						{
							ccst = ic;
							crst = ir;
						}
						int nc;
						for (nc = ic + 1; nc < c; ++nc)
						{
							if (cake[ir][nc] != '?')
							{
								break;
							}
						}
						int nr;
						int rf = false;
						for (nr = ir + 1; nr < r; ++nr)
						{
							for (int nnc = ccst; nnc < nc; ++nnc)
							{
								if (cake[nr][nnc] != '?')
								{
									rf = true;
									break;
								}
							}
							if (rf) break;
						}
						for (int tr = crst; tr < nr; ++tr)
						{
							for (int tc = ccst; tc < nc; ++tc)
							{
								cake[tr][tc] = cake[ir][ic];
							}
						}
						ic = ccst;
						ir = crst;
						startblock = true;
						ul[cake[ir][ic]] = true;
					}
					
				}
			}
		}

		fprintf(fout, "Case #%d:\n", ti + 1);
		for (int ir = 0; ir < r; ++ir) fprintf(fout, "%s\n", cake[ir].c_str());
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
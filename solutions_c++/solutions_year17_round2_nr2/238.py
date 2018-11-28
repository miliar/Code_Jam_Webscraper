#include "stdafx.h"
#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <string.h>
#include <algorithm>

typedef long long int LL;

using namespace std;

int main()
{
	FILE* in, *out;
	string filename = "B-large";
	string infilename = filename, outfilename = filename;
	infilename += ".in";
	outfilename += ".out";
	if ((in = fopen(infilename.c_str(), "rt")) == NULL)
	{
		cout << "Input file not found." << endl;
		getchar();
		return 1;
	}
	if ((out = fopen(outfilename.c_str(), "wt")) == NULL)
	{
		cout << "Cannot create output file." << endl;
		getchar();
		return 2;
	}

	int T;
	fscanf(in, "%d", &T);

	for (int t = 0; t != T; ++t)
	{
		int N, R, O, Y, G, B, V;
		fscanf(in, "%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);
		bool fail = false;
		if (R == G && R>0 && N > R + G || O == B && B>0 && N > O + B || Y == V && Y>0 && N > Y + V)
			fail = true;
		string OB, RG, YV;
		if (O > 0 && N > O + B)
		{
			OB += 'B';
			--B;
		}
		for (int i = 0; 0 < O; ++i)
		{		
			OB += 'O';
			OB += 'B';
			--B; --O;
		}
		if (G > 0 && N > R + G)
		{
			RG += 'R';
			--R;
		}
		for (int i = 0; 0 < G; ++i)
		{
			RG += 'G';
			RG += 'R';
			--G; --R;
		}
		if (V > 0 && N > Y + V)
		{
			YV += 'Y';
			--Y;
		}
		for (int i = 0; 0 < V; ++i)
		{
			YV += 'V';
			YV += 'Y';
			--Y; --V;
		}
		if (YV.length() > 0 && YV.front()=='Y')
			++Y;
		if (RG.length() > 0 && RG.front() == 'R')
			++R;
		if (OB.length() > 0 && OB.front() == 'B')
			++B;
		if (R < 0 || Y < 0 || B < 0)
			fail = true;

		int Mx = R;
		if (Y > Mx) Mx = Y;
		if (B > Mx) Mx = B;
		int Other2 = R + B + Y - Mx;
		if (Mx > Other2)
			fail = true;
		if(fail)
		{
			fprintf(out, "Case #%d: IMPOSSIBLE\n", t + 1);
			continue;
		}
		
		string preSol;
		while (R + B + Y > 0)
		{
			int Mx = -1;
			char chosen;
			if ((preSol.size() == 0 || preSol.back() != 'R') && (R > Mx || R == Mx && preSol.size() > 0 && preSol.front() == 'R'))
			{
				Mx = R;
				chosen = 'R';
			}
			if ((preSol.size() == 0 || preSol.back() != 'Y') && (Y > Mx || Y == Mx && preSol.size() > 0 && preSol.front() == 'Y'))
			{
				Mx = Y;
				chosen = 'Y';
			}
			if ((preSol.size() == 0 || preSol.back() != 'B') && (B > Mx || B == Mx && preSol.size() > 0 && preSol.front() == 'B'))
			{
				Mx = B;
				chosen = 'B';
			}
			preSol += chosen;
			if (chosen == 'R')
				--R;
			if (chosen == 'Y')
				--Y;
			if (chosen == 'B')
				--B;
		}
		if (YV.length() > 0)
		{
			int pos = preSol.find("Y");
			preSol = preSol.substr(0, pos) + YV + preSol.substr(pos+1);
		}
		if (RG.length() > 0)
		{
			int pos = preSol.find("R");
			preSol = preSol.substr(0, pos) + RG + preSol.substr(pos + 1);
		}
		if (OB.length() > 0)
		{
			int pos = preSol.find("B");
			preSol = preSol.substr(0, pos) + OB + preSol.substr(pos + 1);
		}

		const char* sol = preSol.c_str();
		fprintf(out, "Case #%d: %s\n", t+1, sol);
	}

	fclose(in);
	fclose(out);
	return 0;
}



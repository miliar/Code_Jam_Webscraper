#include "stdafx.h"
#include <fstream>
#include <string>
#include <cstdlib>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <stdio.h>
#include <unordered_set>
#include <unordered_map>

#include <math.h>

using namespace std;

ofstream fout("OUT111.txt");
ifstream fin("INP111.txt");


int main()
{
	int TT;
	fin >> TT;

	for (int tt = 0; tt < TT; tt++)
	{
		int ac, aj;
		fin >> ac >> aj;
		vector <vector <int> > ev;
		for (int i = 0; i < ac; i++)
		{
			int c, d;
			fin >> c >> d;
			vector <int> te1 = { c, 0, 0 };
			vector <int> te2 = { d, 1, 0 };
			ev.push_back(te1);
			ev.push_back(te2);
		}
		for (int i = 0; i < aj; i++)
		{
			int c, d;
			fin >> c >> d;
			vector <int> te1 = { c, 0, 1 };
			vector <int> te2 = { d, 1, 1 };
			ev.push_back(te1);
			ev.push_back(te2);
		}
		sort(ev.begin(), ev.end());

		if (ac + aj == 1)
		{
			fout << "Case #" << tt + 1 << ": " << 2 << "\n";
			continue;
		}

		int must[2] = { 0, 0 };
		int betw[2] = { 0, 0 };
		int bord = 0;
		int n = ev.size();
		int swit = 0;
		int betwlen[2][102];
		int numbetw[2] = { 0, 0 };
		vector <int> betw1;
		for (int i = 1; i < n; i++)
		{
			if (ev[i][1] == 0)
			{
				if (ev[i - 1][2] == ev[i][2])
				{
					betw[ev[i - 1][2]] += (ev[i][0] - ev[i - 1][0]);
					betwlen[ev[i - 1][2]][numbetw[ev[i - 1][2]]] = (ev[i][0] - ev[i - 1][0]);
					numbetw[ev[i - 1][2]]++;
				}
				else
				{
					bord += (ev[i][0] - ev[i - 1][0]);
					swit++;
				}
			}
			else
				must[ev[i][2]] += (ev[i][0] - ev[i - 1][0]);
		}

		if (ev[0][2] == ev[n - 1][2])
		{
			betw[ev[0][2]] += (24 * 60 + ev[0][0] - ev[n - 1][0]);
			betwlen[ev[0][2]][numbetw[ev[0][2]]] = (24*60+ev[0][0] - ev[n - 1][0]);
			numbetw[ev[0][2]]++;
		}
		else
		{
			bord += (24*60 + ev[0][0] - ev[n - 1][0]);
			swit++;
		}

		if (must[0] + betw[0] <= 720 && must[1] + betw[1] <= 720)
		{
			fout << "Case #" << tt + 1 << ": " << swit << "\n";
			continue;
		}
		else
		{
			int badind = 0;
			if (must[1] + betw[1] > 720)
				badind = 1;
			int defic = must[badind] + betw[badind] - 720;
			vector <int> dife;
			for (int i = 0; i < numbetw[badind]; i++)
				dife.push_back(betwlen[badind][i]);
			sort(dife.begin(), dife.end());
			reverse(dife.begin(), dife.end());
			for (int i = 0; i < dife.size() && defic > 0; i++)
			{
				swit += 2;
				if (defic > dife[i])
					defic = defic - dife[i];
				else
					defic = 0;
			}
			fout << "Case #" << tt + 1 << ": " << swit << "\n";
		}

		//fout << "Case #" << tt + 1 << ": " << 42 << "\n";
	}

	return 0;
}


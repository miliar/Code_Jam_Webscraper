// B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>
#include <iomanip>
#include <vector>
#include <algorithm>

using namespace std;

#define CAMERON 0
#define JAMIE 1

struct activity
{
	int begin;
	int end;
	int owner;
};

bool sort_func(activity i, activity j)
{
	return i.begin < j.begin;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("b.in");
	ofstream out("b.out");

	int t;
	in >> t;
	for (int i = 0; i < t; i++)
	{
		int ac,aj;
		in >> ac >> aj;

		//vector<activity> cameron;
		//vector<activity> jamie;
		vector<activity> act;
		int c_left = 720;
		int j_left = 720;
		int exchanges = 0;
		for (int j = 0; j < ac; j++)
		{
			activity a;
			in >> a.begin >> a.end;
			c_left -= (a.end - a.begin);
			a.owner = CAMERON;
			act.push_back(a);
			//cameron.push_back(a);
		}
		//sort(cameron.begin(), cameron.end(), sort_func);
		for (int j = 0; j < aj; j++)
		{
			activity a;
			in >> a.begin >> a.end;
			j_left -= (a.end - a.begin);
			a.owner = JAMIE;
			act.push_back(a);
			//jamie.push_back(a);
		}
		//sort(jamie.begin(), jamie.end(), sort_func);
		sort(act.begin(), act.end(), sort_func);

		activity a;
		a.begin = act[0].begin + 1440;
		a.end = act[0].end + 1440;
		a.owner = act[0].owner;
		act.push_back(a);

		bool cont = true;
		while(cont)
		{
			int min[2] = {1440, 1440};
			int j_c[2] = {-1,-1};
			for (int j = 0; j < act.size() - 1; j++)
			{
				if ((act[j].owner == act[j+1].owner) && (act[j+1].begin != act[j].end) && (min[act[j].owner] > act[j+1].begin - act[j].end))
				{
					min[act[j].owner] = act[j+1].begin - act[j].end;
					j_c[act[j].owner] = j;
				}
			}

			cont = false;
			if (j_c[CAMERON] > -1)
			{
				if (min[CAMERON] <= c_left)
				{
					cont = true;
					activity a;
					a.begin = act[j_c[CAMERON]].end;
					a.end = act[j_c[CAMERON]+1].begin;
					a.owner = CAMERON;
					act.push_back(a);
					c_left -= min[CAMERON];
				}
			}

			if (j_c[JAMIE] > -1)
			{
				if (min[JAMIE] <= j_left)
				{
					cont = true;
					activity a;
					a.begin = act[j_c[JAMIE]].end;
					a.end = act[j_c[JAMIE]+1].begin;
					a.owner = JAMIE;
					act.push_back(a);
					j_left -= min[JAMIE];
				}
			}

			if (cont)
				sort(act.begin(), act.end(), sort_func);
		}

		int result = 0;
		for (int j = 0; j < act.size() - 1; j++)
		{
			if (act[j].owner == act[j+1].owner)
			{
				if (act[j].end < act[j+1].begin)
					result += 2;
			}
			else
				result += 1;
		}

		out << "Case #" << i+1 << ": " << result << endl;
	}

	in.close();
	out.close();

	return 0;
}


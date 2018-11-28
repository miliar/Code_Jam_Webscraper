#include<iostream>
#include<algorithm>
#include<fstream>
using namespace std;
ifstream in("input.txt");
ofstream out("output.txt");
struct T
{
	int s, e;
	bool operator()(T a, T b)
	{
		if (a.s < b.s)return true;
		return false;
	}
}clist[210], jlist[210];
int main()
{
	int Test;
	in >> Test;
	for (int t = 1; t <= Test; t++)
	{
		int part[1450] = { 0, };
		int part2[1450] = { 0, };
		int C, J;
		in >> C >> J;
		int remain_c = 720;
		int remain_j = 720;
		for (int i = 0; i < C; i++)
		{
			in >> clist[i].s >> clist[i].e;
			for (int j = clist[i].s; j < clist[i].e; j++)
			{
				part[j] = 2;
				remain_j--;
			}
		}
		for (int i = 0; i < J; i++)
		{
			in >> jlist[i].s >> jlist[i].e;
			for (int j = jlist[i].s; j < jlist[i].e; j++)
			{
				part[j] = 1;
				remain_c--;
			}
		}
		int start = 0;
		for (int i = 0; i < 1440; i++)
		{
			if (part[i] != 0)
			{
				start = i;
				break;
			}
		}
		for (int i = 0; i < 1440; i++)
			part2[i] = part[i];
		int bak_c = remain_c;
		int bak_j = remain_j;
		int start_bak = start;
		while (1)
		{
			if (remain_c == 0 && remain_j == 0)break;
			if (part[start] != 0)
			{
				start++;
				start %= 1440;
				continue;
			}
			int before = start - 1;
			if (before < 0)before += 1440;

			if (part[before] == 1 && remain_c != 0)
			{
				part[start] = 1;
				remain_c--;
				continue;
			}
			else if (part[before] == 1 && remain_c == 0)
			{
				part[start] = 2;
				remain_j--;
				continue;
			}
			if (part[before] == 2 && remain_j != 0)
			{
				part[start] = 2;
				remain_j--;
				continue;
			}
			else if (part[before] == 2 && remain_j == 0)
			{
				part[start] = 1;
				remain_c--;
				continue;
			}
		}
		start = start_bak;
		remain_j = bak_j;
		remain_c = bak_c;
		while (1)
		{
			if (remain_c == 0 && remain_j == 0)break;
			if (part2[start] != 0)
			{
				start--;
				if (start < 0)start += 1440;
				continue;
			}
			int before = start + 1;
			before %= 1440;

			if (part2[before] == 1 && remain_c != 0)
			{
				part2[start] = 1;
				remain_c--;
				continue;
			}
			else if (part2[before] == 1 && remain_c == 0)
			{
				part2[start] = 2;
				remain_j--;
				continue;
			}
			if (part2[before] == 2 && remain_j != 0)
			{
				part2[start] = 2;
				remain_j--;
				continue;
			}
			else if (part2[before] == 2 && remain_j == 0)
			{
				part2[start] = 1;
				remain_c--;
				continue;
			}
		}
		int change = 0;
		if (part[0] != part[1439])change++;
		for (int i = 1; i < 1440; i++)
		{
			if (part[i] != part[i - 1])change++;
		}
		int change2 = 0;
		if (part2[0] != part2[1439])change2++;
		for (int i = 1; i < 1440; i++)
		{
			if (part2[i] != part2[i - 1])change2++;
		}
		if (change > change2)
			change = change2;
		out << "Case #" << t << ": " << change << endl;
	}
	return 0;
}

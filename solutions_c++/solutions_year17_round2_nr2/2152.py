#include <iostream>
#include <fstream>
#include<conio.h>
#include<stdio.h>
#include<iomanip>
#include<string>
#include<ctype.h>
#include<math.h>
#include<map>
#include<vector>
#include<assert.h>
#include<algorithm>

using namespace std;

#define FOR(k,a,b) for(int k=a; k <(b); ++k)
#define MIN(x,y) ((x)<(y)?(x):(y))
#define MAX(x,y) ((x)>(y)?(x):(y))

ifstream fin;
ofstream fout;
char convert(int i)
{
	if (i == 0)
		return 'R';
	if (i == 1)
		return 'O';
	if (i == 2)
		return 'Y';
	if (i == 3)
		return 'G';
	if (i == 4)
		return 'B';
	if (i == 5)
		return 'V';
}
bool sortdes(const pair<int, int> &a,
	const pair<int, int> &b)
{
	return (a.first > b.first);
}
void _main(int t)
{
	int n, r, o, y, g, b, v;
	vector<pair<int, int>> h,tem;
	fin >> n ;
	FOR(i, 0, 6)
	{
		int x;
		fin >> x;
		h.push_back(make_pair(x, i));
	}
	sort(h.begin(), h.end(),sortdes);
	if (h[0].first > n / 2)
		fout << "IMPOSSIBLE";
	else
	{
		char temp = ' ';
		int te = h[0].second;
		tem.push_back(make_pair(0, 0));
		FOR(i, 0, n)
		{
			bool bo =true;
			int ch = 1;
			while (bo&&ch<=5)
			{
				if (h[ch].second == te&&h[0].first == h[ch].first)
				{
					tem[0] = h[0];
					h[0] = h[ch];
					h[ch] = tem[0];
					bo = false;
				}
				else
					ch++;

			}
			
			if (convert(h[0].second) != temp)
			{
				fout << convert(h[0].second);
				h[0].first -= 1;
				temp= convert(h[0].second);
			}
			else
			{
				fout << convert(h[1].second);
				h[1].first -= 1;
				temp=convert(h[1].second);
			}
			sort(h.begin(), h.end(),sortdes);
		}
	}
}
int main()
{
	int t;
	fin.open("input.txt", ios::in);
	fout.open("output.txt", ios::out);
	fin >> t;
	for (int i = 1; i <= t; i++)
	{
		fout << "Case #" << i << ": ";
		_main(i);
		fout << "\n";
	}
	return 0;
}
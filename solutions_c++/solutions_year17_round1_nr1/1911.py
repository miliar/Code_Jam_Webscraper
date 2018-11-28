#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

FILE* in = fopen("input.in", "r");
FILE* out = fopen("output.out", "w");

int R, C;
void solve();

int main()
{
	int T;	fscanf(in,"%d", &T);
	for (int tc = 1; tc <= T; ++tc)
	{
		fprintf(out, "Case #%d:\n", tc);
		solve();
	}
}

void solve()
{
	fscanf(in,"%d %d", &R, &C);
	vector<char> alphabets;
	int numOfAlphabets = 0;
	vector<vector<int> > map(R,vector<int>(C,-1));
	for (int r = 0; r < R; ++r)
	{
		char inp[27];	fscanf(in,"%s", inp);
		for (int c = 0; c < C; ++c)
		{
			if (inp[c] != '?')
			{
				alphabets.push_back(inp[c]);
				map[r][c] = numOfAlphabets++;
			}
		}
	}

	for (int c = 0; c < C; ++c)
	{
		int bef = -1;
		for (int r = 0; r < R; ++r)
		{
			if (map[r][c] != -1)
				bef = map[r][c];
			else
				map[r][c] = bef;
		}
		bef = -1;
		for (int r = R-1; r >= 0; --r)
		{
			if (map[r][c] != -1)
				bef = map[r][c];
			else
				map[r][c] = bef;
		}
	}

	for (int r = 0; r < R; ++r)
	{
		int bef = -1;
		for (int c = 0; c < C; ++c)
		{
			if (map[r][c] != -1)
				bef = map[r][c];
			else
				map[r][c] = bef;
		}
		bef = -1;
		for (int c = C - 1; c >= 0; --c)
		{
			if (map[r][c] != -1)
				bef = map[r][c];
			else
				map[r][c] = bef;
		}
	}

	for (int r = 0; r < R; ++r)
	{
		for (int c = 0; c < C; ++c)
		{
			fprintf(out, "%c", alphabets[map[r][c]]);
		}
		fprintf(out, "\n");
	}
}
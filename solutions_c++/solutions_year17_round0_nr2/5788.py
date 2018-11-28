#pragma warning(disable:4996)
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <memory.h>
#include <algorithm>

using namespace std;

const char inFileName[] = "B-large.in";
const char outFileName[] = "B-large.out";

const int MAX_N = 30;

int T, n, m;
char s[MAX_N];

void solve(int n, char s[], int& m)
{
	m = n;
	int ind = 0;
	while (ind + 1 < n && s[ind] <= s[ind + 1]) 
		ind++;
	
	if (ind == n - 1)
	{
		return;
	}

	if (s[ind] == '1')
	{
		m = n - 1;
		for (int i = 0; i < m; i++)
			s[i] = '9';
		return;
	}

	for (int i = ind + 1; i < n; i++)
		s[i] = '9';
	int c = s[ind];
	while (ind > 0 && s[ind - 1] == c)
	{
		s[ind] = '9';
		ind--;
	}
	s[ind]--;
}

int main() {

	FILE* inFile = fopen(inFileName, "r");
	FILE* outFile = fopen(outFileName, "w");

	fscanf(inFile, "%d", &T);
	for (int t = 0; t < T; t++)
	{
		fscanf(inFile, "%s\n", s);
		n = strlen(s);
		solve(n, s, m);
		fprintf(outFile, "Case #%d: ", t + 1);
		for (int i = 0; i < m; i++)
		{
			fprintf(outFile, "%c", s[i]);
		}
		fprintf(outFile, "\n");
	}

	fclose(inFile);
	fclose(outFile);
	return 0;
}

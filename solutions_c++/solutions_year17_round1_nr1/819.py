#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int mark[30];
string S[30];

void solve()
{
	int r, c;
	scanf("%d%d", &r, &c);

	for(int i = 0;i < r;i++)
	{
		mark[i] = 0;
	}

	for(int i = 0;i < r;i++) cin >> S[i];

	for(int i = 0;i < r;i++)
	{
		int prev = -1;
		for(int j = 0;j < c;j++)
		{
			if(S[i][j] == '?')
			{
				if(prev != -1) S[i][j] = prev+'A';
			}
			else prev = int(S[i][j]-'A');
		}
		prev = -1;
		for(int j = c-1;j >= 0;j--)
		{
			if(S[i][j] == '?')
			{
				if(prev != -1) S[i][j] = prev+'A';
			}
			else prev = int(S[i][j]-'A');
		}
		prev = -1;
		for(int j = 0;j < c;j++)
		{
			if(S[i][j] == '?')
			{
				if(prev != -1) S[i][j] = prev+'A';
			}
			else prev = int(S[i][j]-'A');
		}
		prev = -1;
		for(int j = c-1;j >= 0;j--)
		{
			if(S[i][j] == '?')
			{
				if(prev != -1) S[i][j] = prev+'A';
			}
			else prev = int(S[i][j]-'A');
		}
		if(S[i][0] != '?') mark[i] = 1;
	}

	for(int i = 1;i < r;i++)
	{
		if(!mark[i] && mark[i-1])
		{
			for(int j = 0;j < c;j++) S[i][j] = S[i-1][j];
			mark[i] = 1;
		}
	}
	for(int i = r-2;i >= 0;i--)
	{
		if(!mark[i] && mark[i+1])
		{
			for(int j = 0;j < c;j++) S[i][j] = S[i+1][j];
			mark[i] = 1;
		}
	}
	for(int i = 1;i < r;i++)
	{
		if(!mark[i] && mark[i-1])
		{
			for(int j = 0;j < c;j++) S[i][j] = S[i-1][j];
			mark[i] = 1;
		}
	}
	for(int i = r-2;i >= 0;i--)
	{
		if(!mark[i] && mark[i+1])
		{
			for(int j = 0;j < c;j++) S[i][j] = S[i+1][j];
			mark[i] = 1;
		}
	}

	for(int i = 0;i < r;i++)
	{
		cout << S[i] << "\n";
	}
}

int main(void)
{
	int t;
	scanf("%d", &t);
	for(int i = 1;i <= t;i++)
	{
		printf("Case #%d:\n", i);
		solve();
	}
}
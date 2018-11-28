#include <bits/stdc++.h>
#define ll long long
#define M 1000000007
using namespace std;
struct node
{
	int row, col;
};
string s[30];
void expand_right(node &n, int c)
{
	char ch = s[n.row][n.col];
	int i = n.col;
	while(++i < c && s[n.row][i] == '?')
		n.col++, s[n.row][i] = ch;
}
void expand_left(node &n)
{
	char ch = s[n.row][n.col];
	int i = n.col;
	while(--i >= 0 && s[n.row][i] == '?')
		n.col--, s[n.row][i] = ch;
}
void expand_down(node &start, node &stop, int r)
{
	char ch = s[start.row][start.col];
	int col_start = start.col, col_end = stop.col, i = stop.row;
	while(++i < r)
	{
		bool flag = true;
		for(int j = col_start; j <= col_end && flag; j++)
		{
			if(s[i][j] != '?')
				flag = false;
		}
		if(!flag)
			break;
		stop.row = i;
		for(int j = col_start; j <= col_end; j++)
			s[i][j] = ch;
	}
}
void expand_up(node &start, node &stop)
{
	char ch = s[start.row][start.col];
	int col_start = start.col, col_end = stop.col, i = start.row;
	while(--i >= 0)
	{
		bool flag = true;
		for(int j = col_start; j <= col_end && flag; j++)
		{
			if(s[i][j] != '?')
				flag = false;
		}
		if(!flag)
			break;
		start.row = i;
		for(int j = col_start; j <= col_end; j++)
			s[i][j] = ch;
	}
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t;
	cin >> t;
	for(int ii = 1; ii <= t; ii++)
	{
		set<char> s1;
		int r, c;
		cin >> r >> c;
		for(int j = 0; j < r; j++)
			cin >> s[j];
		for(int i = 0; i < r; i++)
		{
			for(int j = 0; j < c; j++)
			{
				if(s[i][j] == '?' || s1.find(s[i][j]) != s1.end())
					continue;
				s1.insert(s[i][j]);
				node start, stop;
				start.row = stop.row = i;
				start.col = stop.col = j;
				expand_right(stop, c);
				expand_left(start);
				expand_down(start, stop, r);
				expand_up(start, stop);
			}
		}
		cout << "Case #" << ii << ":\n";
		for(int i = 0; i < r; i++)
			cout << s[i] << "\n";
	}
	return 0;
}

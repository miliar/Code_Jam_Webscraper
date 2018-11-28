#include<bits/stdc++.h>
using namespace std;
# define ll long long
# define mod 1000000007
# define MAX 300011
string str[30];
void fillHorizontal(int r, int c, int i, int j)
{
	char ch = str[i][j];
	for (int ii = j - 1; ii >= 0; ii--) {
		if (str[i][ii] != '?')
			break;
		str[i][ii] = ch;
	}
	for (int ii = j + 1; ii < c; ii++) {
		if (str[i][ii] != '?')
			break;
		str[i][ii] = ch;
	}
}
void fillVertical(int r, int c, int row, int st, int en, char ch) {
	int i, j, cnt;
	for (i = row-1; i >=0; i--) {
		cnt = 0;
		for (j = st; j <= en && !cnt; j++) {
			if (str[i][j] != '?')
				cnt++;
		}
		if (!cnt)
			for (j = st; j <= en; j++)
				str[i][j] = ch;
		else
			break;
	}
	for (i = row + 1; i < r; i++) {
		cnt = 0;
		for (j = st; j <= en && !cnt; j++) {
			if (str[i][j] != '?')
				cnt++;
		}
		if (!cnt)
			for (j = st; j <= en; j++)
				str[i][j] = ch;
		else
			break;
	}
}
int main()
{
	ifstream in("file/a.txt");
	ofstream out("file/b.txt");
	cin.sync_with_stdio(false);
	int t, r, c, i, j, var = 0;
	in >> t;
	while (t--)
	{
		var++;
		out << "Case #" << var << ":\n";
		in >> r >> c;
		for (i = 0; i < r; i++)
			in >> str[i];
		for (i = 0; i < r; i++)
		{
			for (j = 0; j < c; j++)
			{
				if (str[i][j] != '?')
				{
					fillHorizontal(r, c, i, j);
				}
			}
		}
		for (i = 0; i < r; i++) {
			int st, en;
			st = en = -1;
			for (j = 0; j < c; j++) {
				if (str[i][j] != '?' && st == -1 && en == -1) {
					st = en = j;
				}
				else if (str[i][j] != '?' && st >= 0 && en >= 0) {
					if (str[i][j] == str[i][j - 1]) {
						en = j;
					}
					else {
						fillVertical(r, c, i, st, en, str[i][en]);
						st = en = j;
					}
				}
				else {
					if (st >= 0 && en >= 0)
						fillVertical(r, c, i, st, en, str[i][en]);
					st = en = -1;
				}
			}
			if (st >= 0 && en >= 0) {
				fillVertical(r, c, i, st, en, str[i][c - 1]);
			}
		}
		for (i = 0; i < r; i++)
			out << str[i] << '\n';
	}
	return 0;
}

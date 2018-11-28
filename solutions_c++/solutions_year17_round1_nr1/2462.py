#include<iostream>
#include<string>
#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
#include<queue>
using namespace std;



int R; int C;
char board[26][26];


struct Rect
{
	char ch;
	int r;
	int h;
	int c;
	int w;
	Rect() {};
	Rect(int ch_, int a, int b, int c_, int d) { ch = ch_; r = a; c = b; h = c_; w = d; };
};


bool possibleH(char ch, int r, int c, int h)
{
	if (c < 0 || c >= C)return false;
	for (int i = 0; i < h; i++)
	{
		if(board[r + i][c]==0 || board[r + i][c] == ch)continue;
		return false;
	}
	return true;
}
bool possibleR(char ch, int r, int c, int w)
{
	if (r < 0 || r >= R)return false;
	for (int j = 0; j < w; j++)
	{
		if (board[r][c + j] == 0 || board[r][c + j] == ch)continue;
		return false;
	}
	return true;
}
void solve()
{
	queue<Rect> q;
	cin >> R >> C;
	for (int i = 0; i < R; i++)
	{
		for (int j = 0; j < C; j++)
		{
			cin >> board[i][j];
			if (board[i][j] == '?' )board[i][j] = 0;
			else q.push(Rect(board[i][j],i, j, 1, 1));
		}

	}
	while (!q.empty())
	{
		Rect R = q.front(); q.pop();
		for (int i = 1; possibleH(R.ch, R.r, R.c - 1, R.h); i++)
		{
			R.w++;
			R.c--;
		}
		for (int i = 1; possibleR(R.ch, R.r - 1, R.c, R.w); i++)
		{
			R.h++;
			R.r--;
		}
		for (int i = 0; possibleH(R.ch, R.r, R.c + R.w, R.h); i++)
		{
			R.w++;
		}
		for (int i = 0; possibleR(R.ch, R.r + R.h, R.c, R.w); i++)
		{
			R.h++;
		}
		for (int i = R.r; i < R.r + R.h; i++)
			for (int j = R.c; j < R.c + R.w; j++)
				board[i][j] = R.ch;
	}
};



int main()
{
	int T;
	//freopen("Text.txt", "r", stdin);
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	ios::sync_with_stdio(false);
	cin >> T;
	for (int tc = 1; tc <= T; tc++)
	{
		solve();
		cout << "Case #" << tc << ": " << endl;
		for (int i = 0; i < R; i++)
		{
			for (int j = 0; j < C; j++)
			{
				cout<<board[i][j];
			}
			cout << endl;
		}
	}
	fclose(stdin);
	fclose(stdout);

	return 0;
}
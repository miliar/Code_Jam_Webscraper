#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>

using namespace std;

struct magic
{
	int number, id;
	char Letter;
	int c1, c2, c3;
};

bool cmp(magic m1, magic m2)
{
	if (m1.number != m2.number)
		return m1.number > m2.number;
	return m1.id < m2.id;
}

int n;
magic m[9];

void solve(int num)
{
	cin >> n;
	for (int i = 1; i <= 6; i++)
	{
		cin >> m[i].number;
		m[i].id = i;
	}
	m[1].Letter = 'R';
	m[1].c1 = 1;
	m[1].c2 = 1;
	m[1].c3 = 1;
	m[2].Letter = 'O';
	m[2].c1 = 1;
	m[2].c2 = 2;
	m[2].c3 = 2;
	m[3].Letter = 'Y';
	m[3].c1 = 2;
	m[3].c2 = 2;
	m[3].c3 = 2;
	m[4].Letter = 'G';
	m[4].c1 = 2;
	m[4].c2 = 3;
	m[4].c3 = 2;
	m[5].Letter = 'B';
	m[5].c1 = 3;
	m[5].c2 = 3;
	m[5].c3 = 3;
	m[6].Letter = 'V';
	m[6].c1 = 1;
	m[6].c2 = 3;
	m[6].c3 = 3;
	sort(m + 1, m + 7, cmp);
	for (int i = 1; i <= 6; i++)
	{
		m[i].id = i;
	}
	magic Last;
	Last.Letter = 'K';
	Last.id = 0;
	Last.number = 0;
	Last.c1 = 0;
	Last.c2 = 0;
	Last.c3 = 0;
	string answer = "";
	cout << "Case #" << num << ": ";
	for (int i = 1; i <= n; i++)
	{
		bool err = true;
		sort(m + 1, m + 7, cmp);
		for (int j = 1; j <= 6; j++)
		{
			if (m[j].number > 0)
			{
				if (Last.c1 != m[j].c1 && Last.c2 != m[j].c2 && Last.c3 != m[j].c3)
				{
					answer += m[j].Letter;
					m[j].number--;
					err = false;
					Last = m[j];
					break;
				}
			}
		}
		if (err)
		{
			cout << "IMPOSSIBLE" << endl;
			return;
		}
	}
	if (answer[0] == answer[n - 1])
	{
		cout << "IMPOSSIBLE" << endl;	
	}
	else
	{
		cout << answer << endl;
	}
	return;
}

int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B_small.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		solve(i);
	}
	return 0;
}
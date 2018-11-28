#include<iostream>
#include<vector>

#pragma warning(disable:4996)
using namespace std;
struct resault {
	char _e;
	int _r, _c;
	resault(char e, int r, int c) {
		_e = e;
		_r = r;
		_c = c;
	}
};
void f(int t)
{
	int hang[101] = {};
	int lie[101] = {};
	int zdj[201] = {};
	int ydj[201] = {};
	int N, M;
	cin >> N >> M;
	int grade = 0;
	char e;
	int r, c;
	int all[101][101] = {};
	vector<resault> re;
	while (M--)
	{
		getchar();
		scanf("%c %d %d", &e, &r, &c);
		all[c][r] = e;
		switch (e)
		{
		case '+':
			zdj[c - r + N - 1] = 1;
			ydj[c + r - 1] = 1;
			break;
		case 'x':
			hang[r] = 1;
			lie[c] = 1;
			break;
		case 'o':
			zdj[c - r + N - 1] = 1;
			ydj[c + r - 1] = 1;
			hang[r] = 1;
			lie[c] = 1;
			break;
		}
	}
	int visited[101][101] = {};
	int i = 1, j = 1;
	int sum = N*N;
	int flag = 0;
	visited[i][j] = 1;
	switch (all[j][i])
	{
	case 'o':grade += 2;
		break;
	case '+':
		if (!hang[i] && !lie[j])
		{
			grade += 2;
			hang[i] = 1;
			lie[j] = 1;
			re.push_back(resault('o', i, j));
		}
		else
			grade += 1;
		break;
	case 'x':
		if (!zdj[j - i + N - 1] && !ydj[j + i - 1])
		{
			grade += 2;
			zdj[j - i + N - 1] = 1;
			ydj[j + i - 1] = 1;
			re.push_back(resault('o', i, j));
		}
		else
			grade += 1;
	default:

		if (!zdj[j - i + N - 1] && !ydj[j + i - 1] && !hang[i] && !lie[j])
		{
			grade += 2;
			zdj[j - i + N - 1] = 1;
			ydj[j + i - 1] = 1;
			hang[i] = 1;
			lie[j] = 1;
			re.push_back(resault('o', i, j));
		}
		else if (!zdj[j - i + N - 1] && !ydj[j + i - 1])
		{
			grade += 1;
			zdj[j - i + N - 1] = 1;
			ydj[j + i - 1] = 1;
			re.push_back(resault('+', i, j));
		}
		else if (!hang[i] && !lie[j])
		{
			grade += 1;
			hang[i] = 1;
			lie[j] = 1;
			re.push_back(resault('x', i, j));
		}
		break;
	}
	--sum;
	while (sum)
	{
		if (flag == 0 && (i + 1 > N || visited[i + 1][j] == 1 )) {
			flag = 1; continue;
		}
		if (flag == 1 && (j + 1 > N||visited[i][j + 1] == 1 )) {
			flag = 2; continue;
		}
		if (flag == 2 && (i - 1 < 1 || visited[i - 1][j] == 1)) {
			flag = 3; continue;
		}
		if (flag == 3 && (j - 1 < 1||visited[i][j - 1] == 1  )) {
			flag = 0; continue;
		}
		switch (flag)
		{
		case 0:	++i;
			break;
		case 1:++j;
			break;
		case 2:--i;
			break;
		case 3:--j;
			break;
		}
		visited[i][j] = 1;
		switch (all[j][i])
		{
		case 'o':grade += 2;
			break;
		case '+':
			if (!hang[i] && !lie[j])
			{
				grade += 2;
				hang[i] = 1;
				lie[j] = 1;
				re.push_back(resault('o', i, j));
			}
			else
				grade += 1;
			break;
		case 'x':
			if (!zdj[j - i + N - 1] && !ydj[j + i - 1])
			{
				grade += 2;
				zdj[j - i + N - 1] = 1;
				ydj[j + i - 1] = 1;
				re.push_back(resault('o', i, j));
			}
			else
				grade += 1;
		default:

			if (!zdj[j - i + N - 1] && !ydj[j + i - 1] && !hang[i] && !lie[j])
			{
				grade += 2;
				zdj[j - i + N - 1] = 1;
				ydj[j + i - 1] = 1;
				hang[i] = 1;
				lie[j] = 1;
				re.push_back(resault('o', i, j));
			}
			else if (!zdj[j - i + N - 1] && !ydj[j + i - 1])
			{
				grade += 1;
				zdj[j - i + N - 1] = 1;
				ydj[j + i - 1] = 1;
				re.push_back(resault('+', i, j));
			}
			else if (!hang[i] && !lie[j])
			{
				grade += 1;
				hang[i] = 1;
				lie[j] = 1;
				re.push_back(resault('x', i, j));
			}
			break;
		}
		--sum;
	}
	printf("Case #%d: %d %d\n", t,grade,re.size());
	for (auto x : re)
		printf("%c %d %d\n", x._e, x._r, x._c);

}
int main()
{

	freopen("file.txt", "w", stdout);
	int T;

	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		f(t);
	}

}
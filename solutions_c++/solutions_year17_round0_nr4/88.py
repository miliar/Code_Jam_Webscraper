#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

int T;

int input_data[20000][3];

bool w[210][210], visit[210];
int match[210];
bool choose1[210], choose2[210];
int change[110][110], orig[110][110];
int n, m, tot;

int find(int x)
{
	
	for (int i = 0; i < tot; i++)
	{
		if (w[x][i] && !visit[i])
		{
			visit[i] = 1;
			if (match[i] == -1 || find(match[i]))
			{
				match[i] = x;
				return 1;
			}
		}
	}
	return 0;
}
void Solve()
{
	scanf("%d %d\n", &n, &m);
	memset(change, 0, sizeof(change));
	memset(orig, 0, sizeof(orig));
	for (int i = 0; i < m; i++)
	{
		char c;
		scanf("%c %d %d\n", &c, &input_data[i][1], &input_data[i][2]);
		input_data[i][0] = c;
		input_data[i][1]--;
		input_data[i][2]--;
		if (c == '+' || c == 'o')
			orig[input_data[i][1]][input_data[i][2]] += 1;
		if (c == 'x' || c == 'o')
			orig[input_data[i][1]][input_data[i][2]] += 2;
	}
	//select not '+'
	memset(w, 1, sizeof(w));
	memset(choose1, 0, sizeof(choose1));
	memset(choose2, 0, sizeof(choose2));
	for (int i = 0; i < m; i++)
		if (input_data[i][0] == 'o' || input_data[i][0] == 'x')
		{
			choose1[input_data[i][1]] = true;
			choose2[input_data[i][2]] = true;
		}

	for (int i = 0; i < n; i++)
	{
		if (choose1[i])
			for (int j = 0; j < n; j++)
				w[i][j] = false;

		if (choose2[i])
			for (int j = 0; j < n; j++)
				w[j][i] = false;
	}
	memset(match, 255, sizeof(match));
	tot = n;
	for (int i = 0; i < n; i++)
	{
		memset(visit, 0, sizeof(visit));
		find(i);
	}

	for (int i = 0; i < n; i++)
		if (match[i] != -1)
			change[match[i]][i] = (change[match[i]][i] | 2);

	//select not 'x'
	memset(w, 0, sizeof(w));
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			w[i + j][i - j + (n - 1)] = true;
	memset(choose1, 0, sizeof(choose1));
	memset(choose2, 0, sizeof(choose2));
	for (int i = 0; i < m; i++)
		if (input_data[i][0] == 'o' || input_data[i][0] == '+')
		{
			choose1[input_data[i][1] + input_data[i][2]] = true;
			choose2[input_data[i][1] - input_data[i][2] + (n-1)] = true;
		}

	for (int i = 0; i < 2 * n - 1; i++)
	{
		if (choose1[i])
			for (int j = 0; j < 2 * n - 1; j++)
				w[i][j] = false;

		if (choose2[i])
			for (int j = 0; j < 2 * n - 1; j++)
				w[j][i] = false;
	}
	memset(match, 255, sizeof(match));
	tot = 2 * n - 1;
	for (int i = 0; i < 2 * n - 1; i++)
	{
		memset(visit, 0, sizeof(visit));
		find(i);
	}

	for (int i = 0; i < 2 * n - 1; i++)
		if (match[i] != -1)
			change[(match[i] + i - (n - 1)) / 2][(match[i] - i + (n - 1)) / 2] = (change[(match[i] + i - (n - 1)) / 2][(match[i] - i + (n - 1)) / 2] | 1);

	//final
	int ans1 = 0, ans2 = 0;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
		{
			if ((change[i][j] | orig[i][j]) != orig[i][j])
			{
				ans2++;
			}
			int temp = (change[i][j] | orig[i][j]);
			if (temp == 1 || temp == 2)
				ans1 += 1;
			else if (temp == 3)
				ans1 += 2;
		}
	printf("%d %d\n", ans1, ans2);
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			if ((change[i][j] | orig[i][j]) != orig[i][j])
			{
				int temp = (change[i][j] | orig[i][j]);
				if (temp == 1)
					printf("+ ");
				else if (temp == 2)
					printf("x ");
				else if (temp == 3)
					printf("o ");
				printf("%d %d\n", i+1, j+1);
			}
}

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	scanf("%d\n", &T);
	for (int i = 0; i < T; i++)
	{
		printf("Case #%d: ", i + 1);
		Solve();
	}
}
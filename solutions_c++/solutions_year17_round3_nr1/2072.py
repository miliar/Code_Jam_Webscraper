#include <iostream>
#include <cstdio>

using namespace std;

#define MAX(a, b) (a > b ? a : b)
#define PI 3.14159265359

int N, K;
double R[1001], H[1001], t[1001][1001], resp;
bool was[1001];

double calc_top(double R)
{
	return PI * R * R;
}

double calc_side(double R, double H)
{
	return 2.0 * PI * R * H;
}

void dfs(int pos, int count)
{
	int i;
	double area;

	if (count == K)
	{
		resp = MAX(resp, t[count][pos]);
		return;
	}

	was[pos] = true;

	for (i = 0; i < N; i++)
	{
		if (!was[i] && R[pos] <= R[i])
		{
			area = (calc_top(R[i]) - calc_top(R[pos])) + calc_side(R[i], H[i]);
			//cout<<"area "<<i<<" "<<area<<endl;

			if (t[count+1][i] < area + t[count][pos])
			{
				t[count+1][i] = area + t[count][pos];

				dfs(i, count + 1);
			}
		}
	}

	was[pos] = false;
}

int main()
{
	int test, T, i, j;

	cin>>T;

	for (test = 1; test <= T; test++)
	{
		cin>>N>>K;

		for (i = 0; i < N; i++)
		{
			cin>>R[i]>>H[i];
			was[i] = false;

			for (j = 0; j < N+1; j++)
			{
				t[i][j] = 0.0;
			}
		}
		R[i] = 0.0;
		H[i] = 0.0;
		for (j = 0; j < N+1; j++)
		{
			t[i][j] = 0.0;
		}
		was[i] = false;

		resp  = 0.0;
		dfs(i, 0);

		printf("Case #%d: %.6lf\n", test, resp);

	}

	return 0;
}

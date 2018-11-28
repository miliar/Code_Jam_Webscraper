#include<iostream>
#include<algorithm>
#include<fstream>
#include<math.h>
#define PI 3.14159265358979323
using namespace std;
ifstream in("input.txt");
ofstream out("output.txt");
struct T
{
	long long int r, h;
	bool operator()(T a, T b)
	{
		if (a.r > b.r)return true;
		if (a.r == b.r && a.h > b.h)return true;
		return false;
	}
}list[1010];
double Dy[1010][1010];

int main()
{
	long long int Test;
	in >> Test;
	for (long long int t = 0; t < Test; t++)
	{
		memset(list, 0, sizeof(list));
		memset(Dy, 0, sizeof(Dy));
		long long int n, m;
		in >> n >> m;
		for (long long int i = 0; i < n; i++)
			in >> list[i].r >> list[i].h;

		sort(list, list + n, T());
		double MAX = 0;
		for (long long int i = 0; i < n; i++)
		{
			Dy[1][i] = 2 * list[i].r*list[i].h*PI;
			Dy[1][i] += list[i].r*list[i].r*PI;
		}

		for (long long int i = 2; i <= m; i++)
		{
			for (long long int j = i-1; j < n; j++)
			{
				for (long long int k = 0; k < j; k++)
				{
					if (Dy[i][j] < Dy[i - 1][k] + 2 * list[j].r*list[j].h*PI)
					{
						Dy[i][j] = Dy[i - 1][k] + 2 * list[j].r*list[j].h*PI;
					}
				}
			}
		}
		for (long long int i = 0; i < n; i++)
		{
			if (MAX < Dy[m][i])
				MAX = Dy[m][i];
		}
		out.precision(9);
		out << "Case #" << t + 1 << ": ";
		out << fixed << MAX << endl;
	}

	return 0;
}
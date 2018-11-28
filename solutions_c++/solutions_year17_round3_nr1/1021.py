#include <iostream>
#include <fstream>
#include <algorithm>

#define PI 3.1415926535897932384626433832795028841971

using namespace std;

struct data
{
	double R;
	double H;
	double O;
};

bool cmp(struct data x, struct data y)
{
	if (x.O == y.O)return x.R > y.R;
	return x.O > y.O;
}

int main()
{
	ifstream in("A-large.in");
	ofstream out("output.txt");
	out << fixed;
	out.precision(10);

	int T;
	in >> T;
	for (int Case = 1; Case <= T; Case++)
	{
		int N, K;
		in >> N >> K;

		struct data *Pancake = new struct data[N];
		
		for (int i = 0; i < N; i++)
		{
			in >> Pancake[i].R >> Pancake[i].H;
			Pancake[i].O = 2 *PI*Pancake[i].R*Pancake[i].H;
		}

		sort(&Pancake[0], &Pancake[N], cmp);

		double sum_max = 0;
		for (int i = 0; i < N; i++)
		{
			double sum = PI*Pancake[i].R*Pancake[i].R + Pancake[i].O;
			int j = 0;
			for (int cnt = 0; cnt < K - 1; cnt++)
			{
				if (i == j)j++;
				sum += Pancake[j++].O;
			}
			if (sum_max < sum)sum_max = sum;
		}

		out << "Case #" << Case << ": " << sum_max << endl;
	}

	return 0;
}
#include <iostream>
#include <fstream>
#include <bits/stdc++.h>

using namespace std;


struct el
{
	double R;
	double H;
};

int K;

double max_S;

vector<el> pancakes;

void f(size_t i, vector<size_t> t, vector<char> taken, size_t k)
{
	taken[i] = 1;
	t.push_back(i);

	if (k == K)
	{
		double S = .0;

		for (int j = 0; j < t.size() - 1; ++j)
		{
			auto const& p1 = pancakes[t[j]];
			auto const& p2 = pancakes[t[j + 1]];

			S += 2.0*M_PI*p1.R*p1.H + M_PI*(p1.R*p1.R - p2.R*p2.R);
		}

		S += 2.0*M_PI*pancakes[t.back()].R*pancakes[t.back()].H + M_PI*pancakes[t.back()].R*pancakes[t.back()].R;

		max_S = max(S, max_S);

		return;
	}

	for (int j = 0; j < taken.size(); ++j)
		if (!taken[j] && pancakes[j].R <= pancakes[i].R)
			f(j, t, taken, k + 1);
}

int main()
{
	ifstream in("input.txt");

	size_t T;

	in >> T;

	ofstream out("output.txt");

	for (int z = 1; z <= T; ++z)
	{
		int N;
		in >> N >> K;

		pancakes.resize(N);

		for (auto& p : pancakes)
			in >> p.R >> p.H;

		max_S = .0;
		vector<size_t> t;
		vector<char> taken(N);
		for (int i = 0; i < N; ++i)
			f(i, t, taken, 1);

		out << "Case #" << z << ": " << fixed << setprecision(9) << max_S << "\n";
	}
}
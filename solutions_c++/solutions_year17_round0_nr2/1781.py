#include <iostream>

using namespace std;

struct Problem
{
	string N;

	void solve()
	{
		while (!isTidy())
		{
			cerr << "Solving for N = " << N << endl;

			for (int i = 0; (i < N.size()) && (!isTidy()); ++i)
			{
				int j = N.size() - i - 1;

				if (N[j] == '9')
					continue;

				N[j] = '9';
				dec(j - 1);
			}
		}

		while (N.size() > 1 && N[0] == '0')
			N.erase(N.begin());
	}

private:
	void dec(int i)
	{
		for (; i >= 0; --i)
		{
			if (N[i] == '0')
				N[i] = '9';
			else
			{
				--N[i];
				break;
			}
		}
	}

	bool isTidy() const
	{
		return isTidy(0, N.size());
	}

	bool isTidy(int from, int to) const
	{
		bool is = true;

		for (int i = from + 1; i < to; ++i)
			is = is && (N[i - 1] <= N[i]);

		return is;
	}
};

istream &operator >>(istream &in, Problem &p)
{
	in >> p.N;
	return in;
}

ostream &operator <<(ostream &out, Problem &p)
{
	out << p.N;
	return out;
}

void test()
{
	int T = 0;
	cin >> T;

	for (int i = 0; i < T; ++i)
	{
		Problem p;
		cin >> p;
		p.solve();
		cout << "Case #" << i + 1 << ": " << p << endl;
	}
}

int main()
{
	test();
	return 0;
}

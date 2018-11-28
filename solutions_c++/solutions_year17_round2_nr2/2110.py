#include <iostream>
#include <string>

using namespace std;

struct Problem
{
	int N, R, O, Y, G, B, V;
	string result;

	char choose(int &a, int &b, int &c, char ac, char bc, char cc)
	{
		if (c >= a && c >= b)
		{
			--c;
			return cc;
		}

		if (a > b)
		{
			--a;
			return ac;
		}
		else
		{
			--b;
			return bc;
		}
	}

	void solve()
	{
		if (
			R <= Y + B + G &&
			Y <= R + B + V &&
			B <= Y + R + O &&
			O <= B &&
			G <= R &&
			V <= Y)
		{
			if (R > 0)
				--R, result += 'R';
			else if (Y > 0)
				--Y, result += 'Y';
			else if (B > 0)
				--B, result += 'B';
			else if (O > 0)
				--O, result += 'O';
			else if (G > 0)
				--G, result += 'G';
			else if (V > 0)
				--V, result += 'V';

			for (;
				R > 0 ||
				Y > 0 ||
				B > 0 ||
				O > 0 ||
				G > 0 ||
				V > 0
				 ;)
			{
				char choice = ' ';

				switch (result[result.size() - 1])
				{
					case 'R':
						choice = choose(Y, B, G, 'Y', 'B', 'G');
						break;

					case 'Y':
						choice = choose(R, B, V, 'R', 'B', 'V');
						break;

					case 'B':
						choice = choose(Y, R, O, 'Y', 'R', 'O');
						break;

					case 'O':
						choice = 'B';
						--B;
						break;

					case 'G':
						choice = 'R';
						--R;
						break;

					case 'V':
						choice = 'Y';
						--Y;
						break;
				}

				result += choice;
			}
		}
		else
			result = "IMPOSSIBLE";
	}
};

istream &operator >>(istream &in, Problem &p)
{
	in >> p.N >> p.R >> p.O >> p.Y >> p.G >> p.B >> p.V;
	return in;
}

ostream &operator <<(ostream &out, Problem &p)
{
	out << p.result;
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
//	freopen("in", "rt", stdin);

	test();
	return 0;
}

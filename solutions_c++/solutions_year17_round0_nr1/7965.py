#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int solveIt(string ps, int K);

string showResult(int result)
{
	string txt;
	ostringstream out;

	if (result < 0)
		out << "IMPOSSIBLE";
	else
		out << result;

	return out.str();
}

int main()
{
	int T;

	cin >> T;

	for (int ti = 1; ti <= T; ++ti)
	{
		string ps;
		int K;

		cin >> ps >> K;

		cout << "Case #" << ti << ": " << showResult(solveIt(ps, K)) << endl;
	}

	return 0;
}

int solveIt(string ps, int K)
{
	int flips = 0;
	const int N = ps.size();

	for(int i = 0; i < N; ++i)
	{
		if (ps[i] == '+') continue;
		if (i + K > N) return -1;

		++flips;

		for(int r = i; r < i + K; ++r)
		{
			ps[r] = (ps[r] == '+' ? '-' : '+');
		}
	}

	return flips;
}


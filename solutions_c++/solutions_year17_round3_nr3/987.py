#include<iostream>
#include<algorithm>
#include<fstream>
#include<string>
#include<vector>
#include<queue>
using namespace std;

int test;
int n, k;
double u, pp;
vector<double> p;

int main()
{
	ifstream in("C-small-1-attempt2.in");
	//ifstream in("input.txt");
	ofstream out("output.txt");
	in >> test;
	for (int t = 1; t <= test; ++t)
	{
		in >> n >> k;
		in >> u;
		p.clear();
		for (int i = 0; i < n; ++i) {
			in >> pp;
			p.push_back(pp);
		}

		sort(p.begin(), p.end());

		int c = 1;
		for (int i = 0; i < n-1; ++i) {
			if (u <= 0.0f)
				break;
			if (u >= (double)c * (p[i + 1] - p[i])) {
				u -= ((double)c * (p[i + 1] - p[i]));
				for (int j = 0; j <= i; ++j)
					p[j] = p[i + 1];
			}
			else {
				double each = u / (double)c;
				for (int j = 0; j <= i; ++j)
					p[j] += each;
				u = 0.0f;
				break;
			}
			
			++c;
		}

		if (u >= 0.0f) {
			double each = u / (double)n;
			for (int j = 0; j < n; ++j)
				p[j] += each;
		}

		double res = 1.0f;
		for (int i = 0; i < n; ++i)
			res *= p[i];

		out << fixed;
		out.precision(10);
		out << "Case #" << t << ": " << res << endl;
	}

	in.close();
	out.close();
	return 0;
}
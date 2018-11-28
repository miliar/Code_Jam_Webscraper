#include<iostream>
#include<algorithm>
#include<fstream>
#include<string>
#include<vector>
#include<queue>
using namespace std;

int test;
vector<pair<int, int> > a;
int d, n;
int t1, t2;

bool cmp(pair<int, int> aa, pair<int, int> bb)
{
	return aa.first < bb.first;
}

int main()
{
	ifstream in("A-small-attempt1.in");
	//ifstream in("input.txt");
	ofstream out("output.txt");
	in >> test;
	for (int t = 1; t <= test; ++t)
	{
		a.clear();
		in >> d >> n;
		for (int i = 0; i < n; ++i) {
			in >> t1 >> t2;
			a.push_back(pair<int, int>(t1, t2));
		}
		sort(a.begin(), a.end(), cmp);

		int pos = n - 1;
		for (int i = 0; i < n - 1; ++i)
		{
			bool ok = false;
			for (int j = i + 1; j < n; ++j)
			{
				if (a[i].second == a[j].second)
					continue;

				double x = (double)(a[i].second - a[j].second) / (double)(a[j].first - a[i].first);
				if (x < 0.0f)
					continue;

				if ((double)a[i].first + (double)a[i].second * x >= (double)d)
					continue;

				ok = true;
				break;
			}
			
			if (!ok)
			{
				pos = i;
				break;
			}
		}

		double x = ((double)d - (double)a[pos].first) / (double)a[pos].second;

		double res = (double)d / x;
		out.setf(ios::showpoint);
		out << fixed;
		out.precision(7);
		out << "Case #" << t << ": " << res << endl;
	}

	in.close();
	out.close();
	return 0;
}
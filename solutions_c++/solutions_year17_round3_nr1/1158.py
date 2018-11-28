#define M_PI 3.14159265358979323846
#include<iostream>
#include<algorithm>
#include<fstream>
#include<string>
#include<vector>
#include<queue>
using namespace std;

int test;
vector<pair<long long int, long long int> > a;
int n, k;
long long int t1, t2;

bool b[1005];
//long long int d[1005][1005];


bool cmp(pair<long long int, long long int> aa, pair<long long int, long long int> bb)
{
	if (aa.first == bb.first)
		return aa.second > bb.second;
	return aa.first > bb.first;
}

int main()
{
	ifstream in("A-large.in");
	//ifstream in("input.txt");
	ofstream out("output.txt");
	in >> test;
	for (int t = 1; t <= test; ++t)
	{
		a.clear();
		in >> n >> k;
		for (int i = 0; i < n; ++i)
		{
			in >> t1 >> t2;
			a.push_back(pair<long long int, long long int>(t1, t2));
			b[i] = false;
		}
		sort(a.begin(), a.end(), cmp);

		for (int j = 0; j < k; ++j)
		{
			long long int mx = 0;
			int pos = -1;
			for (int i = 0; i < n; ++i)
			{
				if (!b[i] && a[i].first * a[i].second > mx)
				{
					mx = a[i].first * a[i].second;
					pos = i;
				}
			}
			b[pos] = true;
		}

		for (int i = 0; i < n; ++i)
		{
			if (b[i]) break;

			int fpos = 0;
			long long int fv = 0;
			for (int j = 0; j < n; ++j)
			{
				if (b[j]) {
					fpos = j;
					fv = a[j].first * a[j].first;
					break;
				}
			}

			int pos = -1;
			long long int minrh = 999999999999999;
			for (int j = 0; j < n; ++j) {
				if (!b[j]) continue;
				if (a[j].first * a[j].second < minrh)
				{
					minrh = a[j].first * a[j].second;
					pos = j;
				}
			}

			long long int rr = a[i].first * a[i].first - fv;
			rr += 2 * (a[i].first * a[i].second - minrh);
			if (rr > 0)
			{
				b[i] = true;
				b[pos] = false;
				break;
			}
		}

		bool first = true;
		long long int res = 0;
		for (int i = 0; i < n; ++i) {
			if (!b[i]) continue;
			if (first) {
				res += (a[i].first * a[i].first);
				first = false;
			}
			res += (2 * a[i].first * a[i].second);
		}

		double result = (double)res * (double)M_PI;
		
		//out << fixed;
		out.precision(100);
		out << "Case #" << t << ": " << result << endl;
	}

	in.close();
	out.close();
	return 0;
}
#include<iostream>
#include<algorithm>
#include<fstream>
#include<string>
#include<vector>
#include<queue>
#include<unordered_map>
using namespace std;

int test;
long long int n, k;
unordered_map<long long int, long long int> a;

//vector<long long int> a;
//vector<int> cnt;

int cmp(int q, int r) { return q > r; }

int main()
{
	ifstream in("C-large.in");
	//ifstream in("input.txt");
	ofstream out("output.txt");
	in >> test;
	for (int t = 1; t <= test; ++t)
	{
		in >> n >> k;
		a.clear();

		a.insert(pair<long long int, long long int>(n, 1));

		long long int a1, a2;
		long long int curk = 0;
		while (1)
		{
			long long int num = -1;
			long long int cnt = 0;
			for (auto &x : a)
			{
				if (num < x.first)
				{
					num = x.first;
					cnt = x.second;
				}
			}

			a.erase(num);

			if (num % 2 == 1)
			{
				a1 = a2 = num / 2;
			}
			else
			{
				a1 = num / 2; a2 = num / 2 - 1;
			}

			if (curk + cnt >= k)
				break;

			curk += cnt;

			if (a1 == a2)
			{
				if (a.find(a1) == a.end())
					a.insert(pair<long long int, long long int>(a1, cnt * 2));
				else
					a[a1] += (cnt * 2);
			}
			else
			{
				if (a.find(a1) == a.end())
					a.insert(pair<long long int, long long int>(a1, cnt));
				else
					a[a1] += cnt;
				if (a.find(a2) == a.end())
					a.insert(pair<long long int, long long int>(a2, cnt));
				else
					a[a2] += cnt;
			}
		}

		out << "Case #" << t << ": " << max(a1, a2) << " " << min(a1, a2) << endl;
	}

	in.close();
	out.close();
	return 0;
}
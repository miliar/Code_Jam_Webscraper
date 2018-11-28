
#define _CRT_SECURE_NO_WARNINGS
#include<vector>
#include<iostream>
#include<algorithm>

using namespace std;

bool intersect_1(int a, int b, int c, int d) {
	if (a > b)  swap(a, b);
	if (c > d)  swap(c, d);
	return max(a, c) <= min(b, d);
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	cin >> test;
	for (int testNum = 0; testNum < test; ++testNum)
	{
		int n, p;
		cin >> n >> p;

		vector<int> standart(n);
		for (int i = 0; i < n; ++i)
		{
			cin >> standart[i];
		}

		vector<vector<pair<int, int> > > war(n, vector<pair<int,int> >(0));
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < p; ++j)
			{
				int tmp;
				cin >> tmp;
				int mi = (tmp * 10) / (standart[i] * 11);
				int x = (tmp * 10);
				int y = (standart[i] * 11);
				int z = (standart[i] * 9);
				if ((tmp* 10) % (standart[i] * 11) != 0)
					mi++;
				int ma = (tmp * 10) / (standart[i] * 9);

				if (mi <= ma)
				{
					war[i].push_back(make_pair(mi, ma));
				}
			}
			sort(war[i].begin(), war[i].end());
		}

		int pack = 0;

		for (int i = 0; i < war[0].size(); ++i)
		{
			bool allok = true;
			vector<int> indexs;
			for (int j = 1; j < n; ++j)
			{
				for (int k = 0; k < war[j].size(); ++k)
				{
					allok = false;
					if (intersect_1(war[0][i].first,war[0][i].second,war[j][k].first,war[j][k].second))
					{
						indexs.push_back(k);
						allok = true;
						break;
					}
				}
				if (!allok)
					break;
			}
			if (allok && indexs.size() == n-1)
			{
				for (int j = 1; j < n; ++j)
				{
					war[j][indexs[j - 1]] = make_pair(-1, -1);
				}
				++pack;
			}
		}

		cout << "Case #" << testNum + 1 << ": " << pack << endl;
	}
	return 0;
}
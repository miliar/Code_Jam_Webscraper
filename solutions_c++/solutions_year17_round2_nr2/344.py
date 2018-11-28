#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N = 1e3 + 7;

int ch[] = {'R', 'O', 'Y', 'G', 'B', 'V'};
vector<string> v[6];

bool cmp(int a, int b)
{
	return v[a].size() > v[b].size();
}

int main()
{
	ios::sync_with_stdio(false);

	int t;
	cin >> t;
	for (int T=0; T<t; T++)
	{
		cout << "Case #" << T+1 << ": ";
		for (int i=0; i<6; i++)
			v[i].clear();
		bool ok = true;
		int n;
		int a[6];
		cin >> n;
		for (int i=0; i<6; i++)
			cin >> a[i];
		vector<string> tmp[N];
		bool goood = false;
		for (int i=1; i<6; i+=2)
		{
			if (!a[i])
				continue;
			int p = (i + 3) % 6;
			if (a[p] < a[i])
				ok = false;
			else if (a[p] == a[i])
			{
				for (int j=0; j<6; j++)
					if (j != i && j != p && a[j] > 0)
					{
						ok = false;
					}
				string res;
				for (int j=0; j<a[p]; j++)
				{
					res.push_back(ch[p]);
					res.push_back(ch[i]);
				}
				v[p].push_back(res);
				a[p] = 0;
				goood = true;
				break;
			}
			string s;
			s.push_back(ch[p]);
			for (int j=0; j<a[i]; j++)
			{
				s.push_back(ch[i]);
				s.push_back(ch[p]);
			}
			a[p] -= a[i] + 1;
			v[p].push_back(s);
		}
		for (int i=0; i<6; i+= 2)
			for (int j=0; j<a[i]; j++)
			{
				string s;
				s.push_back(ch[i]);
				v[i].push_back(s);
			}
		int ind[3];
		for (int i=0; i<3; i++)
			ind[i] = 2 * i;
		sort(ind, ind+3, cmp);
		int sz = v[ind[0]].size();
		if (!goood)
		if (sz > (int)v[ind[1]].size() + (int)v[ind[2]].size() || !ok)
		{
			cout << "IMPOSSIBLE\n";
			continue;
		}
		for (int i=0; i<sz; i++)
			tmp[i].push_back(v[ind[0]][i]);
		for (int i=0; i<(int)v[ind[1]].size(); i++)
			tmp[i].push_back(v[ind[1]][i]);
		for (int i=0; i<(int)v[ind[2]].size(); i++)
			tmp[sz - 1 - i].push_back(v[ind[2]][i]);
		for (int i=0; i<sz; i++)
			for (auto x : tmp[i])
				cout << x;
		cout << "\n";
	}
	

	return 0;
}

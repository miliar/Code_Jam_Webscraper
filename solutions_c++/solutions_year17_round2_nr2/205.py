#define SUBMIT
#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:160777216")
#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <cmath>
#include <string>
#include <cstdio>
#include <ctime>
#include <cstring>
#include <cstdlib>
#include <sstream>

#define PI acos(-1.0)
#define VI vector<int>
#define PII pair<int,int>
#define MP make_pair
#define INF 1000000000000000007LL
#define eps 1e-12
#define ll long long
#define f0(i , n) for (int i = 0; i < n; i++)
#define NMAX 500000
using namespace std;

int i, j, n, m, t, test , k ;

int a[3][2];
int mx[3], mn[3] , cnt[3];

vector<string> get(string c1 , string c2 ,  int cnt1 , int cnt2 , int needcnt)
{
	int i, j, k;
	vector<string> ret;
	for (i = 0; i <= cnt2; i++)
	{
		if (i * 2 <= cnt1)
		{
			int x = cnt1 - 2 * i;
			int y = cnt2 - i;
			int total = i + x - y;
			if (total == needcnt)
			{
				cnt1 -= 2 * i;
				cnt2 -= i;
				for (j = 0; j < i; j++)
				{
					string s = c1 + c2 + c1;
					ret.push_back(s);
				}

				
				if (cnt2 > 0)
				{
					string s = c1;
					cnt1--;

					while (cnt2 > 0)
					{
						s += c2 + c1;
						cnt2--;
						cnt1--;
					}
					ret.push_back(s);
				}

				while (cnt1 > 0)
				{
					cnt1--;
					ret.push_back(c1);
				}
				return ret;
			}
		}
	}

}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	string c[3][2];
	c[0][0] = "R";
	c[0][1] = "G";
	c[1][0] = "B";
	c[1][1] = "O";
	c[2][0] = "Y";
	c[2][1] = "V";

	cin >> t;
	for (test = 1; test <= t; test++)
	{
		int R, O, Y, G, B, V;
		cin >> n;
		//cin >> R >> O >> Y >> G >> B >> V;
		cin >> a[0][0] >> a[1][1] >> a[2][0] >> a[0][1] >> a[1][0] >> a[2][1];
		int isans = 1;

		cout << "Case #" << test << ": ";
		
		int cont = 1;
		for (i = 0; i < 3; i++)
		{
			if (a[i][0] + a[i][1] == n)
			{
				if (a[i][0] == a[i][1])
				{
					for (j = 0; j < a[i][0]; j++)
						cout << c[i][0] << c[i][1];
					cout << endl;
				} else
					cout << "IMPOSSIBLE" << endl;
				
				cont = 0;
				break;
			}
			
				
		}

		if (!cont)
			continue;

		for (i = 0; i < 3; i++)
		{
			if (a[i][0] <= a[i][1] && a[i][0] + a[i][1] != 0)
				isans = 0;

			mx[i] = a[i][0] - a[i][1];
			mn[i] = 0;
			int x = a[i][0];
			int y = a[i][1];
			
			while (x - 2 >= 0 && y - 1 >= 0 &&  x - 2 > y - 1)
			{
				mn[i]++;
				x -= 2;
				y -= 1;
			}
			mn[i] += x - y;
		}
		
		if (isans == 0)
		{
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		
		
		int ansfound = 0;
		for (i = mn[0]; i <= mx[0] && !ansfound; i++)
		{
			for (j = mn[1]; j <= mx[1] && !ansfound; j++)
			{
				int curmin = abs(i - j);
				int curmax = i + j;

				int curl = max(curmin, mn[2]);
				int curr = min(curmax, mx[2]);

				if (curl <= curr)
				{
					ansfound = 1;
					cnt[0] = i;
					cnt[1] = j;
					cnt[2] = curl;
				}
			}
		}
		
		
		if (!ansfound)
		{
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		vector<string> v[3];
		v[0] = get("R", "G", a[0][0], a[0][1], cnt[0]);
		v[1] = get("B", "O", a[1][0], a[1][1], cnt[1]);
		v[2] = get("Y", "V", a[2][0], a[2][1], cnt[2]);
		
		int last = -1;
		string ans;
		int first = -1;
		while (v[0].size() || v[1].size() || v[2].size())
		{
			int max = 0, nom = 0;
			for (i = 0; i < 3; i++)
			{
				if (last != i && (v[i].size() > max || v[i].size() == max && first == i))
				{
					max = v[i].size();
					nom = i;
				}
			}

			if (first == -1)
				first = nom;
			ans += v[nom][v[nom].size() - 1];
			v[nom].pop_back();
			last = nom;
		}
		cout << ans << endl;
	}

	return 0;
}
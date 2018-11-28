#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <numeric>
#include <limits>
#include <functional>
#include <iomanip>
#include <fstream>

using namespace std;
typedef long long ll;
typedef long double ld;
int const INF = numeric_limits<int>::max();
string s = "#ROYGBV";

int const N = 10;
int const R = 1;
int const O = 2;
int const Y = 3;
int const G = 4;
int const B = 5;
int const V = 6;
int cnt[N], cnt_original[N];
int degree[N];
vector<int> g[N];
string const IMP = "IMPOSSIBLE";

string ans;
bool ok = true;

void get_ans(int u)
{
	ans.push_back(s[u]);
	cnt[u]--;
	vector<pair<int, int>> neigh;
	for (int v : g[u])
	{
		if (cnt[v] > 0 && ok)
		{
			//get_ans(v);
			neigh.push_back({ cnt[v], v });
		}
	}
	sort(neigh.begin(), neigh.end(), greater<pair<int, int>>());
	for (auto v : neigh)
	{
		if (cnt[v.second] > 0 && ok)
		{
			get_ans(v.second);
		}
	}
	ok = false;
}



int main()
{
	ios::sync_with_stdio(false);
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int tests;
	cin >> tests;
	g[R] = { Y, G, B };
	g[O] = { G, B, V };
	g[Y] = { B,V,R };
	g[G] = { V, R, O };
	g[B] = { R, O, Y };
	g[V] = { O, Y, B };
	for (int test = 1; test <= tests; test++)
	{
		ok = true;
		fill(degree, degree + N, 0);
		fill(cnt, cnt + N, 0);
		fill(cnt_original, cnt_original + N, 0);

		ans = "";
		int n;
		cin >> n;
		for (int i = 1; i <= 6; i++)
		{
			cin >> cnt[i];
			cnt_original[i] = cnt[i];
		}
		
		//for (int u = 1; u <= 6; u++)
		//{
		//	for (int v : g[u])
		//	{
		//		degree[u] += cnt[v] * cnt[u];
		//	}
		//}


		bool flag = true;
		//for (int u = 1; u <= 6; u++)
		//{
		//	if (cnt[u] > 0 && degree[u] < n / 2)
		//	{
		//		flag = false;
		//		break;
		//	}
		//}
		bool got_ans = false;


		for (int u = 1; u <= 6 && !got_ans; u++)
		{
			ans = "";
			ok = true;
			for (int i = 0; i < N; i++)
			{
				cnt[i] = cnt_original[i];
			}
			if (cnt[u] > 0)
			{
				get_ans(u);
				if (ans.size() == n)
				{
					int first = s.find(ans[0]);
					int last = s.find(ans[n - 1]);
					for (int v : g[first])
					{
						if (v == last)
						{
							cout << "Case #" << test << ": " << ans << endl;
							got_ans = true;
							break;
						}

					}
				}
				
			}
		}
		if (!got_ans)
		{
			cout << "Case #" << test << ": " << IMP << endl;
		}
		/*for (int u = 1; u <= 6; u++)
		{
			if (cnt[u] > 0)
			{
				get_ans(u);
				break;
			}
		}
		
		if (!flag || ans.size() < n)
		{
			cout << "Case #" << test << ": " << IMP << endl;
		}
		else
		{
			int first = s.find(ans[0]);
			int last = s.find(ans[n - 1]);
			for (int v : g[first])
			{
				if (v == last)
				{
					cout << "Case #" << test << ": " << ans.substr(0, n) << endl;
				}

			}
			
		}*/
	}
	return 0;
}


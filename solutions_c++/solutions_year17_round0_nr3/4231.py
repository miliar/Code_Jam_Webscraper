#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <set>

using namespace std;
string s, ans;
int t;
long long n, k, cur;
long long ss[1001000];
pair <long long, long long> p;

pair <long long, long long> solve(long long nn)
{
	if (nn % 2)
	{
		return{ nn / 2, nn / 2 };
	}
	else
		return{  nn / 2 - 1, nn / 2 };
}

int main()
{
	ios::sync_with_stdio(false);
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin >> t;

	for (int i = 0; i < t; i++)
	{
		fill(ss, ss + 1001000, 0);
		cin >> n >> k;
		ss[n] = 1;
		cur = n;
		for (int j = 0; j < k; j++)
		{
			while (ss[cur] == 0)
				cur--;
			ss[cur]--;
			p = solve(cur);
			ss[p.first]++;
			ss[p.second]++;
		}

		cout << "Case #" << i + 1 << ": ";
		cout << s << p.second << ' ' << p.first << endl;

	}
}
#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector <ll> vl;
typedef vector <pair <ll, ll>> vll;


void solve(int nn)
{
	int n, m;
	ld u, temp;
	ld ans = 1;
	cin >> n >> n;
	cin >> u;
	vector <ld> vec;
	vec.push_back(1);
	for (int i = 0; i < n; i++)
	{
		cin >> temp;
		vec.push_back(temp);
	}

	sort(vec.begin(), vec.end());

	int kol = 1;
	ld level = vec[0];
	bool flag = true;

	for (int i = 1; i < vec.size(); i++)
	{
		ld need = kol * (vec[i] - vec[i - 1]);
		if (u >= need)
		{
			u -= need;
			kol++;
			level = vec[i];
		}
		else
		{
			level += u / kol;
			for (int j = 0; j < kol; j++)
				ans *= level;
			for (int j = i; j < vec.size(); j++)
				ans *= vec[j];
			flag = false;
			break;
		}
	}

	cout << "Case #" << nn + 1 << ": " << ans;
	
	cout << endl;
}

int main()
{
	ios::sync_with_stdio(false);
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cout << setprecision(8) << fixed;
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
		solve(i);
	return 0;
}
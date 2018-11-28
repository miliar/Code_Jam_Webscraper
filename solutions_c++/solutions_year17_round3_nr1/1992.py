#define _CRT_SECURE_NO_WARNINGS
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <vector>
#include <stack>
#include <deque>
#include <math.h>
#include <map>
#include <fstream>
#include <iomanip>
#include <queue>
#include <bitset>
#include <math.h>

using namespace std;

typedef long long ll;
#define mp make_pair
#define N 100001
#define INF 100000000000000000

const int c = 1E9 + 7;
double const pi = 3.14159265358979323846264338327950288419716939937510;

vector<pair<double, int>> arr;

bool vis[10001];

int main()
{
	ofstream out;
	out.open("gcjc.txt");
	int t;
	cin >> t;
	for (int z = 1; z <= t; ++z)
	{
		int n, m;
		cin >> n >> m;
		for (int i = 0; i <= 1000; ++i)
			vis[i] = false;
		int ma = 0;
		for (int i = 0,x,y; i < n; ++i)
		{
			cin >> x >> y;
			arr.push_back(mp(pi * x * 2 * y, x));
		}
		bool yes = false;
		sort(arr.begin(), arr.end());
		reverse(arr.begin(), arr.end());
		double ans = 0;
		for (int i = 0; i < m - 1; ++i)
		{
			ans += arr[i].first;
			ma = max(ma, arr[i].second);
			vis[i] = true;
		}
		double tmp = 0;
		for(int i = 0; i < n; ++i)
		{
			if (!vis[i] && arr[i].first + pow(arr[i].second, 2) * pi > tmp && arr[i].second >= ma)
				tmp = pow(arr[i].second, 2) * pi + arr[i].first;
		}
		if (tmp < arr[m - 1].first + pow(ma, 2) * pi)
			ans += arr[m - 1].first + pow(ma, 2) * pi;
		else
			ans += tmp;
		out << "Case #" << z << ": " << setprecision(90) << ans << endl;
		arr.clear();
	}
	return 0;
}
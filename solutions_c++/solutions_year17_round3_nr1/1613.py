#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <utility>
#include <bitset>
#include <algorithm>
#include <set>
#include <iomanip>
#include <map>

using namespace std;

#define mp(a, b) make_pair(a,b)

long double EPS = 1e-9;

double pi = 3.14159265359;


vector<pair<long long int, int> > pred(vector<pair<long long int, long long int> > &a)
{
	vector<pair<long long int, int> > ans(a.size(), mp(0, -1));
	for (int i = 0; i < ans.size(); ++i)
	{
		ans[i].first = 2 * a[i].first * a[i].second;
		ans[i].second = i;
	}
	sort(ans.begin(), ans.end());
	reverse(ans.begin(), ans.end());
	return ans;
}

long long int calc(vector<pair<long long int, long long int> > &a, int st, vector<pair<long long int, int> > &post, int k)
{
	long long int width = a[st].first * a[st].first;
	long long int height = a[st].second * a[st].first * 2;

	int cur = 1;
	for (int i = 0; i < post.size(); ++i)
	{
		if (cur == k)
			break;
		if (post[i].second < st)
		{
			++cur;
			height += post[i].first;
		}
		if (post[i].second == st)
			continue;
		
	}

	if (cur != k)
	{
		return -1;
		
	}
	return width + height;
	
}

void f()
{
	int n, k;
	cin >> n >> k;
	vector<pair<long long int, long long int> > arr(n, make_pair(0, 0));
	for (int i = 0; i < n; ++i)
	{
		cin >> arr[i].first >> arr[i].second;
	}
	sort(arr.begin(), arr.end());

	vector<pair<long long int, int> > heights = pred(arr);
	long long int max = -1;
	for (int i = 0; i < arr.size(); ++i)
	{
		long long int tmp = calc(arr, i, heights, k);
		if (tmp > max)
			max = tmp;
	}
	cout << setprecision(7) << fixed << max*pi;
}

int main() {
	int n;
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	cin >> n;
	for (int i = 0;i < n;i++)
	{
		
		cout << "Case #" << i + 1 << ": ";
		f();
		cout << endl;
	}

	return 0;
}
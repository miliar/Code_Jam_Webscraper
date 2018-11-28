#pragma comment(linker,"/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <sstream>
#include <stdio.h>

#include <algorithm>
#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <functional>

#include <cmath>
#include <string>

#include <cassert>
#include <time.h>
#include <memory.h>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()

#define fi(n) for (int i = 0; i < (n); ++ i)
#define fj(n) for (int j = 0; j < (n); ++ j)
#define fin() for (int i = 0; i < n; ++ i)
#define fjm() for (int j = 0; j < m; ++ j)
#define forv(i, v) for (int i = 0; i < sz((v)); ++ i)


#ifdef _DEBUG
#define dbg(...) {fprintf(stderr, __VA_ARGS__); fflush(stderr);}
#define dbgx(x) {cerr << #x << " = " << x << endl;}
#else
#define dbg(...) { }
#define dbgx(x) { }
#endif

typedef unsigned long long ull;
typedef long long lint;
typedef pair < int, int > pii;
typedef long double ld;

const int INF = 1000 * 1000 * 1000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-9;

void prepare(string s)
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	if (sz(s) > 0)
	{
		freopen((s + ".in").c_str(), "r", stdin);
		freopen((s + ".out").c_str(), "w", stdout);
	}
#endif
}

int n;
int a, b, c;
int x, y, z;

void read()
{
	cin >> n;
	cin >> a >> x >> b >> y >> c >> z;
}

char A = 'R';
char B = 'Y';
char C = 'B';

bool fail(const string & s)
{
	for (int i = 0; i < sz(s) - 1; ++i)
	{
		if (s[i] == s[i + 1])
			return true;
	}
	if (s.front() == s.back())
		return true;
	return false;
}

void solve()
{
	string ans;
	vector<pair<int, char> > arr;
	arr.push_back(mp(a, A));
	arr.push_back(mp(b, B));
	arr.push_back(mp(c, C));
	while (arr[0].first != arr[1].first || arr[1].first != arr[2].first)
	{

		sort(all(arr), greater<pair<int, char>>());

		if (arr[2].first == 0)
			break;
		if (arr[1].first == 0)
			break;

		ans.push_back(arr[0].second);
		ans.push_back(arr[1].second);

		arr[0].first--;
		arr[1].first--;
	}

	if (arr[2].first == 0)
	{
		arr.pop_back();
	}

	if (ans.size() != 0)
	{
		if (ans.back() == arr[0].second)
			swap(arr[0], arr[1]);
		int sz = sz(arr) - 1;
		if (ans.front() == arr[sz].second)
			swap(arr[sz - 1], arr[sz]);
	}

	while (true)
	{
		int old_sz = sz(ans);
		for (int j = 0; j < sz(arr); ++j)
		{
			if (arr[j].first == 0)
				continue;
			arr[j].first--;
			ans.push_back(arr[j].second);
		}
		if (old_sz == sz(ans))
			break;
	}

	if (fail(ans))
	{
		ans = "IMPOSSIBLE";
	}


	cout << ans;
	cerr << ans;
}

int main()
{
	prepare("");


	//for (int a = 0; a < 5; ++a)
	//	for (int b = 0; b < 5; ++b)
	//		for (int c = 0; c < 5; ++ c)
	//{
	//	//read();
	//			::a = a;
	//			::b = b;
	//			::c = c;
	//			if (a + b + c < 3)
	//				continue;
	//	cout << "Case #" << a << " " << b << " " << c << ": ";
	//	//cerr << "Case #" << i + 1 << ": ";
	//	solve();
	//	cout << endl;
	//	cerr << endl;
	//}

	int T;
	cin >> T;
	fi(T)
	{
		read();
		cout << "Case #" << i + 1 << ": ";
		cerr << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
		cerr << endl;
	}

	return 0;
}

#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stack>
#include <map>
#include <ctime>
#include <set>
using namespace std;

#pragma comment(linker, "/STACK:167772160")

#define mp(x, y) make_pair(x, y)
#define sc(x) scanf("%d", &x)
#define sc2(x, y) scanf("%d %d", &x, &y)
#define scl(x) scanf("%I64d", &x)
#define scl2(x, y) scanf("%I64d %I64d", &x, &y)
#define forn(i, a, b) for(int i=a; i<b; ++i)
#define ford(i, a, b) for(int i=b-1; i>=a; --i)
#define all(x) x.begin(), x.end()
#define pr(x) printf("%d ", x)

typedef pair<int, int> pii;
typedef long long ll;

const long double EPS = 1e-8;
const long double PI = atan((long double)1) * 4;
const int inf = (int)1e9;
const ll INF = (ll)1e18;

typedef long double ld;

bool isTidy(ll x)
{
	int prevDigit = 9;
	while(x)
	{
		int digit = x % 10;
		x /= 10;
		if (digit > prevDigit)
			return false;
		prevDigit = digit;
	}
	return true;
}

ll f(ll n)
{
	vector<int> digits;
	while(n)
	{
		digits.push_back(n % 10);
		n /= 10;
	}
	reverse(all(digits));
	bool flag = false;
	for(int i=0; i+1<digits.size(); ++i)
		if(digits[i+1]<digits[i])
		{
			digits[i]--;
			forn(j, i + 1, digits.size())
				digits[j] = 9;
			flag = true;
			break;
		}
	ll ans = 0;
	forn(i, 0, digits.size())
		ans = ans * 10 + digits[i];
	if (flag)
		return f(ans);
	else 
		return ans;
	
}

void solve()
{
	int t;
	sc(t);
	forn(tt, 0, t)
	{
		ll n;
		scanf("%I64d", &n);
		printf("Case #%d: %I64d\n", tt + 1, f(n));
	}
}


int main()
{
	//gen();
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	solve();
#ifndef ONLINE_JUDGE
	fprintf(stderr, "Time: %.2lf\n", (double)clock() / CLOCKS_PER_SEC);
#endif
	return 0;
}
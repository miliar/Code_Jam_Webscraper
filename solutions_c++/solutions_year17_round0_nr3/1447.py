#include <bits/stdc++.h>
#define rep(i, a, b) for (int i = (a); i <= (b); ++i)
#define drep(i, a, b) for (int i = (a); i >= (b); --i)
#define REP(i, a, b) for (int i = (a); i < (b); ++i)
#define pb(x) push_back(x)
#define mp(x, y) (make_pair(x, y))
#define clr(x) memset(x, 0, sizeof(x))
#define xx first
#define yy second

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
const int inf = ~0U >> 1;
const ll INF = ~0ULL >> 1;
template <class T> inline void read(T &n)
{
    char c; int flag = 1;
    for (c = getchar(); !(c >= '0' && c <= '9' || c == '-'); c = getchar()); if (c == '-') flag = -1, n = 0; else n = c - '0';
    for (c = getchar(); c >= '0' && c <= '9'; c = getchar()) n = n * 10 + c - '0'; n *= flag;
}
//***************************

ll N, K;
set<ll> S;
map<ll, ll> c;

void run()
{
	S.clear();
	c.clear();
	scanf("%lld%lld", &N, &K);
	S.insert(-N); c[N] = 1;
	ll cur = 0;
	while (S.size())
	{
		pair<ll, ll> u;
		u.xx = -(*S.begin());
		u.yy = c[u.xx];
		S.erase(S.begin());
		
		ll l = u.xx / 2, r = u.xx - l - 1;
		if (l > r) swap(l, r);
		if (cur + u.yy >= K)
		{
			printf("%lld %lld\n", r, l);
			return;
		}
		cur += u.yy;
		if (l > 0 && l == r) 
		{
			c[l] += u.yy * 2;
			S.insert(-l);
		}
		else 
		{
			if (l > 0)
			{
				c[l] += u.yy;
				S.insert(-l);
			}
			if (r > 0)
			{
				c[r] += u.yy;
				S.insert(-r);
			}
		}
	}
}

int main(int argc, char *argv[])
{
	int cases;
	scanf("%d", &cases);
	rep(_, 1, cases)
	{
		printf("Case #%d: ", _);
		run();
	}
	return 0;
}

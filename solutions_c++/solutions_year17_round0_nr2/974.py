#include<iostream>
#include<cstdio>
#include<algorithm>
#include<queue>
#include<map>
#include<set>
#include<stack>
#include<cstring>
#include<string>
#include<vector>
#include<iomanip>
//#include<unordered_set>
//#include<unordered_map>
#include<cmath>
#include<list>
#include<bitset>
using namespace std;

#define ull unsigned long long
#define ll long long
#define lson l,mid,id<<1
#define rson mid+1,r,id<<1|1

typedef pair<int, int>pii;
typedef pair<ll, ll>pll;
typedef pair<double, double>pdd;
const double eps = 1e-6;
const int MAXN = 100005;
const int MAXM = 5005;
const ll LINF = 0x3f3f3f3f3f3f3f3f;
const int INF = 0x3f3f3f3f;
const double FINF = 1e18;
const ll MOD = 1000000007;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	string s;
	int t, cas = 0, pos;
	scanf("%d", &t);
	while (t--)
	{
		cin >> s;
		pos = s.size() - 1;
		for (int i = s.size() - 1; i >= 1; --i)
		{
			if (s[i] < s[i - 1])
			{
				s[i - 1]--;
				for (int k = pos; k >= i; --k)s[k] = '9';
				pos = i - 1;
			}
		}
		printf("Case #%d: ", ++cas);
		if (s[0] == '0')
		{
			for (int i = 1; i < s.size(); ++i)
			{
				cout << s[i];
			}
			cout << '\n';
		}
		else cout << s << '\n';
	}
}
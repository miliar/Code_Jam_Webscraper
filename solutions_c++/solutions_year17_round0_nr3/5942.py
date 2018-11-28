#define _CRT_SECURE_NO_DEPRECATE
#include <functional>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <numeric>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <bitset>
#include <queue>
#include <cmath>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <unordered_set>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
/*--------------------------------*/
#define pb push_back
#define INT_MIN (1 << 31)
#define INT_MAX ~(1 << 31)
#define LL_MIN -9223372036854775808
#define LL_MAX  9223372036854775807
#define lower(c) char(32 | c)
#define upper(c) char(~32 & c)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define RFOR(i, a, b) for (int i = a; i >= b; i--)
#define FORIT(i, a, b) for (auto i = a; i != b; i++)
#define READ freopen("input.txt", "r", stdin);
#define WRITE freopen("output.txt", "w", stdout);
#define MOD ll(1000000007)
#define PI acos(-1)
/*-------------------------------------------------------------*/

map<ull, set<pair<ull, ull>>> M;

int main() {


	int T;
	ll n, k;
	pair<ll, ll> res;
	scanf("%d\n", &T);

	FOR(t, 1, T){

		M.clear();
		scanf("%lld %lld", &n, &k);
		M[n].insert({ 1, n });

		while (k--){
			ull s = M.rbegin()->second.begin()->first, e = M.rbegin()->second.begin()->second;
			ull x = M.rbegin()->first, mid = (s + e) / 2;

			if (((mid - 1) - s) + 1) M[((mid - 1) - s) + 1].insert({ s, mid - 1 });
			if ((e - (mid + 1)) + 1) M[(e - (mid + 1)) + 1].insert({ mid + 1, e });

			M[x].erase(M[x].begin());
			if (M[x].empty()) M.erase(x);

			res = { max(mid - s, e - mid), min(mid - s, e - mid) };
		}

		printf("Case #%d: %lld %lld\n", t, res.first, res.second);
	}

	return 0;
}
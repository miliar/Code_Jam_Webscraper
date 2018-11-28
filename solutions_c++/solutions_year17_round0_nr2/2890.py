#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <list>
#include <set>
#include <cstdlib>
#include <vector>
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <stack>
#include <ctime>
#include <queue>
#include <map>
#include <cstring>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef bool bl;
typedef pair<bl, bl> pbl;
typedef pair<ld, ld> pld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
#define mp make_pair
#define ft first
#define sd second
#define forn(i, y, x) for(int i = y; i < x; i++)
#define ford(i, y, x) for(int i = y; i >= x; i--)
#define sz(x) (int)x.size()
#define all(x) x.begin(), x.end()
#define error exit(1)
const ll mod = (ll)1e9 + 7;
const int inf = (int)2e9;
const ll INF = (ll)1e18;
const int base = 1000 * 1000 * 1000;
const int maxn = 2005;
const ld pi = acosl(-1.0);
const ld eps = 1e-9;

char buff[1234];

void solve()
{
	int t;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++){
		scanf("%s", buff);
		string s(buff);
		bool isOk = false;
		while (!isOk){
			isOk = true;
			if (sz(s) == 1) break;
			for (int i = 1; i < sz(s); i++){
				if (s[i] < s[i - 1]){
					isOk = false;
					for (int j = i; j < sz(s); j++)
						s[j] = '9';
					int j = i - 1;
					while (s[j] == '0'){
						s[j] = '9';
						j--;
					}
					s[j]--;
					break;
				}
			}
		}
		int j = 0;
		while (s[j] == '0') j++;
		printf("Case #%d: ", tt + 1);
		for (int i = j; i < sz(s); i++)
			printf("%c", s[i]);
		printf("\n");
	}
}

int main()
{
#ifdef _DEBUG
	freopen("B-large(1).in", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	solve();
	return 0;
}
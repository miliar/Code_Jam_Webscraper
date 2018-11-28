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
//int dx[] = { -1, -1, 0, 1, 1, 1, 0, -1 };
//int dy[] = { 0, 1, 1, 1, 0, -1, -1, -1 };
//int dx[] = { -1, 0, 1, 0 };
//int dy[] = { 0, 1, 0, -1 };
/*-------------------------------------------------------------*/


struct cake{
	int r, h;
	ull x;
} arr[1000];

bool CMP(cake b, cake a){ return (b.r > a.r); }

int T, n, k; 
ull MAX;

void solve(int i, int t, ull res){
	if (t == k){
		MAX = max(MAX, res);
		return;
	}
	if (i < 0 || i >= n)return;


	solve(i + 1, t, res);


	res += arr[i].x;
	if (t) res -= ((ull)arr[i].r * arr[i].r);
	solve(i + 1, t + 1, res);
}

int main(){

	scanf("%d", &T);
	FOR(t, 1, T){
		MAX = 0;
		scanf("%d %d", &n, &k);
		FOR(i, 0, n - 1){
			scanf("%d %d", &arr[i].r, &arr[i].h);
			arr[i].x = ((ull)arr[i].r * arr[i].r) + (2 * (ull)arr[i].r * arr[i].h);
		}

		sort(arr, arr + n, CMP);
		solve(0, 0, 0);

		printf("Case #%d: %.8lf\n", t, MAX*PI);

	}

	return 0;
}
#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <stdio.h>
#include <set>
#include <stack>
#include <map>
#include <utility>
#include <numeric>
#include <queue>
using namespace std;

#define all(v) (v).begin(),(v).end()
#define allr(v) (v).rbegin(),(v).rend()
#define sz(a) int((a).size())
#define pb push_back
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end();i++)
#define mem(a, b) memset(a, b, sizeof(a))
#define mp make_pair
#define EPS      1e-9
#define F        first
#define S        second
#define sc(x)	 scanf("%d",&x)
#define scl(x)	 scanf("%I64d",&x)
#define sq(x)	 (x)*(x)
#define INF (1000000000)
#define oo (1ll<<60)

typedef stringstream ss;
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vll;
typedef vector<bool> vb;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
const int dx[] = { 0, 0, -1, 1 };
const int dy[] = { -1, 1, 0, 0 };

bool tidy(int n) {
	int prev = n % 10;
	n /= 10;
	while (n != 0) {
		if (prev < n % 10)
			return false;
		prev = n % 10;
		n /= 10;
	}
	return true;
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ",t);
		int n;
		cin >> n;
		while(!tidy(n--));
		n++;
		printf("%d\n",n);
	}
	return 0;
}


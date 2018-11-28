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

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		int arr[1000], k, cnt = 0;
		mem(arr, 0);
		string str;
		cin >> str;
		cin >> k;
		for (int i = 0; i < sz(str) - k; i++) {
			if (str[i] == '-' && arr[i] % 2 || str[i] == '+' && !(arr[i] % 2))
				continue;
			else {
				cnt++;
				for (int j = i; j < i + k; j++)
					arr[j]++;
			}

		}
		for (int i = sz(str) - 1; i >= k-1; i--) {
			if (str[i] == '-' && arr[i] % 2 || str[i] == '+' && !(arr[i] % 2))
				continue;
			else {
				cnt++;
				for (int j = i; j > i - k; j--)
					arr[j]++;
			}

		}

		bool can = true;
		for (int i = 0; i < sz(str); i++)
			if (!(str[i] == '-' && arr[i] % 2 || str[i] == '+' && !(arr[i] % 2))) {
				printf("IMPOSSIBLE\n");
				can = false;
				break;
			}

		if (can)
			printf("%d\n", cnt);
	}
	return 0;
}


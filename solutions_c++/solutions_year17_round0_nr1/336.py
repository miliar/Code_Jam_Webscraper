#define _USE_MATH_DEFINES
#include <algorithm>
#include <cstdio>
#include <functional>
#include <iostream>
#include <cfloat>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <time.h>
#include <vector>
#include <random>
#include <cassert>
using namespace std;

#define rep(i, N) for (int i = 0; i < N; i++)
#define pb push_back

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> i_i;
typedef pair<ll, int> ll_i;
typedef pair<int, ll> i_ll;
typedef pair<double, int> d_i;
typedef pair<ll, ll> ll_ll;
typedef pair<double, double> d_d;
typedef vector<int> vi;
struct edge { int v; ll w; };

const int MOD = 1000000007;
ll _MOD = 1000000009;
double EPS = 1e-10;
int INF = INT_MAX / 2;

int main() {
	int T; cin >> T;
	rep(t, T) {
		string s; int K;
		cin >> s >> K;
		int N = s.length(), ans = 0;
		for (int l = 0; l + K <= N; l++)
			if (s[l] == '-') {
				for (int i = l; i < l + K; i++)
					s[i] = '+' + '-' - s[i];
				ans++;
			}
		bool ok = true;
		rep(i, N) if (s[i] == '-') ok = false;
		printf("Case #%d: ", t + 1);
		if (ok) cout << ans;
		else cout << "IMPOSSIBLE";
		cout << endl;
	}
}

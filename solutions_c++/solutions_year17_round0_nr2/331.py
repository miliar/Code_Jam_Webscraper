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

bool f(string& s) {
	int N = s.length();
	rep(i, N - 1) if (s[i] > s[i + 1]) {
		s[i]--;
		for (int j = i + 1; j < N; j++) s[j] = '9';
		return true;
	}
	return false;
}

int main() {
	int T; cin >> T;
	rep(t, T) {
		string s; cin >> s;
		while (f(s));
		while (s.front() == '0') s.erase(s.begin());
		printf("Case #%d: ", t + 1);
		cout << s << endl;
	}
}

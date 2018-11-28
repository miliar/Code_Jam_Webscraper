#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <vector>
#include <string>
#include <iostream>
#include <cassert>
#include <map>
#include <algorithm>

using namespace std;

long long n, k;

void output(long long len)
{
    len --;
    long long a = len / 2;
    long long b = len - a;
    cout << b << ' ' << a << endl;
}

void dfs(long long len, long long cmin, long long cmax, long long k)
{
    map<long long, long long> m;
    long long a, b;
    a = len / 2; b = len - a;
    if (k <= cmax) {
        cout << b << ' ' << a << endl;
        return;
    }
    k -= cmax;

    m[a] += cmax;
    m[b] += cmax;
    a = (len - 1) / 2; b = len - 1 - a;
    if (k <= cmin) {
        cout << b << ' ' << a << endl;
        return;
    }
    k -= cmin;
    m[a] += cmin;
    m[b] += cmin;

    a = m.begin()->first;
    dfs(a, m[a], m[a + 1], k);
}

void solve()
{
    cin >> n >> k;
    dfs(n, 1, 0, k);
}

int main()
{
	//freopen("C-small-2-attempt0.in", "r", stdin); freopen("C-small-2-attempt0.out", "w", stdout);
	//freopen("C-small-attempt1.in", "r", stdin); freopen("C-small-attempt1.out", "w", stdout);
	//freopen("C-small-attempt2.in", "r", stdin); freopen("C-small-attempt2.out", "w", stdout);
	freopen("C-large.in", "r", stdin); freopen("C-large.out", "w", stdout);
	int test_case;
	cin >> test_case;
	for(int i = 0; i < test_case; ++ i) {
		printf("Case #%d: ", i + 1);
		cerr << "Start: " << i << endl;
		solve();
	}
	return 0;
}

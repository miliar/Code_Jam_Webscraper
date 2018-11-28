#include <cmath>
#include <map>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <vector>
#include <string>
#include <iostream>
#include <cassert>
#include <algorithm>

using namespace std;

int n, p;
map<vector<int>, int> mem;

int dfs(vector<int> a)
{
    if (mem.count(a)) return mem[a];
    int tmp = 0;
    int c = 0;
    for(int i = 0; i < p; ++ i) {
        c += i * a[i];
    }
    for(int i = 0; i < p; ++ i) {
        if (a[i]) {
            vector<int> b = a;
            b[i] --;
            int x = 0;
            if ((c - i) % p == 0) x = 1;
            tmp = max(tmp, dfs(b) + x);
        }
    }
    mem[a] = tmp;
    return tmp;
}

void solve()
{
    cin >> n >> p;
    vector<int> a(p);
    vector<int> zero(p, 0);
    mem[zero] = 0;
    for(int i = 0; i < n; ++ i) {
        int x;
        cin >> x;
        a[x % p] ++;
    }
    cout << dfs(a) << endl;
}

int main()
{
	//freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
	//freopen("A-small-attempt1.in", "r", stdin); freopen("A-small-attempt1.out", "w", stdout);
	//freopen("A-small-attempt2.in", "r", stdin); freopen("A-small-attempt2.out", "w", stdout);
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
	int test_case;
	cin >> test_case;
	for(int i = 0; i < test_case; ++ i) {
		printf("Case #%d: ", i + 1);
		cerr << "Start: " << i << endl;
		solve();
	}
	return 0;
}

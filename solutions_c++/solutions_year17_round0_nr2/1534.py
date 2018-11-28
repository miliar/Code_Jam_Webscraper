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
#include <algorithm>

using namespace std;

void solve()
{
    long long n;
    cin >> n;
    long long ret = 0;
    int tot = 0;
    for(long long m = n; m; m /= 10) ++ tot;
    int now = 1;
    for(int i = tot - 1; i >= 0; -- i) {
        for(int j = now; j < 10; ++ j) {
            long long tmp = 0;
            for(int k = i; k >= 0; -- k) tmp = tmp * 10 + 1;
            if (ret + tmp <= n) {
                ret += tmp;
                now ++;
            } else {
                break;
            }
        }
    }
    cout << ret << endl;
}

int main()
{
	//freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-attempt0.out", "w", stdout);
	//freopen("B-small-attempt1.in", "r", stdin); freopen("B-small-attempt1.out", "w", stdout);
	//freopen("B-small-attempt2.in", "r", stdin); freopen("B-small-attempt2.out", "w", stdout);
	freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout);
	int test_case;
	cin >> test_case;
	for(int i = 0; i < test_case; ++ i) {
		printf("Case #%d: ", i + 1);
		cerr << "Start: " << i << endl;
		solve();
	}
	return 0;
}

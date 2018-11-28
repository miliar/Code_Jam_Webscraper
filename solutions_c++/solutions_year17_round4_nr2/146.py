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

int n, m, c;

void solve()
{
    cin >> n >> c >> m;
    vector<int> cnt(c, 0);
    vector<int> freq(n, 0);
    for(int i = 0; i < m; ++ i) {
        int p, who;
        cin >> p >> who;
        --p, --who;
        cnt[who] ++;
        freq[p] ++;
    }
    int ans = *max_element(cnt.begin(), cnt.end());
    int sum = 0;
    for(int i = 0; i < n; ++ i) {
        sum += freq[i];
        int tmp = sum / (i + 1);
        if (sum % (i + 1)) tmp ++;
        ans = max(ans, tmp);
    }
    int promotion = 0;
    for(int i = 0; i < n; ++ i) {
        promotion += max(0, freq[i] - ans);
    }
    cout << ans << ' ' << promotion << endl;
}

int main()
{
	//freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-attempt0.out", "w", stdout);
	//freopen("B-small-attempt1.in", "r", stdin); freopen("B-small-attempt1.out", "w", stdout);
	//freopen("A-small-attempt2.in", "r", stdin); freopen("A-small-attempt2.out", "w", stdout);
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

#include <iostream>
#include <iomanip>
#include <cstring>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
#include <deque>
#include <set>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <fstream>

#define pb push_back
#define mp make_pair
#define F first
#define S second

#ifndef LOCAL
#define cerr if(0)cerr
#endif

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef long double ld;

const int INF = 2 * int(1e9);
const ll INFll = 1ll * int(1e9) * int(1e9);
const int MOD = 1000000007;

template<typename T, typename Q>
ostream& operator<<(ostream& out, pair<T, Q>& a) {
    out << a.F << " " << a.S;
    return out;
}

template<typename T, typename Q>
istream& operator>>(istream& in, pair<T, Q>& a) {
    in >> a.F >> a.S;
    return in;
}

template<typename T>
istream& operator>>(istream& in, vector<T>& a) {
    for (int i = 0; i < a.size(); ++i)
        in >> a[i];
    return in;
}

template<typename T>
ostream& operator<<(ostream& out, vector<T> a) {
    for (int i = 0; i < a.size(); ++i)
        if (i == a.size() - 1)
            out << a[i];
        else
            out << a[i] << " ";
    return out;
}

int solve() {
	int k[2];
	cin >> k[0] >> k[1];
	vi used[2] = {vi(24 * 60, 0), vi(24 * 60, 0)};
	for (int i = 0; i < 2; ++i) {
		for (int j = 0; j < k[i]; ++j) {
			int l, r;
			cin >> l >> r;
			for (int z = l; z < r; ++z)
				used[i][z] = 1;
		}
	}
	int answer = INF;
	for (int start = 0; start < 2; ++start) {
		vector<vector<vi> > dp(2, vector<vi>(721, vi(721, INF)));
		dp[start][0][0] = 0;
		for (int i = 0; i <= 720; ++i)
			for (int j = 0; j <= 720; ++j)
				for (int cur = 0; cur < 2; ++cur) {
					int minute = i + j;
                    if (dp[cur][i][j] != INF) {
                        if (i + 1 <= 720 && !used[0][minute])
                            dp[0][i + 1][j] = min(dp[0][i + 1][j], dp[cur][i][j] + (cur));
                        if (j + 1 <= 720 && !used[1][minute])
                            dp[1][i][j + 1] = min(dp[1][i][j + 1], dp[cur][i][j] + (cur ^ 1));
                    }
				}
		answer = min(answer, min(dp[start][720][720], dp[start ^ 1][720][720] + 1));
	}
	return answer;
}

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    for (int test = 1; test <= t; ++test) {
    	cout << "Case #" << test << ": " << solve() << endl;
    }
    cerr << fixed << setprecision(0) << "TIME = " << clock() / (ld)CLOCKS_PER_SEC * 1000 << "\n";
    return 0;
}

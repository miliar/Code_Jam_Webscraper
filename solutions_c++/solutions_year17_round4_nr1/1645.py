#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

const long long N = 1000000007;

void solve() {
    int N, P;
    vector<int> m(10);
    cin >> N >> P;
    for (int i = 0; i < N; i++) {
        int k; cin>> k;
        m[k % P] ++;
    }
    int ans = 0;
    if (P == 2) {
        ans += m[0];
        ans +=(1 + m[1] ) / 2;
    } else {
        if (P == 3) {
            ans += m[0];
            int k = min(m[1],m[2]);
            ans += k;
            m[1] -= k;
            m[2] -= k;
            for (int j = 1; j <= 2; j++) {
                if (m[j] > 0) {
                    ans += (m[j] + 2 ) / 3;
                }
            }
        } else if (P == 4) {
            ans += m[0];
            ans += m[2] / 2; m[2] = m[2]  % 2;
            int k = min(m[1], m[3]);
            ans += k;
            m[1] -= k; m[3] -= k;

            if (m[2] > 0) {
                if (m[1] >= 2) {
                    ans += 1;
                    m[2] -= 1; m[1] -= 2;
                }
            }

            if (m[2] > 0) {
                if (m[3] >= 2) {
                    ans += 1;
                    m[2] -= 1; m[3] -= 2;
                }
            }

            ans += (m[1] + 3 ) / 4;
            ans += (m[3] + 3) / 4;
        }
    }

    cout << ans;
}

int main()
{
	int cases;
	std::ios::sync_with_stdio(false);
	cin >> cases;
	for (int i = 1; i <= cases; i++) {
		cout <<"Case #" << i << ": ";
		solve();
		cout << endl;
	}
	return 0;
}

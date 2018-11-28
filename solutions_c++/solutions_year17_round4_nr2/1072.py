#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

const long long N = 1000000007;

int count(vector<int>& a, int k) {
    int ans = 0;
    for (auto p: a){
        if (p == k) ans ++;
    }
    return ans;
}
void solve() {
    int N;
    int C, M;
    cin >> N >> C >> M;
    vector<vector<int>> a(1100, vector<int>());
        vector<vector<int>> b(1100, vector<int>());

    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        a[u].push_back(v);
        b[v].push_back(u);
    }


    if (C == 2) {
        if (N == 1) {
            cout <<  M;
            return;
        }
        for (int i = 1; i <= 2; i++) {
            sort(b[i].begin(), b[i].end());
        }

        int k = max(b[1].size(), b[2].size());
        vector<int> cc(20);
        for (int i = 1; i <= 2; i++) {
            cc[i] = count(b[i], 1);
        }
        int r = cc[1] + cc[2];
        
        int k1 = b[1].size() -r;
        int k2 = b[2].size() -r;

        
        int ans2 = 0;
        for (int j = 2; j < 1010; j++) {
            int u1 = count(b[1], j) - cc[2];
            int u2 = count(b[2], j) - cc[1];
            ans2 = max(ans2, u1+u2-max(k1,k2));
        }
        
        if (r >= b[1].size() || r >= b[2].size()) {
            ans2 = 0;
        }
        ans2 = max(0, ans2);

        cout << max(r, k) <<" " << ans2;
        return;
    }
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

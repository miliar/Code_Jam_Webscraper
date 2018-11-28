// IOI 2018
#include <bits/stdc++.h>
using namespace std;

const int MAX = 1010;

int N;
const char c[] = {'R', 'O', 'Y', 'G', 'B', 'V'};
int a[6];
int nc;

void imp() { printf("Case #%d: IMPOSSIBLE\n", ++nc); }

typedef pair<int,int> ii;
void solve() {
	cin >> N; 
	for (int i = 0; i < 6; ++i) cin >> a[i]; 
	for (int i = 0; i < 6; ++i) if (a[i] > N / 2) return imp();
	vector<int> ans;
	int last = -1;
	for (int i = 1; i <= N; ++i) {
		int cur = -1, mx = 0;
		for (int j = 0; j < 6; ++j) if (j != last && a[j]) {
			a[j]--; bool ok = 1;
			for (int k = 0; k < 6; ++k) if (a[k] > (N - i + 1) / 2) { ok = 0; break; }
			if (!ok) { a[j]++; continue; }
			last = j;
			ans.push_back(j);
			break;
		}
		
	}
	printf("Case #%d: ", ++nc);
	for (int i = 0; i < ans.size(); ++i) printf("%c", c[ans[i]]); printf("\n");
}

int main() {
	freopen("B-small.in", "r", stdin);
	freopen("B.out", "w", stdout);
	ios_base::sync_with_stdio(false); cin.tie(0);
	int T; cin >> T;
	while(T--)
		solve();
}
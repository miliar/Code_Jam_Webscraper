#include<bits/stdc++.h>
using namespace std;
typedef long long li;
typedef pair<li, li> ii;
typedef vector<ii> vii;
#define pb push_back
#define mp make_pair
#define f first
#define sc second
int t;
li n, k, pick;
vii stall;
void pre_comp() {
	stall.assign(1000010, ii());
	for (int i = 1 ; i <= 1000000 ; i++) {
		if (i % 2 == 0) {
			stall[i].f = i / 2;
			stall[i].sc = i / 2 - 1;
		}
		else {
			stall[i].f = stall[i].sc = i / 2;
		}
	}
}
int main() {
	ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	pre_comp();
	cin >> t;
	for (int i = 1 ; i <= t ; i++)
	{
		ii ans;
		priority_queue<li> Q;
		cin >> n >> k;
		Q.push(stall[n].f);
		Q.push(stall[n].sc);
		k -= 1;
		ans.f = stall[n].f;
		ans.sc = stall[n].sc;
		while (k--) {
			pick = Q.top();
			Q.pop();
			ans.f = stall[pick].f;
			ans.sc = stall[pick].sc;
			Q.push(ans.f);
			Q.push(ans.sc);
		}
		while (!Q.empty()) {
			Q.pop();
		}
		cout << "Case #" << i << ": " << ans.f << " " << ans.sc << endl;
	}
	return 0;
}
#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

class stall {
public:
	int dist;
	stall(int d) 
	{
		dist = d;
	}
	bool stall::operator<(const stall& right) const 
	{
		return dist < right.dist;
	}
};

void solve()
{
	int n, k;
	cin >> n >> k;
	n++;
	priority_queue<stall> q;
	vector<int> v(1000003);
	stall s(n);
	q.push(s);
	v[n] = 1;
	int mn, mx, nd = n;
	while(k--) {
		stall st = q.top();
		if (v[st.dist] == 1) q.pop();
		v[st.dist]--;

		nd = st.dist / 2;
		int rem = st.dist % 2;

		if (v[nd] == 0) q.push(stall(nd));
		v[nd]++;
		mn = nd - 1;
		if (rem == 1) {
			if (v[nd + 1] == 0) q.push(stall(nd + 1));
			v[nd + 1]++;
			mx = mn + 1;
		} else {
			v[nd]++;
			mx = mn;
		}

		

	}

	cout << mx << " " << mn;

}

int main()
{
	freopen("small.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}

	return 0;
}
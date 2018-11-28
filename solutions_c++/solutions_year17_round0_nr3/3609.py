#include<bits/stdc++.h>
#define int long long
using namespace std;
#define rep(i,n) for(int i=0;i<(n);++i)
#define INF (1ll<<60)
typedef pair<int, int> pii;
#define FI first
#define SE second
#define all(s) s.begin(),s.end()
#define RREP(i,n) for(int i=(n)-1;i>=0;--i)
#define pb push_back
#define mp make_pair
#define l_b lower_bound
#define u_b upper_bound

int solve(int n, int k) {
	priority_queue<int> que;
	que.push(n);
	rep(i,k-1)
	{
		int x = que.top();
		x--;
		que.pop();
		que.push(x / 2);
		que.push(x - x / 2);
	}
	return que.top() - 1;
}

signed main() {
	int t;
	cin >> t;
	rep(i,t)
	{
		int n, k;
		cin >> n >> k;
		int len = solve(n, k);
		cout << "Case #" << i + 1 << ": " << len - len / 2 << " " << len / 2
				<< endl;
	}
}

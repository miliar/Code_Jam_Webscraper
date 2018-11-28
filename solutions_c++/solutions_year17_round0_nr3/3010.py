#include <bits/stdc++.h>
using namespace std;

#define EACH(i,c) for(__typeof((c).begin()) i = (c).begin();i!=(c).end();i++)
#define FOR(i,a,b)  for(int i=(a);i<(b);i++)
#define dbg(e)  cout<<(#e)<<" : "<<e<<endl
#define set(v,i) memset(v,i,sizeof(v))
#define all(x) x.begin(),x.end()
#define sz(x) int((x).size())
#define REP(i,n) FOR(i,0,n)
#define pb  push_back
#define mp make_pair

typedef long long LL;

LL test, n, x;


int main() {
	cin >> test;
	REP(tt, test) {
		cin >> n >> x;
		//cout << "input:(" << n << "," << x << ")" << endl;

		LL mini, maxi;
		queue <LL> have;
		map <LL,LL> nums;
		have.push(n);
		nums[n] = 1;

		while(x > 0) {
			LL now = have.front(); have.pop();
			LL cnt = nums[now];
			if (cnt == 0) continue;
			//if(tt == 1) 
			//cout << "(" << now << "," << cnt << "," << x << ")" << endl;
			
			if (x <= cnt) {
				mini = (now - 1) / 2;
				maxi = now / 2;
				x = 0;
				break;
			} 

			x -= cnt;
			// place the current person in the middle
			LL nxt = (now - 1);
			LL left = nxt / 2;
			LL right = (nxt + 1) / 2;
			/*
			if (tt == 1) {
				dbg(left);
				dbg(right);
			} */
			have.push(right);
			have.push(left);
			nums[now] -= cnt;
			nums[left] += cnt;
			nums[right] += cnt;
		}

		assert(x == 0);
		cout << "Case #" << tt + 1 << ": " << maxi << " " << mini << endl;
	}
	return 0;
}

#include<bits/stdc++.h>

using namespace std;

using LL = long long;

LL N, K;

pair<LL, LL> work(){
	cin >> N >> K;
	map<LL, LL> dic;
	priority_queue<LL> que;
	dic[N] = 1;
	que.push(N);
	while (K > 0) {
		LL x = que.top();
		que.pop();
		LL n = dic[x];
	//	cout << x << ' ' << n << ' ' << K << endl;
		LL rs = (x - 1) / 2;
		LL ls = x - 1 - rs;
		if (n >= K) {
			return make_pair(ls, rs);
		} else {
			K -= n;
			if (dic[ls] == 0) {
				que.push(ls);
			}
			dic[ls] += n;
			if (dic[rs] == 0) {
				que.push(rs);
			}
		//	cout << __LINE__ << ":" << ls << ' ' << n << endl;
		//	cout << __LINE__ << ":" << rs << ' ' << n << endl;
			dic[rs] += n;
		}
	}
	return make_pair(-1, -1);
}

int main(){
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		pair<LL, LL> ans = work();
		printf("Case #%d: ", i);
		cout << ans.first << ' ' << ans.second << endl;
	}
	return 0;
}

#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<vector>
#include<queue>
#include<map>
#include<stdio.h>
#include<string.h>
#include<string>
#include<set>
#include<stdlib.h>
#include<bitset>
using namespace std;
#define ll long long
struct state {
	int l, r;
	state(int _l, int _r) {
		l = _l;
		r = _r;
	}
	bool operator<(const state& obj)const {
		if ((r - l) != (obj.r - obj.l))
			return (r - l) < (obj.r - obj.l);
		return l > obj.l;
	}
};
int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif // !ONLINE_JUDGE
	int t,n,k;
	scanf("%d", &t);
	for(int i=1;i<=t;++i) {
		scanf("%d%d", &n, &k);
		priority_queue<state>pq;
		pq.push(state(0, n - 1));
		pair<int, int>ans;
		while (k > 0) {
			int low = pq.top().l;
			int high = pq.top().r;
			int mid = (low + high) / 2;
			pq.pop();
			--k;
			int ls = mid - low;
			int rs = high - mid;
			ans = make_pair(max(ls,rs), min(ls,rs));
			if (low != mid)
				pq.push(state(low, mid - 1));
			if (high != mid)
				pq.push(state(mid + 1, high));
		}
		printf("Case #%d: %d %d\n",i,ans.first,ans.second);
	}
}
#include <stdio.h>
#include <algorithm>
#include <string>
#include <iostream>
#include <map>
#include <queue>
using namespace std;
#define ll long long
int main(){
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	scanf("%d",&test);
	for(int tc=1; tc<=test; tc++){
		ll a, b;
		priority_queue<ll> q;
		map<ll, ll> mp;
		scanf("%lld %lld", &a, &b);
		mp[a] = 1;
		q.push(a);
		while(1){
			ll now = q.top(); q.pop();
			if(now == 1)break;
			ll nxt1 = (now-1)/2, nxt2 = now/2;
			if(mp.find(nxt1) == mp.end()){
				mp[nxt1] = mp[now];
				q.push(nxt1);
			}
			else mp[nxt1]+=mp[now];
			if(mp.find(nxt2) == mp.end()){
				mp[nxt2] = mp[now];
				q.push(nxt2);
			}
			else mp[nxt2]+=mp[now];
		}
		ll ans = 1;
		for(auto it = mp.end();;){
			if(it == mp.begin())break;
			it--;
			if(it->second >= b){
				ans = it->first;
				break;
			}
			b -= it->second;
		}
		printf("Case #%d: %lld %lld\n", tc, ans/2, (ans-1)/2);
		mp.clear();
	}
	return 0;
}

#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#define rep(i, l, r) for(int i = l; i <= r; ++i)
using namespace std;
typedef long long ll;
const pair<ll, ll> getValue(pair<ll, ll> &x){
	if(x.first <= 0 || x.second <= 0)
		return make_pair(0, 0);
	if(x.first & 1)
		return make_pair(x.first >> 1, x.first >> 1);
	else 
		return make_pair((x.first >> 1)-1, x.first >> 1);
}
const bool cmp(pair<ll, ll> &v1, pair<ll, ll> &v2){
	if(min(v1.first, v1.second) != min(v2.first, v2.second))
		return min(v1.first, v1.second) > min(v2.first, v2.second);
	if(max(v1.first, v1.second) != max(v2.first, v2.second))
		return max(v1.first, v1.second) > max(v2.first, v2.second);
	return 1;
}
void print(pair<ll, ll> x){
	printf("print (%lld %lld)\n", x.first, x.second);
}
int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out2.txt","w",stdout);
	int T;
	cin >> T;
	rep(cas, 1, T){
		ll n, m;
		pair<ll, ll> ans, now1, now2, next1, next2, next3 = make_pair(-1, -1), next4 = make_pair(-1, -1);
		cin >> n >> m;
		now1 = make_pair(n, 1);
		now2 = make_pair(0, 0);
		ans = getValue(now1);
		ll cnt = 1;
		while(m){
			pair<ll, ll> v1 = getValue(now1), v2 = getValue(now2);
			bool flag = cmp(v1, v2);
			if(flag){
				if(m > now1.second)
					m -= now1.second;
				else {
					ans = v1;
					break;
				}
				if(m > now2.second)
					m -= now2.second;
				else {
					ans = v2;
					break;
				}
			}
			else {
				if(m > now2.second)
					m -= now2.second;
				else {
					ans = v2;
					break;
				}
				if(m > now1.second)
					m -= now1.second;
				else {
					ans = v1;
					break;
				}
			}
			if(now1.first & 1){
				next1.first = now1.first >> 1;
				next1.second = 2 * now1.second + now2.second;
				next2.first = next1.first + 1;
				next2.second = now2.second;
			}
			else {
				next1.first = (now1.first >> 1) - 1;
				next1.second = now1.second;
				next2.first = next1.first + 1;
				next2.second = now1.second + 2*now2.second;
			}
			now1 = next1;
			now2 = next2;
			//merge(now1, now2, next1, next2, next3, next4);
		}
		printf("Case #%d: ", cas);
		cout << max(ans.first, ans.second) << " " << min(ans.first, ans.second) << '\n';
	}
	return 0;
}

#include<iostream>
#include<cstdio>
#include<cstring>
#define rep(i, l, r) for(int i = l; i <= r; ++i)
using namespace std;
const int maxn = 10100;
int s[maxn], cnt[maxn], pre[maxn];
int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int T, n, m;
	cin >> T;
	rep(cas, 1 , T){
		int n,C, m,ans1 = 0, ans2 = 0;
		cin >> n >> C >>m;
		rep(i, 1, C)
			cnt[i]  = 0;
		rep(i, 1, n)
			s[i] = pre[i] = 0;
		rep(i, 1, m){
			int p, id;
			cin >> p >> id;
			s[p]++;
			cnt[id]++;
			if(cnt[id] > ans1)
				ans1 = cnt[id];
		}
		rep(i, 1, n)
			pre[i] = pre[i - 1] + s[i];
		rep(i, 1, n)
			ans1 = max(ans1, (pre[i] + (i-1)) / i);
		rep(i, 1, n)
			ans2 += max(0, (s[i] - ans1));
		printf("Case #%d: %d %d\n", cas, ans1, ans2);
	}
	return 0;
} 
/*
1
5 4
6 7 3 5 9
*/

#include<iostream>
#include<cstdio>
#include<cstring>
#define rep(i, l, r) for(int i = l; i <= r; ++i)
using namespace std;
int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int T, n, m, ans;
	cin >> T;
	rep(cas, 1 , T){
		cin >> n >> m;
		ans = 0;
		if(m == 2){
			int cnt = 0;
			rep(i, 1, n){
				int x;
				scanf("%d", &x);
				if(x % m == 0)
					ans ++;
				else 
					++cnt;
			}
			ans += (cnt+1)/2;
			printf("Case #%d: %d\n", cas, ans);
		}
		else if(m == 3){
			int cnt1 = 0, cnt2 =0;
			rep(i, 1, n){
				int x;
				scanf("%d", &x);
				if(x % m == 0)
					ans ++;
				else {
					if(x % m == 1)
						cnt1++;
					else 
						cnt2++;
				}
			}
				int v = min(cnt1, cnt2);
				//printf("v = %d\n", v);
				ans += v;
				cnt1 -= v;
				cnt2 -= v;
				ans += (cnt1 + cnt2 + 2) / 3;
			printf("Case #%d: %d\n", cas, ans);
		}
		else {
			int cnt1 = 0, cnt2 = 0, cnt3 = 0;
			rep(i, 1, n){
				int x;
				scanf("%d", &x);
				if(x % m == 0)
					++ans;
				else if(x % m == 1)
					cnt1++;
				else if(x % m ==2)
					cnt2++;
				else cnt3++;	
			}
			//printf("cnt = %d %d %d\n", cnt1, cnt2, cnt3);
			int v = min(cnt1, cnt3);
			ans += v;
			cnt1 -= v;
			cnt3 -= v;
			ans += cnt2 / 2;
			cnt2 %= 2;
			if(cnt2 > 0){
				if(cnt1 > 0){
					ans ++;
					cnt1 = max(0, cnt1 - 2);
				}
				else if(cnt3  > 0 ){
					ans ++;
					cnt3 = max(0, cnt3 - 2);
				}
				else {
					ans ++;
				}
			}
			if(cnt1 > 0){
				ans += (cnt1+3)/4;
			}
			else {
				ans += (cnt3+3)/4;
			}
			printf("Case #%d: %d\n", cas, ans);
		}
	}
	return 0;
} 
/*
1
5 4
6 7 3 5 9
*/

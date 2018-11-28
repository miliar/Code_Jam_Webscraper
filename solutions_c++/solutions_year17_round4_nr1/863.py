#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>

using namespace std;
int cnt[10];
int main() {
	int T;
	cin >> T;	
	for(int cas = 1; cas <= T; ++cas) {
		int N, P;
		cin >> N >> P;
		for(int i = 0; i < P; ++i) {
			cnt[i] = 0;
		}
		int sum = 0;
		for(int i = 1; i <= N; ++i) {
			int tmp;
			cin >> tmp;
			cnt[tmp % P]++;
			sum += (tmp % P);
			sum %= P;
		}
		int ans = 0;
		if(P == 2) {
			ans += cnt[0];
			ans += cnt[1] / 2;
		} else if(P == 3) {
			ans += cnt[0];
			while(cnt[1] > 0 && cnt[2] > 0) {
				ans ++;
				cnt[1] --;
				cnt[2] --;
			}
			ans += cnt[1] / 3;
			ans += cnt[2] / 3;
		} else if(P == 4) {
			ans += cnt[0];
			while(cnt[1] > 0 && cnt[3] > 0) {
				ans ++;
				cnt[1] --;
				cnt[3] --;
			}
			while(cnt[2] > 1) {
				ans ++;
				cnt[2] -= 2;
			}
			if(cnt[2] == 1) {
				if(cnt[1] >= 2) {
					cnt[1] -= 2;
					ans++;
				} else if(cnt[3] >= 2) {
					cnt[3] -= 2;
					ans++;
				}
			}
			ans += cnt[1] / 4;
			ans += cnt[3] / 4; 
		}
		printf("Case #%d: %d\n",cas,ans+1-(sum==0));
	}
}
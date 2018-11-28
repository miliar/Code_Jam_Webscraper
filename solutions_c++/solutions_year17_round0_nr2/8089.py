#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
int bits[1000];
LL work(LL num) {
	int len = 0;
	while(num > 0) {
		bits[++len] = num % 10;
		num /= 10; 
	}
	while(1) {
		bool vis = 0;
		for(int i = len;i > 1;-- i) {
			if(bits[i] > bits[i-1]) {
				vis = 1;
				bits[i] = bits[i] - 1;
				for(int j = i-1;j > 0;-- j) {
					bits[j] = 9;
				}
				break;
			}
		}
		if(!vis) break;
	}
	LL x = 0;
	for(int i = len;i > 0;-- i) {
		x = x * 10 + bits[i];
	}
	return x;
}
int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T = 0;
	LL num = 0;
	scanf("%d",&T);
	for(int t = 1;t <= T;++ t) {
		cin >> num;
		LL ans = work(num);
		printf("Case #%d: %lld\n",t,ans);
	}
	return 0;
} 

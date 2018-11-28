#include<bits/stdc++.h>
using namespace std;
#define ll long long

int T;
ll n;
int a[25];

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("x.out", "w", stdout);
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t){
		printf("Case #%d: ", t);
		scanf("%lld", &n);
		ll nn = n;
		int m = 0;
		while(nn){
			a[++m] = nn % 10;
			nn /= 10;
		}
		int i = m; ll ans = 0;
		while(i > 1 && a[i - 1] >= a[i]) i--;
		if(i == 1) ans = n;
		else{
			while(i < m && a[i] == a[i + 1]) ++i;
			for(int j = m; j > i; --j) ans = ans * 10 + a[j];
			ans = ans * 10 + a[i] - 1;
			for(int j = 1; j < i; ++j) ans = ans * 10 + 9;
		}
		printf("%lld\n", ans);
	}
	return 0;
}

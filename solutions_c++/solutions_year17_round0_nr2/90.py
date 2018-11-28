#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <cstdlib>
#define maxn 1009
using namespace std;
long long n;
int tot;
int a[maxn], b[maxn];
void init(long long n){
	while(n){
		a[tot++] = n % 10;
		n /= 10;
	}
}
bool check(int *a, int tot){
	for(int i = tot - 1; i >= 1; i--){
		if(a[i] <= a[i - 1])
			continue;
		else
			return 0;
	}
	return 1;
}
long long get9(int x){
	long long ans = 0;
	for(int i = 0 ; i < x; i++){
		ans *= 10;
		ans += 9;
	}
	return ans;
}

long long getb(int n){
	long long ans = 0;
	for(int i = n - 1; i >= 0; i--){
		ans *= 10;
		ans += b[i];
	}	
	return ans;
}

int main(){
	freopen("/Users/fengweiming/ProgramContest/GoogleCodeJam2017/QualificationRound/B.in", "r", stdin);
	freopen("/Users/fengweiming/ProgramContest/GoogleCodeJam2017/QualificationRound/B.out", "w", stdout);
	int tt, cot = 1;
	scanf("%d", &tt);
	while(tt--){
		tot = 0;
		scanf("%lld", &n);
		init(n);
		if(check(a, tot))
			printf("Case #%d: %lld\n", cot++, n);
		else{
			long long ans = get9(tot - 1);
			for(int i = tot - 1; i >= 0; i--){
				if(i == tot - 1 && a[i] <= 1)
					continue;
				if(a[i] <= 0)
					continue;
				for(int j = tot - 1; j > i; j--)
					b[j] = a[j];
				b[i] = a[i] - 1;
				for(int j = i - 1; j >= 0; j--)
					b[j] = 9;
				if(check(b, tot))
					ans = max(ans, getb(tot));
			}
			printf("Case #%d: %lld\n", cot++, ans);
		}
	}
	return 0;
}
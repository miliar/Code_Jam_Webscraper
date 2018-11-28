#include <bits/stdc++.h>

using namespace std;
#define LL long long
const int maxn = 1005;
const double pi = 3.14159265358979323846;

struct cake{
	LL r, h;
	LL s;
}a[maxn];
LL b[maxn];

bool cmp(cake X, cake Y){
	return X.r > Y.r;
}

bool cmpp(LL x, LL y){
	return x > y;
}

double solve(){
	int n, k;
	LL ans = 0;
	cin >> n >> k;
	for (int i = 0; i < n; i++){
		scanf("%lld%lld", &a[i].r, &a[i].h);
		a[i].s = 2 * a[i].r * a[i].h;
	}
	sort(a, a + n, cmp);
	LL temp = 0;
	for (int i = 0; i <= n - k; i++){
		temp = a[i].r * a[i].r + a[i].s;
		for (int j = i + 1; j < n; j++)
			b[j - i - 1] = a[j].s;
		sort(b, b + n - 1 - i, cmpp);
		for (int j = 1; j < k; j++)
		temp += b[j - 1];
		ans = max(ans, temp);
	}
	return double(ans) * pi;
}

int main(){
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
		printf("Case #%d: %.9lf\n", i, solve());
	return 0;
}

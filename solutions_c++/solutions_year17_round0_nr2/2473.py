#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define f(i, x, n) for (int i = x; i < (int)(n); ++i)

int main(){
	freopen("main.in", "r", stdin);
	freopen("main.out", "w", stdout);
	int t;
	scanf("%d", &t);
	f(tc, 1, t + 1){
		printf("Case #%d: ", tc);
		ll n;
		scanf("%lld", &n);
		vector<int> x;
		while (n)x.push_back(n % 10), n /= 10;
		reverse(x.begin(), x.end());
		f(i, 1, x.size())if (x[i] < x[i - 1]){
			--x[i - 1];
			f(j, i, x.size())x[j] = 9;
			--i;
			while (i > 0 && x[i] < x[i - 1])x[i] = 9, --x[--i];
			break;
		}
		ll an = 0;
		f(i, 0, x.size())an = an * 10 + x[i];
		printf("%lld\n", an);
	}
}

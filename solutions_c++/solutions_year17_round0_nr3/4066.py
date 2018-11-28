#include <bits/stdc++.h>

using namespace std;

long long n, k;

int main() {
	//freopen("C-small-2-attempt0.in", "r", stdin);
	//freopen("C-small-2-attempt0.out", "w", stdout);
	int T, tCase = 0;	scanf("%d", &T);
	while(T --) {
		scanf("%I64d%I64d", &n, &k);
		printf("Case #%d: ",++ tCase);
		int d = 0;
		long long u = k;
		while(u) {++d, u >>= 1;}
		-- d;
		long long val = n+1-(1<<d);
		long long kk = (1<<d)+val%(1<<d);
		val /= (1<<d);
		if(kk > k) val ++;
		//cout << "\nval : " << val << endl;
		val --;
		//cout << "\nval : " << val << endl;
		printf("%I64d %I64d\n", (val+1)/2, val/2);
	}
	return 0;
}
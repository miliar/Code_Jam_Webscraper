#include <cstdio>
#include <cstring>

using namespace std;

long long solve(long long x)
{
	//printf("%lld\n", x);
	int d[20], l = 0;
	while (x){
		d[l ++] = x % 10; x /= 10;
	}
	for (int i = 0; i < l; i ++){
		bool f = true;
		for (int j = l-1; j > i && f; j --)
			if (d[j] > d[j-1]) f = false;
		if (f && i && ((i == l-1 && d[i] == 1) || (i < l-1 && d[i] == d[i+1])))
			f = false;
		if (f){
			//printf("%d: %d\n", i, d[i]);
			x = 0;
			for (int j = l-1; j >= i; j --)
				x = x * 10 + d[j];
			if (i) x --;
			for (int j = i-1; j >= 0; j --)
				x = x * 10 + 9;
			return x;
		}
	}
	x = 0;
	for (int i = 0; i < l-1; i ++)
		x = x * 10 + 9;
	return x;
}

int main()
{
	freopen("b1.in", "r", stdin);
	freopen("b1.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t ++)
	{
		long long x;
		scanf("%lld", &x);
		printf("Case #%d: %lld\n", t, solve(x));
	}
	return 0;
}

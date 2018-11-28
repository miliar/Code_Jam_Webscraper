#include <cstdio>

int t;
long long n;

int countDigit(long long n) {
	int ans = 0;	
	while (n > 0) {
		n /= 10;
		ans++;
	}

	return ans;
}

long long pow(long long a, int b) {
	if (b == 0) {
		return 1LL;
	}

	if ((b & 1) == 0) {
		long long tmp = pow(a, b / 2);

		return 	tmp * tmp;
	} 
	
	long long tmp = pow(a, (b - 1) / 2);
	
	return tmp * tmp * a;
}

long long dfs(long long target, int digit, long long current, int prevDigit) {
	if (digit == 0) {
		if (current <= target) {
			return current;
		} else {
			return -1;
		}
	}

	if (current > target) {
		return -1;
	}

	for (int i = 9; i >= prevDigit; i--) {
		long long check = dfs(target, digit - 1, current + 1LL * i * pow(10LL, digit - 1), i);

		if (check != -1) {
			return check;
		}
	}

	return -1;
}
int main() {
	scanf("%d", &t);

	for (int i = 0; i < t ; i++) {
		scanf("%lld", &n);
		
		int digit = countDigit(n);
		printf("Case #%d: %lld\n", i + 1, dfs(n, digit, 0LL, 0));
	}
}

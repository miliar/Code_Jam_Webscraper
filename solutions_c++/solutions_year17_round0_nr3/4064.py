#include<cstdio>
#include<queue>

long long solve(long long n, long long k) {
	printf("%lld %lld\n", n, k);
	//if (n == k)
	//	return 0;
	if (k == 0)
		return -1;
	if (k == 1)
		return n;
	k--;
	n--;

	long long n1,n2,k1,k2;
	n1 = n2 = n/2;
	if (n%2==1)
		n2++;
	k1 = k2 = k/2;
	if (k%2==1)
		k2++;
	long long a1, a2;
	a1 = solve(n1,k1);
	a2 = solve(n2,k2);
	printf("%lld %lld (%lld, %lld, %lld) (%lld, %lld, %lld)\n", n,k, n1,k1,a1,n2,k2,a2);
	if (a1 > a2)
		return a1;
	else
		return a2;
}

long long solve2(long long n, long long k) {
	std::priority_queue<long long> segmentos;
	segmentos.push(n);
	while (--k) {
		long long n = segmentos.top();
		if (n == 1)
			return 1;
		printf("%lld\n",n);
		segmentos.pop();
		n--;
		long long n1,n2;
		n1 = n2 = n/2;
		if (n%2==1)
			n2++;
		if (n1 > 0)
			segmentos.push(n1);
		if (n2 > 0)
			segmentos.push(n2);
	}
	printf("%lld\n",segmentos.top());
	return segmentos.top();
}

int main() {
	int t;
	scanf("%d", &t);
	for (int _t = 1; _t <= t; _t++) {
		long long n,k;
		scanf("%lld %lld", &n, &k);
		long long answer = solve2(n,k)-1;
		long long max, min;
		max = min = answer/2;
		if (answer%2==1)
			max++;
		printf("Case #%d: %lld %lld\n", _t, max, min);
	}
	return 0;
}


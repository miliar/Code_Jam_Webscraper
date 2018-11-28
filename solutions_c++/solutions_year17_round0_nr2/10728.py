#include <cstdio>
#include <cstring>

using namespace std;

bool arrumado(long long n ){
	while (n > 0){
		if (n % 10 < (n / 10) % 10){
			return false;
		}
		n = n/10;
	}
	return true;
}

long long last_number(long long n){
	while (n > 0){
		if(arrumado(n)){
			return n;
		}
		n--;
	}
}

int main() {
	int t; scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		register long long n; scanf("%lld", &n);
		printf("Case #%d: %lld\n", tc, last_number(n));
	}
}
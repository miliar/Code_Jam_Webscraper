#include <cstdio>
#include <vector>
using namespace std;

const int N = 20;
char a[N];

typedef long long lint;

lint ston(char a[]){
	int len = strlen(a);
	lint ten = 1;
	lint ret = 0;

	for (int i = len - 1; i >= 0; --i){
		ret += ten * (lint)(a[i] - '0');
		ten *= 10;
	}

	return ret;
}

lint P(lint a, lint b){
	lint ret = 1;
	for (int i = 0; i < b; ++i){
		ret *= a;
	}
	return ret;
}

lint go(char a[]){
	int len = strlen(a);
	
	bool ok = false;
	int idx;
	for (int i = 0; i < len-1; ++i){
		if (a[i] > a[i - 1]){
			ok = true;
			idx = 1;
		}
	}
	if (!ok)
		return ston(a);
	
	lint p1 = P(10LL, len - idx - 1LL);
	a[idx + 1] = '\0';
	return p1*(ston(a)-1) + p1 - 1;
}

lint get(lint n){
	lint ret = 0;
	while (n){
		++ret;
		n /= 10LL;
	}
	return ret;
}



lint go(lint n){
	lint len = get(n);
	lint ten = 1;
	lint ret = 0;
	
	for (int i = len - 1; i >= 0; --i){
		if (i == 0 && n){
			ret += n*ten;
			
		}
		else if (((n / 10) % 10) <= n % 10){
			ret += (n % 10) * ten;
			n /= 10;
		}
		else{
			ret = 10 * ten - 1;
			n = (n / 10) - 1;
		}
		ten *= 10LL;
	}
	return ret;
}

int main(){
	freopen("input.txt", "r",stdin);
	freopen("output.txt", "w",stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i){
		lint n;
		scanf("%lld", &n);
		printf("Case #%d: %lld\n", i,go(n));
	}
	return 0;
}
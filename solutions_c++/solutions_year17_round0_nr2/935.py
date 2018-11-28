#include<bits/stdc++.h>

using namespace std;

char s[100];

int check(const char * s){
	int l = strlen(s);
	for (int i = 0; i < l-1; ++i) {
		if (s[i] > s[i+1]) {
			return i;
		}
	}
	return -1;
}

long long work(){
	long long n, N;
	long long m = 0;
	scanf("%s", s);
	int l = strlen(s);
	int mark = -1;
	
	sscanf(s, "%lld", &n);
	while ((mark = check(s)) != -1) {
		n = 0;
		int l = strlen(s);
		for (int i = 0; i <= mark; ++i) {
			n = n * 10 + (s[i] - '0');
		}
		for (int i = mark+1; i < l; ++i) n *= 10;
		n -= 1;
		sprintf(s, "%lld", n);
	}
	return n;
}

int main(){
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		printf("Case #%d: %lld\n", i, work());
	}
	return 0;
}

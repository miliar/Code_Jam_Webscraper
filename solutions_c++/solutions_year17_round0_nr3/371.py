#include <stdio.h>
#include <string.h>

int T;
int n, k;
long long int Ra, Rb;

int h[1000001];
int hp = 0;

void push(int v) {
	h[++hp] = v;
	int p = hp;
	while(p > 1) {
		if(h[p] < h[p / 2]) break;
		h[p] = h[p / 2];
		p /= 2;
	}
	h[p] = v;
}

int pop() {
	if(hp == 0) return 0;
	int v = h[1];
	int p = 1, pp;
	h[1] = h[hp--];
	while(p * 2 <= hp) {
		pp = p * 2;
		if(pp + 1 <= hp && h[pp] < h[pp + 1]) pp++;
		if(h[p] > h[pp]) break;
		h[pp]^=h[p]^=h[pp]^=h[p];
		p = pp;
	}
	return v;
}


int foo(int C) {
	hp = 0;
	scanf("%d %d", &n, &k);

	push(n);
	int j, v;
	for(j=0;j<k-1;j++) {
		v = pop();
		if((v-1)/2) push((v - 1) / 2);
		if(v/2) push(v / 2);
	}

	v = pop();
	Ra = v/2, Rb = (v-1)/2;
	
	printf("Case #%d: ", C);
	printf("%lld %lld\n", Ra, Rb);
}

int main() {
	scanf("%d", &T);
	for(int i=0;i<T;i++) {
		foo(i+1);
	}
	return 0;
}


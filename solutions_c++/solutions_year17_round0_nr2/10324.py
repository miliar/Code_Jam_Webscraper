#include <stdio.h>

bool orden(int x) {
	int ultimo=x%10;
	x/=10;
	while(x) {
		if(x%10>ultimo)
			return false;
		ultimo=x%10;
		x/=10;
	}
	return true;
}

int f(int x) {
	while(!orden(x)) x--;
	return x;
}

int main() {
	int T,x;
	scanf("%d",&T);
	for(int t=1;t<=T;t++) {
		scanf("%d",&x);
		printf("Case #%d: %d\n",t,f(x));
	}
	return 0;
}

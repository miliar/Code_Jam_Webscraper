#include <bits/stdc++.h>
#include <string.h>
#define MAXN 2000

using namespace std;

int main(void) {
	int v[MAXN];
	char s[MAXN];
	int t;
	
	scanf("%d", &t);
	
	int k, cont, tam, ans;
	bool possible;
	for(int test = 1; test <= t; test++) {
		possible = true;
		memset(v,0,sizeof(int)*MAXN);
		cont = ans = 0;
		getchar();
		scanf("%s", s);
		tam = strlen(s);
		scanf("%d", &k);
		for(int i = 0; i < tam; i++) {
			if(v[i] == 1) cont = (cont + 1)%2;
			if(cont == 1) s[i] = (s[i] == '+' ? '-' : '+');
			if(s[i] == '-') {
				ans++;
				cont = (cont + 1)%2;
				v[i+k] = 1;
			}
			if(i + k > tam && s[i] == '-') possible = false;
		}
		printf("Case #%d: ", test);
		if(possible) printf("%d\n", ans);
		else puts("IMPOSSIBLE");
	}
	
	
	return 0;
}
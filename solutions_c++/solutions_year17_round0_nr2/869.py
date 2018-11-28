#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	int tc, cn;
	char N[10000];
	scanf("%d", &tc);
	for(cn = 1; cn <= tc; cn++) {
		scanf("%s", N);
		int l = strlen(N);
		int i;
		for(i = l - 2; i >= 0; i--)
			if(N[i] > N[i + 1]) {
			  N[i]--;
			  for(int j = i + 1; N[j]; j++)
			    N[j] = '9';
			}
		printf("Case #%d: ", cn);
		i = 0;
		if(N[0] == '0')
		  i++;
		for(; N[i]; i++)
		  printf("%c", N[i]);
		puts("");
	}
	return 0;
}

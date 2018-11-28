#include <bits/stdc++.h>

using namespace std;

#define N 1000

char s[N + 1];
int n, k;

void flip(int x){
	int i;

	for (i = x; i < x + k; i++){
		s[i] = (s[i] == '-' ? '+' : '-');
	}
}

bool check(){
	int i;

	for (i = 0; i < n; i++){
		if (s[i] == '-'){
			return false;
		}
	}

	return true;
}

int main(){
	int t, ans, i, j;

	scanf("%d\n", &t);

	for (i = 1; i <= t; i++){
		scanf("%[^ ]%n %d\n", s, &n, &k);

		for (j = 0, ans = 0; j < n - k + 1; j++){
			if (s[j] == '-'){
				flip(j);
				ans++;
			}
		}

		if (check()){
			printf("Case #%d: %d\n", i, ans);
		}
		else{
			printf("Case #%d: IMPOSSIBLE\n", i);
		}
	}

	return 0;
}